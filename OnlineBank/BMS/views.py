# from _typeshed import Self
from django.contrib import messages
from django.http import request, response
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import render, redirect
from .models import Feedback, NewAccounts, creditcards
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate


# ---------------- Creat Account Function --------------->
def CreatAccount(request):
    if request. method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        paswo = request.POST.get('password')
        phonenumber = request.POST.get('phoneNum')
        Emaile = request.POST.get('maile')
        nationalId = request.POST.get('national_id')
        Balanc = request.POST.get('balanc')
        accountType = request.POST.get('account_type')
        confirmPassword = request.POST.get('confirm_password')
        if paswo == confirmPassword:
            if(NewAccounts.objects.filter(password=paswo).exists()):
                return render(request, 'CreatAccount.html', {"message": "Password is usable try again"})
            elif NewAccounts.objects.filter(national_id=nationalId).exists() and NewAccounts.objects.filter(account_type=accountType).exists():
                return render(request, 'CreatAccount.html', {"message": 'Account already found'})
            else:
                x = NewAccounts(firstname=fname, lastname=lname,  password=paswo, phoneNum=phonenumber, maile=Emaile,
                                national_id=nationalId, balanc=Balanc,  account_type=accountType)
                x.save()
                return render(request, 'CreatAccount.html', {"message": "Account Created Succesfully"})
        else:
            return render(request, 'CreatAccount.html', {"message": "password not matching"})
        # return redirect('/')
        return redirect('/')
    else:
        return render(request, 'CreatAccount.html')
#----------------- End of Creat Account function -----------------#


#-----------------  Registration function -----------------#
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']

        if psw == psw_repeat:
            if User.objects.filter(username=username).exists():
                return render(request, 'login.html', {"message": "Username is already taken"})
            elif User.objects.filter(email=email).exists():
                return render(request, 'login.html', {"message": "Emaile is Found"})
            else:
                user = User.objects.create_user(
                    username=username, password=psw, email=email)
                user.save()
            return render(request, 'login.html', {"message": "Sign Up Successfully"})
        else:
            return render(request, 'login.html', {"message": "password not matching"})
    else:
        return render(request, 'login.html')
#----------------- End of Registration function -----------------#


#----------------- Login function -----------------#
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {"message": 'invalid username or password'})
    else:
        return render(request, 'login.html')
#----------------- End of Login function -----------------#


#----------------- Logout function -----------------#
def logout(request):
    auth.logout(request)
    return redirect('/')
#----------------- End of Logout function -----------------#


#---------------- forget password function ---------------#
# change login to forget password form
def forgetPassword(request):
    if request.method == 'POST':
        username = request.POST['username']
        newpsw = request.POST['new_psw']
        newpsw_repeat = request.POST['new_psw_repeat']

        if newpsw == newpsw_repeat:
            user = auth.authenticate(username=username)
            if user is None:
                u = User.objects.get(username=username)
                u.set_password(newpsw)
                u.save()
                return render(request, 'login.html', {"message": "Password Changed Succesfullty.."})
            else:
                return render(request, 'forgetPassword.html', {"message": "User Not Found"})
        else:
            return render(request, 'forgetPassword.html', {"message": "password not matching"})
        return redirect('forgetPassword')

    else:
        return render(request, 'forgetPassword.html')
#---------------- End forget password function ---------------#


#---------------- money transection function function ---------------#
def transections(request):
    if request.method == 'POST':
        user1ID = request.POST.get('User1_ID')
        Accpass = request.POST.get('Account_password')
        user2ID = request.POST.get('User2_ID')
        amount = request.POST.get('amount')
        #x = NewAccounts.objects.filter(national_id=user1ID, password=Accpass)
        user1 = NewAccounts.objects.get(national_id=user1ID)
        if user1 is not None:
            #user1 = NewAccounts.objects.get(password=Accpass)
            user2 = NewAccounts.objects.get(national_id=user2ID)
            if user2 is not None:
                if user1.balanc >= int(amount):
                    user1.balanc = user1.balanc - int(amount)
                    user2.balanc = user2.balanc + int(amount)
                    user1.save()
                    user2.save()
                    return render(request, 'transections.html', {"message": "succesddful"})
                else:
                    return render(request, 'transections.html', {"message": "Account 2 ID not found"})
        else:
            return render(request, 'transections.html', {"message": "Invalid Account ID or password "})
    else:
        return render(request, 'transections.html')


#-------------------credit card Function-----------#


def creditcardForm(request):
    if request. method == 'POST':
        fname = request.POST.get('Name')
        age = request.POST.get('age')
        monthlySalary = request.POST.get('Month_salary')
        phonenumber = request.POST.get('phone')
        Emaile = request.POST.get('maile')
        Card_type = request.POST.get('card_type')

        x = creditcards(fullname=fname, phoneNum=phonenumber, maile=Emaile, monthluSalary=monthlySalary,
                        type=Card_type, Age=age)
        x.save()
        return render(request, 'creditcardForm.html', {"message": "Thanks,Your request will be reviewed "})
    return render(request, 'creditcardForm.html')
#------------End of credit card functions-----------#

#-------------------contact Us Function-----------#


def contactUs(request):
    if request.method == 'POST':
        fname = request.POST.get('Fname')
        lname = request.POST.get('Lname')
        subjet = request.POST.get('subject')
        Emaile = request.POST.get('maile')
        Message = request.POST.get('message')
        data = Feedback(firstname=fname, lastname=lname,
                        subjet=subjet, message=Message, maile=Emaile)
        data.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

#------------End of ccontact Us Function-----------#


def cred(request):
    return render(request, 'cred.html')
