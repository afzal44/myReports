from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.models import user_type, User
from .forms import NewUserForm
def signup(request):
    form = NewUserForm(request.POST)
    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        dr = request.POST.get('doctor')
        pt = request.POST.get('patient')
        lab = request.POST.get('lab')
        
        user = User.objects.create_user(
            email=email,
        )
        user.set_password(password)
        user.save()
        
        usert = None
        if dr:
            user_dr = user_type(user=user,is_doctor=True)
        elif pt:
            user_pt = user_type(user=user,is_patient=True)
        elif lab:
            user_lab = user_type(user=user,is_lab=True)
        
        usert.save()
        #Successfully registered. Redirect to homepage
        return redirect('home')
    return render(request=request, template_name="users/register.html", context={"register_form":form})
    
    
def login(request):
    if (request.method == 'POST'):
        email = request.POST.get('email') #Get email value from form
        password = request.POST.get('password') #Get password value from form
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_patient:
                return redirect('phome') #Go to student home
            elif user.is_authenticated and type_obj.is_doctor:
                return redirect('dhome') #Go to teacher home
            elif user.is_authenticated and type_obj.is_lab:
                return redirect('lhome') #Go to teacher home
        else:
            # Invalid email or password. Handle as you wish
            return redirect('home')

    return render(request, 'home.html')
def phome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_patient:
        return render(request,'patient_home.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_doctor:
        return redirect('dhome')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_lab:
        return redirect('lhome')
    else:
        return redirect('login')
                      
def dhome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_patient:
        return render(request,'patient_home.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_doctor:
        return redirect('dhome')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_lab:
        return redirect('lhome')
    else:
        return redirect('home')
def lhome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_patient:
        return render(request,'patient_home.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_doctor:
        return redirect('dhome')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_lab:
        return redirect('lhome')
    else:
        return redirect('home')