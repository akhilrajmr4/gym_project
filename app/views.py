import os
import random
from django.shortcuts import render, redirect
from app.models import *
from datetime import datetime, date, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django. contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django.db.models import Q
from Gym_Main.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# **********Login**********


def login(request):
    Trainer = designation.objects.get(designation="Trainer")
    Trainee = designation.objects.get(designation="Trainee")
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect('SuperAdmin_Dashboard')
        else:

            if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation=Trainer.id, status="active").exists():

                member = user_registration.objects.get(
                    email=request.POST['email'], password=request.POST['password'])
                request.session['Tnr_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['Tnr_id'] = member.id

                return redirect('Trainer_dashboard')

            elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation=Trainee.id, status="active").exists():

                member = user_registration.objects.get(
                    email=request.POST['email'], password=request.POST['password'])
                if member.net_due_date == None:
                    context = {
                        'msg_error': 'Please contact admin to verify account and pay first payment'}
                    return render(request, 'login.html', context)
                else:
                    dd = (member.net_due_date - datetime.now().date()).days
                    if (dd >= 0):
                        request.session['Tne_id'] = member.designation_id
                        request.session['usernamets1'] = member.fullname
                        request.session['Tne_id'] = member.id
                        return redirect('Trainee_Dashboard')
                    else:
                        context = {
                            'msg_error': 'Your registration End. Please renew registration'}
                        return render(request, 'login.html', context)

            else:
                context = {'msg_error': 'Invalid data'}
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


# ***********Reset Password************

def reset_password(request):
    if request.method == "POST":
        email_id = request.POST.get('email')
        access_user_data = user_registration.objects.filter(
            email=email_id).exists()
        if access_user_data:
            _user = user_registration.objects.get(email=email_id)
            password = random.SystemRandom().randint(100000, 999999)

            _user.password = password
            subject = ' your authentication data updated'
            message = 'Password Reset Successfully\n\nYour login details are below\n\nUsername : ' + str(email_id) + '\n\nPassword : ' + str(password) + \
                '\n\nYou can login this details\n\nNote: This is a system generated email, do not reply to this email id'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_id, ]
            send_mail(subject, message, email_from,
                      recipient_list, fail_silently=True)

            _user.save()
            msg_success = "Password Reset successfully check your mail new password"
            return render(request, 'Reset_password.html', {'msg_success': msg_success})
        else:
            msg_error = "This email does not exist  "
            return render(request, 'Reset_password.html', {'msg_error': msg_error})

    return render(request, 'Reset_password.html')


# **********Registration**********

def Registration(request):
    Trainer = designation.objects.get(designation="Trainer")
    Trainee = designation.objects.get(designation="Trainee")
    if request.method == 'POST':
        if user_registration.objects.filter(email=request.POST['email']).exists():
            msg_error = "Email id already exists"
            return render(request, 'Registration.html', {'msg_error': msg_error})
        else:
            acc = user_registration()
            acc.fullname = request.POST['name']
            acc.dateofbirth = request.POST['dateofbirth']
            acc.gender = request.POST['gender']
            acc.email = request.POST['email']
            acc.password = random.randint(10000, 99999)
            acc.mobile = request.POST['mobile']
            acc.alternativeno = request.POST['alt_no']
            acc.pincode = request.POST['pincode']
            acc.district = request.POST['district']
            acc.idproof = request.FILES['id_proof']
            acc.photo = request.FILES['pic']
            acc.state = request.POST['state']
            acc.native_place = request.POST['native_place']
            acc.permanentaddress1 = request.POST['address1']
            acc.permanentaddress2 = request.POST['address2']
            acc.permanentaddress3 = request.POST['address3']
            acc.height = request.POST['height']
            acc.weight = request.POST['weight']
            acc.batch_id = request.POST['batch']
            acc.joiningdate = datetime.now()
            acc.reg_end_date = datetime.now() + timedelta(days=90)
            acc.status = "active"
            acc.designation_id = Trainee.id
            acc.save()
            subject = 'Welcome Gym'
            message = 'Congratulations,\n' \
                'You have successfully registered with our website.\n' \
                'username :'+str(acc.email)+'\n' 'password :'+str(acc.password) + \
                '\n' 'WELCOME '
            recepient = str(acc.email)
            send_mail(subject, message, EMAIL_HOST_USER,
                      [recepient], fail_silently=False)
            msg_success = "Registration successfully Check Your Registered Mail"
            return render(request, 'Registration.html', {'msg_success': msg_success})
    else:
        batchs = batch.objects.all()
        return render(request, 'Registration.html', {'batchs': batchs})

# ******************************Super Admin******************************

# ------------------------------Amal------------------------------


