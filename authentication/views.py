from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control, never_cache
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Profile

def index(request):
    return render(request, 'home/index.html')

@never_cache
def login(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'authentication/login.html')

@never_cache
@login_required(login_url='login')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'Logged Out')
        return redirect('login')

def signup(request):


    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email Taken')
                return redirect('signup')
            else:

                if fname[0] != fname[0].upper():
                    fname=fname.capitalize()
                if lname[0] != lname[0].upper():
                    lname=lname.capitalize()

                print(fname+' '+lname)
                user = User.objects.create_user(username=username, 
                                                first_name=fname,
                                                last_name=lname,
                                                email=email,
                                                password=pass1)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = Profile(user=user_model, id_user=user_model.id)
                new_profile.save()
                messages.success(request, 'Profile Created')
                return redirect('login')

        else:
            messages.warning(request, 'Passwords do not match')
            return redirect('signup')


    return render(request, 'authentication/signup.html')

def profile(request):
    
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(id_user=user.id)
    context = {'user':user, 'profile':profile}
    return render(request, 'authentication/profile.html', context)

@csrf_exempt
def updateProfile(request):
    
    if request.method == 'POST':
        profileData = {
            "firstname": request.POST['firstname'],
            "lastname": request.POST['lastname'],
            "username": request.POST['username'],
            "email": request.POST['email'],
        }

        user = User.objects.get(id=request.user.id)
        
        if user.username != profileData['username']:
            if User.objects.filter(username=profileData['username']).exists():
                return JsonResponse({"errorMessage":"Username Taken"}, status=400)
        elif user.email != profileData['email']:
            if User.objects.filter(email=profileData['email']).exists():
                return JsonResponse({"errorMessage":"Email Taken"}, status=400)
        else:
            user.username = profileData['username']
            user.first_name = profileData['firstname']
            user.last_name = profileData['lastname']
            user.email = profileData['email']

            user.save()

            return JsonResponse({"profileData":profileData}, status=200)

    else: return JsonResponse({}, status=400)

@csrf_exempt
def updateDetails(request):
    
    if request.method == 'POST':
        detailsData = {
            "address1": request.POST['address1'],
            "address2": request.POST['address2'],
            "location": request.POST['location'],
            "zipcode": request.POST['zipcode'],
        }

        user = User.objects.get(id=request.user.id)
        
        details = Profile.objects.get(id_user=user.id)

        details.address1 = detailsData['address1']
        details.address2 = detailsData['address2']
        details.location = detailsData['location']
        details.zipcode = detailsData['zipcode']

        details.save()

        return JsonResponse({"userDetails":detailsData}, status=200)
    
    else: return JsonResponse({}, status=400)


    

    