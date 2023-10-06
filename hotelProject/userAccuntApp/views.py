from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateUserForm , LoginForm ,UpdateUserForm
from userAccuntApp.forms import GuestForm
from userAccuntApp.forms import Guest



def register(request):
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid:
           current_user =  form.save(commit=False)
           form.save()
           guest = Guest.objects.create(
               user = current_user,name=form.cleaned_data['first_name']
               ,lastname=form.cleaned_data['last_name']
               ,email=form.cleaned_data['email'])
           
           messages.success(request,'You sign up successfully')  
           return redirect('home')
        else:
            messages.error(request,'Invalid Form')
    else:
        form = CreateUserForm()
    
    context = {'form':form}
    return render(request,'register.html', context= context)



def my_login(request):
    
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data= request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                print('user logged in')
                messages.success(request,'You logged in successfully')
                return redirect('home')
    
    context ={'form':form}
    return render(request,'log_in.html', context=context)


def log_out(request):

    auth.logout(request)
    messages.success(request,'You logout successfully')
    return redirect('home')



@login_required(login_url='my_login')
def registerGuest(request):
    
    ins = Guest.objects.get(user=request.user)

    if request.method == 'POST':
        form = GuestForm(request.POST, instance=ins)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            birth_date = form.cleaned_data['birth_date']
            checkin_date = form.cleaned_data['checkin_date']

            form.name = name
            form.lastname = lastname
            form.email = email
            form.birth_date = birth_date
            form.checkin_date = checkin_date
            form.save()
            messages.success(request,'Your register is successfully Done')
        else:
            messages.error(request,'Invalid profile')
    else:
        form = GuestForm(instance=ins)
    
    
    context = {
        'form': form,
    }
    return render(request, 'registerguest.html', context=context)