def SuperAdmin_Accountsett(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':

            newPassword = request.POST.get('newPassword')
            confirmPassword = request.POST.get('confirmPassword')

            user = User.objects.get(is_superuser=True)
            if newPassword == confirmPassword:
                user.set_password(newPassword)
                user.save()
                msg_success = "Password has been changed successfully"
                return render(request, 'SuperAdmin_Accountsett.html', {'msg_success': msg_success})
            else:
                msg_error = "Password does not match"
                return render(request, 'SuperAdmin_Accountsett.html', {'msg_error': msg_error})
        return render(request, 'SuperAdmin_Accountsett.html', {'users': users})
    else:
        return redirect('/')


def SuperAdmin_logout(request):
    request.session.flush()
    return redirect("/")

# ------------------------------Ananadhu------------------------------


def SuperAdmin_index(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request, 'SuperAdmin_index.html', {'users': users})
    else:
        return redirect('/')


def SuperAdmin_Dashboard(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='Trainer')
        des1 = designation.objects.get(designation='Trainee')
        Trainer_count = user_registration.objects.filter(
            designation_id=des).count()
        Trainee_count = user_registration.objects.filter(
            designation_id=des1).count()
        machine_count = Machine.objects.count()
        return render(request, 'SuperAdmin_Dashboard.html', {'machine_count': machine_count, 'users': users, 'Trainee_count': Trainee_count, 'Trainer_count': Trainer_count, 'des': des})
    else:
        return redirect('/')


def SuperAdmin_Total_Instructors_Table(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='Trainer')
        Trainer = user_registration.objects.filter(designation_id=des).filter(
            status='active' or 'Active').all().order_by('-id')
        return render(request, 'SuperAdmin_Total_Instructors_Table.html', {'users': users, 'Trainer': Trainer, 'des': des})
    else:
        return redirect('/')


def SuperAdmin_TotalTraineesUPhysicalTrainer_Table(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='Trainee')
        Trainee = user_registration.objects.filter(designation=des).filter(
            Trainer_id=id).filter(status='active' or 'Active').order_by('-id')
        return render(request, 'SuperAdmin_TotalTraineesUPhysicalTrainer_Table.html', {'users': users, 'Trainee': Trainee, 'des': des, 'id': id})
    else:
        return redirect('/')


def SuperAdmin_TraineeProfile(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        Trainee = user_registration.objects.get(id=id)
        return render(request, 'SuperAdmin_TraineeProfile.html', {'users': users, 'Trainee': Trainee, 'id': id})
    else:
        return redirect('/')


def SuperAdmin_Batch_Cards(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request, 'SuperAdmin_Batch_Cards.html', {'users': users})
    else:
        return redirect('/')


def SuperAdmin_AddBatch(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        Batch = batch.objects.all()
        return render(request, 'SuperAdmin_AddBatch.html', {'users': users, 'Batch': Batch})
    else:
        return redirect('/')


def SuperAdmin_AddBatchsave(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            a = batch()
            a.batch = request.POST['batch']
            a.fromtime = request.POST['fromtime']
            a.totime = request.POST['totime']
            Bach = a.batch
        if batch.objects.filter(batch=Bach).exists():
            msg_error = "Batch already exist"
            return render(request, 'SuperAdmin_AddBatch.html', {'users': users, 'msg_error': msg_error})
        else:
            a.save()
            msg_success = "Batch added successfully"
        return render(request, 'SuperAdmin_AddBatch.html', {'users': users, 'msg_success': msg_success})
    else:
        return redirect('/')


def SuperAdmin_UpdateBatch(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        var = batch.objects.filter(id=id)
        var1 = batch.objects.get(id=id)
        Batch = batch.objects.all()
        return render(request, 'SuperAdmin_UpdateBatch.html', {'users': users, 'Batch': Batch, 'var': var, 'var1': var1})

    else:
        return redirect('/')


def SuperAdmin_UpdateBatchsave(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            a = batch.objects.get(id=id)
            a.batch = request.POST.get('batch')
            a.fromtime = request.POST.get('fromtime')
            a.totime = request.POST.get('totime')
            a.save()
            msg_success = "Batch updated successfully"
            Batch = batch.objects.all()
        return render(request, 'SuperAdmin_UpdateBatch.html', {'msg_success': msg_success, 'users': users, 'Batch': Batch})
    else:
        return redirect('/')


def SuperAdmin_ViewBatch(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        Batch = batch.objects.all()
        return render(request, 'SuperAdmin_ViewBatch.html', {'users': users, 'Batch': Batch})
    else:
        return redirect('/')


def SuperAdmin_BatchDelete(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
            users = User.objects.filter(id=SAdm_id)
        else:
            return redirect('/')
        m = batch.objects.get(id=id)
        m.delete()
        msg_success = "Batch deleted successfully"
        return render(request, 'SuperAdmin_Batch_Cards.html', {'msg_success': msg_success, 'users': users})
    else:
        return redirect('/')

# ------------------------------Praveen------------------------------


def SuperAdmin_trainees(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        desig = designation.objects.get(designation='Trainee')
        Atraineenum = user_registration.objects.filter(
            designation=desig).filter(status='active').count()
        Ptraineenum = user_registration.objects.filter(
            designation=desig).filter(status='resign').count()
        return render(request, 'SuperAdmin_trainees.html', {'Atraineenum': Atraineenum, 'Ptraineenum': Ptraineenum, 'users': users})
    else:
        return redirect('/')


def SuperAdmin_ActiveTrainees(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        desig = designation.objects.get(designation='Trainee')
        trainee = user_registration.objects.filter(
            designation=desig).filter(status='active').order_by('-id')
        return render(request, 'SuperAdmin_ActiveTrainees.html', {'trainee': trainee, 'users': users})
    else:
        return redirect('/')


def SuperAdmin_PassiveTrainees(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        desig = designation.objects.get(designation='Trainee')
        trainee = user_registration.objects.filter(
            designation=desig).filter(status='resign').order_by('-id')
        return render(request, 'SuperAdmin_PassiveTrainees.html', {'trainee': trainee, 'users': users})
    else:
        return redirect('/')


def SuperAdmin_ActiveTraineeProfile(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        trainee = user_registration.objects.get(id=id)
        return render(request, 'SuperAdmin_ActiveTrainerProfile.html', {'trainee': trainee, 'users': users})
    else:
        return redirect('/')


def SuperAdmin_PassiveTraineeProfile(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        trainee = user_registration.objects.get(id=id)
        return render(request, 'SuperAdmin_PassiveTrainerProfile.html', {'trainee': trainee, 'users': users})
    else:
        return redirect('/')


def SuperAdmin_Machines(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        machines = Machine.objects.all()
        return render(request, 'SuperAdmin_Machines.html', {'machines': machines, 'users': users})
    else:
        return redirect('/')


def SuperAdmin_machine_category(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        machine_type = Category.objects.filter(cate_type=id)
        machine_name = Machine.objects.filter(id=id)
        return render(request, 'SuperAdmin_machine_category.html', {'machine_type': machine_type, 'machine_name': machine_name, 'users': users})
    else:
        return redirect('/')

# ------------------------------Nimisha------------------------------


def SuperAdmin_Expense(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request, 'SuperAdmin_Expense.html', {'users': users})
    else:
        return redirect('/')


def SuperAdmin_ExpenseView(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        var = expense.objects.all().order_by('-id')
        return render(request, 'SuperAdmin_ExpenseView.html', {'users': users, 'var': var})
    else:
        return redirect('/')


def SuperAdmin_NewTransaction(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        mem = expense()
        if request.method == 'POST':
            mem.payee = request.POST['payee']
            mem.paymethod = request.POST['paymod']
            mem.paydate = request.POST['paydt']
            mem.category = request.POST['category']
            mem.description = request.POST['description']
            mem.amount = request.POST['amount']
            mem.tax = request.POST['tax']
            mem.total = request.POST['total']
            mem.save()
            msg_success = "Expenses added successfully"
            return render(request, 'SuperAdmin_NewTransaction.html', {'msg_success': msg_success})
        else:
            return render(request, 'SuperAdmin_NewTransaction.html')
    else:
        return redirect('/')


def SuperAdmin_ExpenseViewEdit(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        var = expense.objects.filter(id=id)
        return render(request, 'SuperAdmin_ExpenseViewEdit.html', {'users': users, 'var': var})
    else:
        return redirect('/')


def SuperAdmin_ExpenseViewEdit_Update(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            abc = expense.objects.get(id=id)
            abc.payee = request.POST.get('pay')
            abc.paymethod = request.POST.get('paymod')
            abc.paydate = request.POST.get('paydt')
            abc.category = request.POST.get('category')
            abc.description = request.POST.get('description')
            abc.amount = request.POST.get('amount')
            abc.tax = request.POST.get('tax')
            abc.total = request.POST.get('total')
            abc.save
            print(abc)
            msg_success = "Expenses updated successfully"
            return render(request, 'SuperAdmin_ExpenseViewEdit.html', {'msg_success': msg_success})
        else:
            return render(request, 'SuperAdmin_ExpenseViewEdit.html')
    else:
        return redirect('/')


def SuperAdmin_FindExpense(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request, 'SuperAdmin_FindExpense.html', {'users': users, })
    else:
        return redirect('/')


def SuperAdmin_FindExpense_Show(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == "POST":
            fromdate = request.POST.get('startdate')
            todate = request.POST.get('enddate')
            mem = expense.objects.filter(paydate__range=[fromdate, todate])
            return render(request, 'SuperAdmin_FindExpenseView.html', {'users': users, 'mem': mem})
    else:
        return redirect('/')


def SuperAdmin_FindExpenseView(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        var = expense.objects.all().order_by('-id')
        return render(request, 'SuperAdmin_FindExpenseView.html', {'users': users, 'var': var})
    else:
        return redirect('/')


def SuperAdmin_FindExpenseViewEdit(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        var = expense.objects.filter(id=id)
        return render(request, 'SuperAdmin_FindExpenseViewEdit.html', {'users': users, 'var': var})
    else:
        return redirect('/')


def SuperAdmin_FindExpenseNewTransaction(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        mem = expense()
        if request.method == 'POST':
            mem.payee = request.POST['pay']
            mem.paymethod = request.POST['paymod']
            mem.paydate = request.POST['paydt']
            mem.category = request.POST['category']
            mem.description = request.POST['description']
            mem.amount = request.POST['amount']
            mem.tax = request.POST['tax']
            mem.total = request.POST['total']
            mem.save()
            msg_success = "Transaction added successfully"
            return render(request, 'SuperAdmin_FindExpenseNewTransaction.html', {'msg_success': msg_success})
        else:
            return render(request, 'SuperAdmin_FindExpenseNewTransaction.html')
    else:
        return redirect('/')


def SuperAdmin_FindExpenseViewEdit_Update(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            s1 = expense.objects.get(id=id)
            s1.payee = request.POST.get('payee')
            s1.paymethod = request.POST.get('paymod')
            s1.paydate = request.POST.get('paydt')
            s1.category = request.POST.get('category')
            s1.description = request.POST.get('description')
            s1.amount = request.POST.get('amount')
            s1.tax = request.POST.get('tax')
            s1.total = request.POST.get('total')
            s1.save
            msg_success = "Transaction updated successfully"
            return render(request, 'SuperAdmin_FindExpenseViewEdit.html', {'msg_success': msg_success})
        else:
            return render(request, 'SuperAdmin_FindExpenseViewEdit.html')
    else:
        return redirect('/')

# ------------------------------Anwar------------------------------


def SuperAdmin_RegistrationDetails(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
    trainee = designation.objects.get(designation='Trainee')
    count1 = user_registration.objects.filter(
        designation=trainee).filter(status='active', select_status=1).count()
    count2 = user_registration.objects.filter(
        designation=trainee).filter(status='resign').count()
    return render(request, 'SuperAdmin_RegistrationDetails.html', {'users': users, 'count1': count1, 'count2': count2})


def SuperAdmin_Activereg(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        trainee = designation.objects.get(designation="Trainee")
        trainer = designation.objects.get(designation="Trainer")
        user = user_registration.objects.filter(
            designation=trainee).filter(status='active', select_status=1).order_by("-id")
        user2 = user_registration.objects.filter(
            designation=trainer).filter(status='active', select_status=1)
        return render(request, 'SuperAdmin_Activereg.html', {'users': users, 'user_registration': user, 'user_registration2': user2})
    else:
        return redirect('/')


def SuperAdmin_newreg(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        trainee = designation.objects.get(designation="Trainee")
        trainer = designation.objects.get(designation="Trainer")
        user = user_registration.objects.filter(
            status='active', select_status=0)
        return render(request, 'SuperAdmin_newreg.html', {'users': users, 'user_registration': user})
    else:
        return redirect('/')


def Dates(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == "POST":
            dt = user_registration.objects.get(id=id)
            dt.startdate = request.POST['sdate']
            dt.enddate = request.POST['edate']
            dt.save()
            return redirect('SuperAdmin_Activereg')
    else:
        return redirect('/')


def Active_traineesave(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        trainer = user_registration.objects.get(id=id)
        if request.method == 'POST':
            trainer.Trainer_id = request.POST.get('ptrainer')
            trainer.status = request.POST.get('tstatus')
            trainer.admission_rate = request.POST.get('admission_rate')
            trainer.fees_rate = request.POST.get('fees_rate')
            trainer.save()
        return redirect('SuperAdmin_Activereg')
    else:
        return redirect('/')


def addtopt(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        user = user_registration.objects.get(id=id)
        trainer = designation.objects.get(designation='Trainer')
        user.designation = trainer
        user.save()
        return redirect('SuperAdmin_Activereg')
    else:
        return redirect('/')


def addtotr(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        user = user_registration.objects.get(id=id)
        trainee = designation.objects.get(designation='Trainee')
        user.designation_id = trainee.id
        user.save()
        return redirect('SuperAdmin_active_trainers')
    else:
        return redirect('/')


def SuperAdmin_Updatereg(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        user = user_registration.objects.get(id=id)
        return render(request, 'SuperAdmin_Updatereg.html', {'users': users, 'user_registration': user})
    else:
        return redirect('/')


def Active_traineeupdate(request, id):
    if request.method == "POST":
        tr = user_registration.objects.get(id=id)
        tr.fullname = request.POST['trname']
        tr.email = request.POST['tremail']
        tr.mobile = request.POST['trmobile']
        tr.dateofbirth = request.POST['trdob']
        tr.joiningdate = request.POST['joiningdate']
        tr.height = request.POST['trheight']
        tr.weight = request.POST['trweight']
        tr.permanentaddress1 = request.POST['trad1']
        tr.permanentaddress2 = request.POST['trad2']
        tr.permanentaddress3 = request.POST['trad3']
        trr = user_registration.objects.get(id=id)
        try:
            trr.photo = request.FILES['trphoto']
            trr.save()
        except:
            tr.save()
        return redirect('SuperAdmin_Activereg')


def Active_traineedelete(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        user = user_registration.objects.get(id=id)
        user.delete()
        msg_success = "Deleted successfully"
        return render(request, 'SuperAdmin_Activereg.html', {'users': users, 'msg_success': msg_success})
    else:
        return redirect('/')


def Active_traineeaccept(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        user = user_registration.objects.get(id=id)
        user.select_status = 1
        user.select_status = 1
        user.save()
        msg_success = "Accept successfully"
        return render(request, 'SuperAdmin_newreg.html', {'users': users, 'msg_success': msg_success})
    else:
        return redirect('/')


def SuperAdmin_Passivereg(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        trainee = designation.objects.get(designation='trainee')
        user = user_registration.objects.filter(
            designation=trainee).filter(status="resign" or "Resign")
        return render(request, 'SuperAdmin_Passivereg.html', {'users': users, 'user_registration': user})
    else:
        return redirect('/')


def SuperAdmin_PassiveUpdate(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        user = user_registration.objects.get(id=id)
        return render(request, 'SuperAdmin_PassiveUpdate.html', {'users': users, 'user_registration': user})
    else:
        return redirect('/')


def Passive_traineeupdate(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == "POST":
            tr = user_registration.objects.get(id=id)
            tr.fullname = request.POST['trname']
            tr.email = request.POST['tremail']
            tr.mobile = request.POST['trmobile']
            tr.dateofbirth = request.POST['trdob']
            tr.joiningdate = request.POST['joiningdate']
            tr.height = request.POST['trheight']
            tr.weight = request.POST['trweight']
            tr.permanentaddress1 = request.POST['trad1']
            tr.permanentaddress1 = request.POST['trad2']
            tr.permanentaddress1 = request.POST['trad3']
            trr = user_registration.objects.get(id=id)
            try:
                if request.FILES.get('trphoto') is not None:
                    os.remove(trr.photo.path)
                    trr.photo = request.FILES.get('trphoto')
                trr.save()
                msg_success = "Updated successfully"
            except:
                tr.save()
                msg_success = "Updated successfully"
            return render(request, 'SuperAdmin_Passivereg.html', {'users': users, 'msg_success': msg_success})
    else:
        return redirect('/')


def PassiveDates(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == "POST":
            dt = user_registration.objects.get(id=id)
            # dt.startdate = request.POST['sdate']
            # dt.enddate = request.POST['edate']
            
            dt.joiningdate = datetime.now()  
            dt.reg_end_date = datetime.now()  + timedelta(days=90)
            dt.net_due_date = datetime.now()  + timedelta(days=30)
            dt.status = "active"
            dt.save()
            return redirect('SuperAdmin_Passivereg')
    else:
        return redirect('/')

# ------------------------------Akhil------------------------------


def SuperAdmin_physical_trainer_card(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='Trainer')
        count = user_registration.objects.filter(
            designation=des).filter(status='active').count()
        count2 = user_registration.objects.filter(
            designation=des).filter(status='resign').count()
        return render(request, 'SuperAdmin_physical_trainer_card.html', {'users': users, 'count': count, 'count2': count2})
    else:
        return redirect('/')


def SuperAdmin_active_trainers(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='Trainer')
        trainer = user_registration.objects.filter(
            designation_id=des).filter(status='active').order_by('-id')
        return render(request, 'SuperAdmin_active_trainers.html', {'users': users, 'trainer': trainer})
    else:
        return redirect('/')


def Active_trainersave(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        trainer = user_registration.objects.get(id=id)
        if request.method == 'POST':
            trainer.rate = request.POST.get('trate')
            trainer.status = request.POST.get('tstatus')
            trainer.save()
            msg_success = "saved successfully"
            return render(request, 'SuperAdmin_active_trainers.html', {'users': users, 'msg_success': msg_success})
        else:
            return render(request, 'SuperAdmin_active_trainers.html', {'users': users})
    return render(request, 'SuperAdmin_active_trainers.html', {'users': users})


def SuperAdmin_activetrainer_update(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        trainer = user_registration.objects.get(id=id)
        return render(request, 'SuperAdmin_activetrainer_update.html', {'users': users, 'trainer': trainer})
    else:
        return redirect('/')


def SuperAdmin_activetrainer_update_save(request, id):
    trainer = user_registration.objects.get(id=id)
    if request.method == 'POST':
        trainer.fullname = request.POST.get('name')
        trainer.email = request.POST.get('em')
        trainer.mobile = request.POST.get('phno')
        trainer.dateofbirth = request.POST.get('dob')
        trainer.joiningdate = request.POST.get('ag')
        trainer.height = request.POST.get('ht')
        trainer.weight = request.POST.get('wt')
        trainer.permanentaddress1 = request.POST.get('ad1')
        trainer.permanentaddress2 = request.POST.get('ad2')
        trainer.permanentaddress3 = request.POST.get('ad3')
        try:
            if request.FILES.get('pic') is not None:
                os.remove(trainer.photo.path)
                trainer.photo = request.FILES.get('pic')
        except:
            pass
        trainer.save()
        msg_success = "updated changed successfully"
        return render(request, 'SuperAdmin_activetrainer_update.html', {'msg_success': msg_success, 'trainer': trainer})
    else:
        return render(request, 'SuperAdmin_activetrainer_update.html')


def SuperAdmin_resigned_trainers(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='Trainer')
        trainer = user_registration.objects.filter(
            designation_id=des).filter(status='resign').order_by('-id')
        return render(request, 'SuperAdmin_resigned_trainers.html', {'users': users, 'trainer': trainer})
    else:
        return redirect('/')


def SuperAdmin_resignedtrainer_update(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        trainer = user_registration.objects.get(id=id)
        return render(request, 'SuperAdmin_resignedtrainer_update.html', {'users': users, 'trainer': trainer})
    else:
        return redirect('/')


def SuperAdmin_resignedtrainer_update_save(request, id):
    trainer = user_registration.objects.get(id=id)
    if request.method == 'POST':
        trainer.fullname = request.POST.get('name')
        trainer.email = request.POST.get('em')
        trainer.mobile = request.POST.get('phno')
        trainer.dateofbirth = request.POST.get('dob')
        trainer.age = request.POST.get('ag')
        trainer.height = request.POST.get('ht')
        trainer.weight = request.POST.get('wt')
        trainer.address1 = request.POST.get('ad1')
        trainer.address2 = request.POST.get('ad2')
        trainer.address3 = request.POST.get('ad3')
        try:
            if request.FILES.get('pic') is not None:
                os.remove(trainer.photo.path)
                trainer.photo = request.FILES.get('pic')

        except:
            pass
        trainer.save()
        msg_success = "updated changed successfully"
        return render(request, 'SuperAdmin_resignedtrainer_update.html', {'msg_success': msg_success, 'trainer': trainer})


def SuperAdmin_resignedtrainer_renew(request, id):
    trainer = user_registration.objects.get(id=id)
    if request.method == 'POST':
        trainer.status = "active"
        trainer.save()
        msg_success = "renewed successfully"
        return redirect('SuperAdmin_resigned_trainers')
    return render(request, 'SuperAdmin_resigned_trainers.html', {'msg_success': msg_success, 'trainer': trainer})


# def User_payment_save(request):
#     if 'SAdm_id' in request.session:
#         if request.session.has_key('SAdm_id'):
#             SAdm_id = request.session['SAdm_id']
#         else:
#             return redirect('/')
#         users = User.objects.filter(id=SAdm_id)
#         if request.method == "POST":
#             pay = payment()
#             pay.bank = request.POST.get('bankname')
#             pay.accountnumber = request.POST.get('accnumber')
#             pay.ifse = request.POST.get('ifsecode')
#             pay.payment = request.POST.get('amount')
#             pay.user_id = Tne_id
#             pay.date = datetime.now()
#             pay.save()
#             msg_success = "Payment added successfully"
#         return render(request, 'User_payment_history.html', {'users': users, 'msg_success': msg_success})
#     else:
#         return redirect('/')

# ------------------------------Subeesh------------------------------


def SuperAdmin_pay_det(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='Trainee')
        count = user_registration.objects.filter(
            designation_id=des).filter(status='active').count()
        count2 = user_registration.objects.filter(
            designation_id=des).filter(status='resign').count()
        return render(request, 'SuperAdmin_pay_det.html', {'users': users, 'count': count, 'count2': count2})
    else:
        return redirect('/')


def SuperAdmin_current_trainees(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='Trainee')

        ct = user_registration.objects.filter(
            designation_id=des, status='active').values().order_by('-id')

        # for i in ct:
        #     i['pay'] = payment.objects.filter(
        #         user_id=i['id']).latest('date').date
        #     i['pay2'] = payment.objects.filter(
        #         user_id=i['id']).earliest('date').payment

        return render(request, 'SuperAdmin_current_trainees.html', {'users': users, 'ct': ct})
    else:
        return redirect('/')


def SuperAdmin_current_trainees_payment(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        ct = user_registration.objects.get(id=id)
        pay = payment.objects.filter(user_id=ct).order_by('-id')

        pay1 = payment.objects.filter(user_id=id).order_by('-id')

        if request.method == "POST":
            uid = request.POST.get('his_id')
            pay_data = payment.objects.get(id=uid)
            pay_data.status = 1
            pay_data.save()
            msg_success = "payment Verified"
            return render(request, 'SuperAdmin_current_trainees_payment.html', {'users': users, 'ct': ct, 'pay': pay, 'msg_success': msg_success})
        else:
            return render(request, 'SuperAdmin_current_trainees_payment.html', {'users': users, 'ct': ct, 'pay': pay})
    else:
        return redirect('/')


def SuperAdmin_current_trainees_payment_add(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)

        time = datetime.now()
        desi = designation.objects.get(designation='Trainee')
        sps = user_registration.objects.filter(
            designation_id=desi).filter(status='Active') .all()
        mem1 = user_registration.objects.get(id=id)
        return render(request, 'SuperAdmin_current_trainees_payment_add.html', {'mem1': mem1, 'time': time, 'users': users, 'desi': desi, 'sps': sps})
    else:
        return redirect('/')


def SuperAdmin_current_trainees_payment_adding(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        mems = user_registration.objects.get(id=id)
        if request.method == "POST":
            mem1 = user_registration.objects.get(id=id)
            pay = payment()
            pay.payment = request.POST.get('amount')
            pay.date = datetime.now()
            pay.payment_type = request.POST.get('payment_type')
            pay.date = request.POST.get('payment_date')
            pay.net_due_date = datetime.strptime(
                pay.date, '%Y-%m-%d').date() + timedelta(days=30)
            pay.user = mem1
            pay.status = 1
            mems.reg_end_date = datetime.strptime(
                pay.date, '%Y-%m-%d').date() + timedelta(days=90)
            mems.net_due_date = datetime.strptime(
                pay.date, '%Y-%m-%d').date() + timedelta(days=30)
            mems.save()
            pay.save()
            msg_success = "payment added successfully"
            return render(request, 'SuperAdmin_current_trainees.html', {'users': users, 'msg_success': msg_success})
    else:
        return redirect('/')


def SuperAdmin_current_trainees_payment_verify(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        mem2 = payment.objects.get(id=id)
        mem2.status = 1
        ct = user_registration.objects.get(id=mem2.user_id)
        ct.reg_end_date = mem2.date + timedelta(days=90)
        ct.net_due_date = mem2.date + timedelta(days=30)
        mem2.save()
        ct.save()
        msg_success = "payment Verified successfully"
        return render(request, 'SuperAdmin_current_trainees_payment.html', {'users': users, 'msg_success': msg_success, 'ct': ct})
    else:
        return redirect('/')


def SuperAdmin_current_trainees_payment_update(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        mem2 = payment.objects.get(id=id)

        return render(request, 'SuperAdmin_current_trainees_payment_update.html', {'users': users, 'mem2': mem2})
    else:
        return redirect('/')


def SuperAdmin_current_trainees_payment_edit(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == "POST":
            payed = payment.objects.get(id=id)
            payed.payment = request.POST.get('amount')
            payed.payment_type = request.POST.get('payment_type')
            payed.date = request.POST.get('payment_date')
            payed.net_due_date = datetime.strptime(
                payed.date, '%Y-%m-%d').date() + timedelta(days=30)
            ct = user_registration.objects.get(id=payed.user_id)
            ct.reg_end_date = datetime.strptime(
                payed.date, '%Y-%m-%d').date() + timedelta(days=90)
            ct.net_due_date = datetime.strptime(
                payed.date, '%Y-%m-%d').date() + timedelta(days=30)
            payed.save()
            ct.save()
            msg_successupdate = "payment updated successfully"
            return render(request, 'SuperAdmin_current_trainees.html', {'users': users, 'msg_successupdate': msg_successupdate})
    else:
        return redirect('/')


def SuperAdmin_current_trainees_payment_delete(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        payed = payment.objects.get(id=id)
        payed.delete()
        msg_successdelete = "payment deleted successfully"
        return render(request, 'SuperAdmin_current_trainees.html', {'users': users, 'msg_successdelete': msg_successdelete})
    else:
        return redirect('/')


def SuperAdmin_previous_trainees_payment(request):

    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='Trainee')
        aps = user_registration.objects.filter(
            designation_id=des, status='resign').values().order_by('-id')

        for i in aps:
            i['pay'] = payment.objects.filter(
                user_id=i['id']).latest('date').date
            i['pay2'] = payment.objects.filter(
                user_id=i['id']).earliest('date').payment
        pay = payment.objects.all()
        return render(request, 'SuperAdmin_previous_trainees_payment.html', {'users': users, 'aps': aps, 'pay': pay})
    else:
        return redirect('/')
# ------------------------------Sanjay------------------------------


def SuperAdmin_Machine_card(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request, 'SuperAdmin_Machine_card.html', {'users': users})
    else:
        return redirect('/')


def SuperAdmin_Machine_addcategory(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            n = request.POST['c_name']
            d = request.POST['c_details']

            de = request.POST['desc']
            image = request.FILES.get('file')

            addcategory = Machine(machine_name=n,
                                  machine_details=d,
                                  machine_image=image,
                                  machine_description=de)

            addcategory.save()
            msg_success = "Data Added successfully"
            return render(request, 'SuperAdmin_Machine_addcategory.html', {'users': users, 'msg_success': msg_success})

        return render(request, 'SuperAdmin_Machine_addcategory.html')
    else:
        return redirect('/')


def SuperAdmin_Machine_viewcategory(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        cat = Machine.objects.all()
        data = {'cat': cat, 'users': users}

        return render(request, 'SuperAdmin_Machine_viewcategory.html', data)
    else:
        return redirect('/')


def SuperAdmin_Machine_viewmachines(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        cat = Machine.objects.all()
        data = {'cat': cat, 'users': users}
        return render(request, 'SuperAdmin_Machine_viewmachines.html', data)
    else:
        return redirect('/')


def SuperAdmin_Machine_chestpressmachine(request, i_id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)

        cat = Machine.objects.filter(id=i_id)
        data = {'cat': cat, 'users': users}
        return render(request, 'SuperAdmin_Machine_chestpressmachine.html', data)
    else:
        return redirect('/')


def SuperAdmin_add_machine(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            sel1 = request.POST['sel']
            category1 = Machine.objects.get(id=sel1)
            cd = request.POST['cat_det']
            name = request.POST['cat_name']
            image = request.FILES.get('file')
            des = request.POST['descr']

            std = Category(cate_type=category1,
                           cate_details=cd,
                           cate_name=name,
                           cate_image=image,
                           cate_description=des)
            std.save()
            msg_success = "Data Added successfully"
            return render(request, 'SuperAdmin_Machine_form.html', {'users': users, 'msg_success': msg_success})

        return redirect('SuperAdmin_Machine_form')
    else:
        return redirect('/')


def SuperAdmin_category1(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        catg = Machine.objects.all()
        context = {'catg': catg, 'users': users}
        return render(request, 'SuperAdmin_Machine_form.html', context)
    else:
        return redirect('/')


def SuperAdmin_Machine_form(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')

        return redirect('SuperAdmin_category1')
    else:
        return redirect('/')


def SuperAdmin_Machine_bicepsview(request, i_id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        cat = Machine.objects.filter(id=i_id)
        data = {'cat': cat, 'users': users}
        return render(request, 'SuperAdmin_Machine_bicepsview.html', data)
    else:
        return redirect('/')

# ------------------------------Unnikrishnan------------------------------


def superadmin_workout(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request, 'superadmin_workout.html', {'users': users})
    else:
        return redirect('/')


def superadmin_viewworkout(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        workouts = workout.objects.all()
        return render(request, 'superadmin_viewworkout.html', {'users': users, 'workouts': workouts})
    else:
        return redirect('/')


def superadmin_tutorialpage(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return redirect('workout1')
    else:
        return redirect('/')


def superadmin_addtutorial(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            sel1 = request.POST['sel']
            workout1 = workout.objects.get(id=sel1)
            vid = request.FILES.get('file')
            addtutorial = tutorial(Workout=workout1,
                                   video=vid)
            addtutorial.save()
            msg_success = "Tutorial added successfully"
            return render(request, 'superadmin_addtutorial.html', {'users': users, 'msg_success': msg_success})
        return redirect('superadmin_tutorialpage')
    else:
        return redirect('/')


def workout1(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        workouts = workout.objects.all()
        context = {'workouts': workouts, 'users': users}
        return render(request, 'superadmin_addtutorial.html', context)
    else:
        return redirect('/')


def superadmin_addworkout(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            w_name = request.POST['workout_name']
            desc = request.POST['description']
            img = request.FILES.get('file')
            addworkout = workout(workout_name=w_name,
                                 description=desc,
                                 image=img)
            addworkout.save()
            msg_success = "Workout added successfully"
            return render(request, 'superadmin_addworkout.html', {'users': users, 'msg_success': msg_success})
        return render(request, 'superadmin_addworkout.html')
    else:
        return redirect('/')


def superadmin_ChestDetailView(request, i_id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        wrk = workout.objects.filter(id=i_id)
        vdo = tutorial.objects.filter(Workout_id=i_id)
        return render(request, 'superadmin_ChestDetailView.html', {'users': users, 'wrk': wrk, 'vdo': vdo})
    else:
        return redirect('/')


def deletevideo(request, i_id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        std = tutorial.objects.get(id=i_id)
        try:
            std.delete()
            msg_success = "Video deleted successfully"
            workouts = workout.objects.all()
            return render(request, 'superadmin_viewworkout.html', {'users': users, 'workouts': workouts, 'msg_success': msg_success})
        except:
            return render(request, 'superadmin_viewworkout.html')
    else:
        return redirect('/')

# ------------------------------Nidhun------------------------------


def SuperAdmin_achievement_card(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request, "SuperAdmin_achievement_card.html", {'users': users})
    else:
        return redirect('/')


def SuperAdmin_achievements_add_achievements(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        msg_success = ''
        if request.method == 'POST':
            Achievement_title = request.POST.get('Achievement_title')
            Achievement_description = request.POST.get(
                'Achievement_description')
            Achievement_image = request.FILES['Achievement_image']
            achievement = Achievement(Achievement_title=Achievement_title,
                                      Achievement_description=Achievement_description, Achievement_image=Achievement_image)
            achievement.save()
            msg_success = "Achievement Added"
            return render(request, "SuperAdmin_achievements_add_achievements.html", {'users': users, 'msg_success': msg_success})
    else:
        return redirect('/')


def SuperAdmin_achievements_view_achievements(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        qs = Achievement.objects.all()
        return render(request, "SuperAdmin_achievements_view_achievements.html", {'users': users, 'qs': qs})
    else:
        return redirect('/')


def SuperAdmin_achievements_achievement_1(request, i_id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        chievement = Achievement.objects.filter(id=i_id)
        return render(request, "SuperAdmin_achievements_achievement_1.html", {'users': users, 'Achievement': chievement})
    else:
        return redirect('/')

# ******************************Trainer******************************

# ------------------------------Nidhun------------------------------


def Trainer_index(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        return render(request, 'Trainer_index.html', {'mem': mem})
    else:
        return redirect('/')


def Trainer_dashboard(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        return render(request, 'Trainer_dashboard.html', {'mem': mem})
    else:
        return redirect('/')

# ------------------------------Amal------------------------------


def Trainer_Trainees_card(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        Traine = designation.objects.get(designation='Trainee')
        Act_count = user_registration.objects.filter(designation=Traine).filter(
            status="active").filter(Trainer_id=Tnr_id).count()
        Res_count = user_registration.objects.filter(
            Trainer_id=Tnr_id).filter(status="resign").count()
        return render(request, 'Trainer_Trainees_card.html', {'mem': mem, 'Act_count': Act_count, 'Res_count': Res_count})
    else:
        return redirect('/')


def Trainer_Current_Trainees_table(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        des = designation.objects.get(designation="Trainee")
        traine = user_registration.objects.filter(designation_id=des.id).filter(
            Trainer_id=Tnr_id).filter(status="active").order_by("-id")
        return render(request, 'Trainer_Current_Trainees_table.html', {'mem': mem, 'traine': traine})
    else:
        return redirect('/')


def Trainer_Current_Trainees_profile(request, id):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        nam = user_registration.objects.filter(id=id)
        return render(request, 'Trainer_Current_Trainee_profile.html', {'mem': mem, 'nam': nam})
    else:
        return redirect('/')


def Trainer_Previous_Trainees_table(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        traine = user_registration.objects.filter(
            Trainer_id=Tnr_id).filter(status="resign").order_by("-id")
        return render(request, 'Trainer_Previous_Trainees_table.html', {'mem': mem, 'traine': traine})
    else:
        return redirect('/')


def Trainer_Previous_Trainees_profile(request, id):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        nam = user_registration.objects.filter(id=id)
        return render(request, 'Trainer_Previous_Trainee_profile.html', {'mem': mem, 'nam': nam})
    else:
        return redirect('/')


def Trainer_Accsetting(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=Tnr_id)
            abc.fullname = request.POST.get('name')
            abc.dateofbirth = request.POST.get('dateofbirth')
            abc.gender = request.POST.get('gender')
            abc.email = request.POST.get('email')
            abc.permanentaddress1 = request.POST.get('address1')
            abc.permanentaddress2 = request.POST.get('address2')
            abc.permanentaddress3 = request.POST.get('address3')
            abc.native_place = request.POST.get('native_place')
            abc.pincode = request.POST.get('pincode')
            abc.district = request.POST.get('district')
            abc.state = request.POST.get('state')
            abc.mobile = request.POST.get('mobile')
            abc.alternativeno = request.POST.get('alt_no')
            if request.FILES.get('id_proof') is not None:
                old_img = user_registration.objects.get(id=Tnr_id)
                os.remove(old_img.idproof.path)
                abc.idproof = request.FILES.get('id_proof')
            abc.height = request.POST.get('height')
            abc.weight = request.POST.get('weight')
            abc.save()
            msg_success = "Data changed successfully"
            return render(request, 'Trainer_Accsetting.html', {'msg_success': msg_success})
        return render(request, 'Trainer_Accsetting.html', {'mem': mem})
    else:
        return redirect('/')


def Trainer_Profile_Imagechange(request, id):
    if request.method == 'POST':
        ab = user_registration.objects.get(id=id)
        ab.photo = request.FILES['files']
        ab.save()
        msg_success = "Profile Picture changed successfully"
        return render(request, 'Trainer_Accsetting.html', {'msg_success': msg_success})


def Trainer_Changepwd(request, id):
    if request.method == 'POST':
        ac = user_registration.objects.get(id=id)
        oldps = request.POST['currentPassword']
        newps = request.POST['newPassword']
        cmps = request.POST.get('confirmPassword')
        if oldps != newps:
            if newps == cmps:
                ac.password = request.POST.get('confirmPassword')
                ac.save()
                msg_success = "Password changed successfully"
                return render(request, 'Trainer_Accsetting.html', {'msg_success': msg_success})

        elif oldps == newps:
            messages.add_message(request, messages.INFO,
                                 'Current and New password same')
        else:
            messages.info(request, 'Incorrect password same')

        return redirect('Trainer_Accsetting')

# ------------------------------Anwar------------------------------


def Trainer_Payment_history(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        pay = payment.objects.filter(user_id=Tnr_id).order_by('-id')
        return render(request, 'Trainer_Payment_history.html', {'mem': mem, 'pay': pay})
    else:
        return redirect('/')

# ------------------------------Meenu------------------------------


def Trainer_workout_images(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=Tnr_id)
        a1 = workout.objects.all()
        return render(request, 'Trainer_workout_images.html', {'mem': mem, 'a1': a1})


def Trainer_workoutvideos1(request, id):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=Tnr_id)
        data = tutorial.objects.filter(Workout_id=id)
        return render(request, 'Trainer_workoutvideos1.html', {'mem': mem, 'data': data})

# ******************************Trainee******************************

# ------------------------------Amal------------------------------


def Trainee_index(request):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        return render(request, 'Trainee_index.html', {'mem1': mem1})
    else:
        return redirect('/')


def Trainee_Accsetting(request):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        if request.method == 'POST':
            abb = user_registration.objects.get(id=Tne_id)
            abb.fullname = request.POST.get('name')
            abb.dateofbirth = request.POST.get('dateofbirth')
            abb.gender = request.POST.get('gender')
            abb.email = request.POST.get('email')
            abb.permanentaddress1 = request.POST.get('address1')
            abb.permanentaddress2 = request.POST.get('address2')
            abb.permanentaddress3 = request.POST.get('address3')
            abb.native_place = request.POST.get('native_place')
            abb.pincode = request.POST.get('pincode')
            abb.district = request.POST.get('district')
            abb.state = request.POST.get('state')
            abb.mobile = request.POST.get('mobile')
            abb.alternativeno = request.POST.get('alt_no')
            if request.FILES.get('id_proof') is not None:
                old_img = user_registration.objects.get(id=Tne_id)
                os.remove(old_img.idproof.path)
                abb.idproof = request.FILES.get('id_proof')
            abb.height = request.POST.get('height')
            abb.weight = request.POST.get('weight')
            abb.save()
            msg_success = "Data updated successfully"
            return render(request, 'Trainee_Accsetting.html', {'msg_success': msg_success})
        else:

            return render(request, 'Trainee_Accsetting.html', {'mem1': mem1})
    else:
        return redirect('/')


def Trainee_Profile_Imagechange(request, id):
    if request.method == 'POST':
        ab = user_registration.objects.get(id=id)
        if request.FILES.get('files') is not None:
            os.remove(ab.photo.path)
            ab.photo = request.FILES.get('files')
            ab.save()
        msg_success = "Profile Picture changed successfully"
        return render(request, 'Trainer_Accsetting.html', {'msg_success': msg_success})


def Trainee_Changepwd(request, id):
    if request.method == 'POST':
        ac = user_registration.objects.get(id=id)
        oldps = request.POST['currentPassword']
        newps = request.POST['newPassword']
        cmps = request.POST.get('confirmPassword')
        if oldps != newps:
            if newps == cmps:
                ac.password = request.POST.get('confirmPassword')
                ac.save()
                msg_success = "Password changed successfully"
                return render(request, 'Trainer_Accsetting.html', {'msg_success': msg_success})
        elif oldps == newps:
            messages.add_message(request, messages.INFO,
                                 'Current and New password same')
        else:
            messages.info(request, 'Incorrect password same')

        return redirect('Trainee_Accsetting')


def Trainee_logout(request):
    if 'Tne_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')


def Trainer_logout(request):
    if 'Tnr_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

# ------------------------------unnikrishnan------------------------------


def Trainee_Dashboard(request):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        return render(request, 'Trainee_Dashboard.html', {'mem1': mem1})
    else:
        return redirect('/')


def Trainee_index(request):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        return render(request, 'Trainee_index.html', {'mem1': mem1})
    else:
        return redirect('/')

# ------------------------------Akhil------------------------------


def Trainee_payment_history(request):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        pay = payment.objects.filter(user_id=Tne_id).order_by('-id')
        return render(request, 'Trainee_payment_history.html', {'mem1': mem1, 'pay': pay})
    else:
        return redirect('/')


def Trainee_payment_save(request):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        if request.method == "POST":
            pay = payment()
            pay.payment = request.POST.get('amount')
            pay.user_id = Tne_id
            pay.date = request.POST.get('payment_date')
            pay.payment_type = request.POST.get('payment_type')
            pay.net_due_date = datetime.strptime(
                pay.date, '%Y-%m-%d').date() + timedelta(days=30)
            pay.save()
            msg_success = "Payment added successfully"
            return render(request, 'Trainee_payment_history.html', {'mem1': mem1, 'msg_success': msg_success})
        else:
            return render(request, 'Trainee_payment_history.html', {'mem1': mem1})

# ------------------------------meenu------------------------------


def Trainee_workout_images(request):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        a = workout.objects.all()
        return render(request, 'Trainee_workout_images.html', {'mem1': mem1, 'a': a})
    else:
        return redirect('/')


def Trainee_workoutvideos1(request, id):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        new = workout.objects.all()
        data = tutorial.objects.filter(Workout_id=id)
        return render(request, 'Trainee_workoutvideos1.html', {'mem1': mem1, 'new': new, 'data': data})
    else:
        return redirect('/')
