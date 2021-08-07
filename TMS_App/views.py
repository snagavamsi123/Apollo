from django.shortcuts import redirect, render
from .forms import signupform,loginform,ticketsform
from .models import signup,tickets
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.core.cache import cache

@cache_control(no_cache=True,no_store=True,must_revalidate=True)
def home(request):
    return render(request,'home.html')

def signuppage(request):
    if request.method=='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            form = signupform
            message = 'Signup Successfull'
            return render(request,'signup.html',{'form':form,'message':message})
        else:
            message = 'Signup Failed,Please Try again'
            return render(request,'signup.html',{'form':form,'message':message})
      
    form = signupform
    return render(request,'signup.html',{'form':form})


def UserLogin(request):

    if request.method=='POST':
        global user_email
        form = loginform(request.POST)
        userid = request.POST['Email']
        password = request.POST['Password']
        signup_data = signup.objects.all()
        for data in signup_data:
            if data.Email == userid and data.Password == password:
                request.session['Email_ID']=data.Email
                return render(request,'user_home.html',{'name':data.Name,'user_email':data.Email})
        
        else:
            form = loginform
            message = 'Authentication Failed'
            return render(request,'login.html',{'form':form,'message':message})

    
    form = loginform
    return render(request,'login.html',{'form':form})

def newticket(request):
    
    if request.method=='POST':

        form = ticketsform(request.POST)
        Entered_Type = request.POST['Type']
        Entered_Floor = request.POST['Floor']
        Entered_Desk_No = request.POST['Desk_No']
        Entered_Description = request.POST['Description']
        if form.is_valid():
            form.save()
            user_email = request.session['Email_ID']
            
            tickets.objects.filter(Description=Entered_Description).filter(Desk_No=Entered_Desk_No).filter(Floor=Entered_Floor).filter(Type=Entered_Type).update(User=user_email)
            message = 'Ticket Raised Successfully'
            form = ticketsform()
            return render(request,'user_newticket.html',{'form':form,'message':message})

    form = ticketsform()
    return render(request,'user_newticket.html',{'form':form})

def oldtickets(request):

    user_email = request.session['Email_ID']
    data=tickets.objects.filter(User=user_email)
    return render(request,'user_tickets.html',{'data':data})

def editticket(request,id):
    if request.method=='POST':
        updated_Type = request.POST['Type']
        updated_Floor = request.POST['Floor']
        updated_Desk_No = request.POST['Desk_No']
        updated_Description = request.POST['Description']

        tickets.objects.filter(id=id).update(Type=updated_Type,Floor=updated_Floor,Desk_No=updated_Desk_No,Description=updated_Description)
        return redirect('/oldtickets')
    
    edit_ticket = tickets.objects.get(id=id)
    return render(request,'user_edit.html',{'edit_ticket':edit_ticket})

def AdminLogin(request):
    if request.method=='POST':
        userid = request.POST['username']
        password = request.POST['password']

        admin = authenticate(username = userid,password=password)
        if admin is not None:
            return render(request,'admin_home.html')
        else:
            form = loginform
            message = 'Authentication Failed'
            return render(request,'adminlogin.html',{'form':form,'message':message})

    form = AuthenticationForm
    return render(request,'adminlogin.html',{'form':form})

def admin_all(request):
    data = tickets.objects.all()
    return render(request,'admin_alltickets.html',{'data':data})

def AdminEditTicket(request,id):
    if request.method=='POST':
        updated_Type = request.POST['Type']
        updated_Floor = request.POST['Floor']
        updated_Desk_No = request.POST['Desk_No']
        updated_Description = request.POST['Description']
        updated_Status = request.POST['Status']
        updated_Admin_comments = request.POST['Admin_comments']

        tickets.objects.filter(id=id).update(Type=updated_Type,Floor=updated_Floor,Desk_No=updated_Desk_No,Description=updated_Description,Status=updated_Status,Admin_comments=updated_Admin_comments)
        return redirect('/alltickets')
    
    edit_ticket = tickets.objects.get(id=id)
    return render(request,'admin_edittickets.html',{'edit_ticket':edit_ticket})


    

