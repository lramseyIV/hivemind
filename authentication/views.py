from django.shortcuts import render, redirect
from django.contrib import sessions, messages
from .models import User, VerificationURL
import bcrypt
from .helper_functions import create_verification_url, send_email, gen_password

# views.py for authentication app

# LOGIN 
def login(request):
    if request.method == "GET":
        return render (request, 'login.html')
    if request.method =="POST":
        form_username = request.POST['username']
        form_password = request.POST['password']
        if User.objects.filter(username= form_username):
            user = User.objects.get(username = form_username)
            stored = user.password
            if bcrypt.checkpw(form_password.encode(), stored.encode()):
                # check if user is verified if so send to profile else send verify
                if not user.is_verified:
                    return redirect ('/auth/verify')
                request.session['id'] = user.id
                return redirect('/profile')
        messages.error(request, "username or password invalid")
        return render (request, "login.html")

#REGISTRATION
def register(request): # both get and post
    if request.method =="GET":
        return render (request, 'register.html')
    if request.method =="POST":
        errors = User.validator.auth_validator(request)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return render (request, "register.html")
        if User.objects.filter(username=request.POST['username']) or User.objects.filter(email=request.POST['email']):
            messages.error(request, "Username or email already taken")
            return render (request, "register.html")
        form_password = request.POST['password']
        hashed_password = bcrypt.hashpw(form_password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(username = request.POST['username'], password=hashed_password, email=request.POST['email'], phone=request.POST['phone'])
        # create verification url to send to user
        url = create_verification_url()
        VerificationURL.objects.create(user_id=user.id, url_string=url)
        message = f"Hivemind Account Verification\n http://127.0.0.1:8000/auth/confirm/{url}"
        send_email(user.email, message)
        return redirect ('/auth/verify')

# LET USER KNOW TO CHECK EMAIL
def verify(request): # Tell Customer to verify via email.
    return render (request, 'confirm_notify.html')


# LOGOUT
def logout(request):
    if 'id' in request.session:
        del request.session['id']    
    return redirect ('/auth/login')

# HANDLE VERIFICATION URL
def confirm_account(request, url_string): #takes url string and verifies account
    if VerificationURL.objects.filter(url_string=url_string):
        vurl = VerificationURL.objects.get(url_string=url_string)
        user = User.objects.get (id=vurl.user_id)
        user.is_verified = True
        user.save()
        vurl.delete()
        request.session['id'] = user.id
        return redirect("/profile")
    return redirect("/auth/verify")

# AUTH RELATED (changing passwords, forgot passwords MFA etc)
def forgot_password(request):
    # will send user email with new password
    if request.method=="GET":
        return render(request, "forgot_password.html") # NEED TO CREATE HTML
    if request.method=="POST":
        if User.objects.filter(email=request.POST['email']):
            user = User.objects.get(id=int(request.session['id']))
            new_pw = gen_password()
            user.password = bcrypt.hashpw(new_pw.encode(), bcrypt.gensalt()).decode()
            user.save()
            send_email(user.email, f'Hivemind Password Reset\n Password: {new_pw}')
        messages.info(request, "If your email exists we sent you a new temporary password via email.")
        return render (request, "login.html")



