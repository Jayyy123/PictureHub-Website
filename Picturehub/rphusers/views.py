from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile,Socials,AddSocials
from .forms import UserProfileForm,UserForm

def auth(request):
    return render(request, 'rphusers/auth.html')

def loginpage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']

        try:
            user =  User.objects.get(username=username)
        except:
            messages.error(request,"Username does not exist")
        
        user =  authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "{} You have successfully logged in".format(username))
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in {}\nPlease check your details and try again.".format(username))

    return render(request, 'rphusers/login.html')

def logoutt(request):
    logout(request)
    return redirect('login')

def signup(request):

    if request.user.is_authenticated:
        return redirect('home')

    a = UserForm()
    if request.method=="POST":
        username = request.POST['username']
        a = UserForm(request.POST)

        if a.is_valid():
            user =  a.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request, "{} you have successfully signed up and you have been logged in.".format(username))
            return redirect('profile')

        else:
            messages.error(request, '{}, there was an error creating your account'.format(username))

    return render(request, 'rphusers/signup.html', {'a':a})

def profile(request):
    if request.user.is_authenticated:
        username = request.user
    
        try:
            userr = UserProfile.objects.get(username=username)

        except:
            u = User.objects.get(username=username)

            userr = UserProfile.objects.create(
                user = u,
                username = u.username,
                first_name = u.first_name,
                last_name = u.last_name,
                email = u.email,
            )

        user = UserProfile.objects.get(username=username)
            
    return render(request, 'rphusers/profile.html', {'a':user})

def profileform(request,pk):
    user = UserProfile.objects.get(id=pk)
    a = UserProfileForm(instance=user)
    if request.method=="POST":
        a= UserProfileForm(request.POST, request.FILES,instance=user)
        if a.is_valid:
            a.save()
            return redirect('profile')

    return render(request, 'rphusers/profileform.html',{'a':a})
