from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from trainingWebsites.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password # password hashing class and check class
# index page view method
from datetime import date, datetime
from trainingWebsites.models import *

def index(request):
         return render(request,'trainingTemplates/index.html')

def about(request):
         return render(request,'trainingTemplates/about.html')

def services(request):
         return render(request,'trainingTemplates/services.html')

def contact(request):
         if request.POST:
           visitorFullName = request.POST['VistorName']
           visitorMobile = request.POST['VistorMobile']
           visitorEmail = request.POST['VistorEmail']
           visitorGymType = request.POST['VisitorGymType']
           visitorMessage = request.POST['VisitorMessage']
           currentdate = date.today()
           newVisitor = Contact.objects.create(contact_fname = visitorFullName,contact_mobile = visitorMobile,contact_email = visitorEmail,contact_club = visitorGymType,contact_message = visitorMessage,contact_date = currentdate)
           newVisitor.save()
           response = redirect('/contact')
           return response
         return render(request,'trainingTemplates/contact.html')

def classes(request):
   if ClassesDay.objects.filter(NewUser_id=request.user.id).exists():
      class_object = get_object_or_404(ClassesDay,NewUser_id=request.user.id)
      trainerIdGet = class_object.Trainers_id
      trainer_object = get_object_or_404(Trainers,id=trainerIdGet)
   else:
      class_object = ''
      trainer_object = ''
   context={
      'class_object':class_object,
      'trainer_object':trainer_object
   }   
   return render(request,'trainingTemplates/classes.html',context)

def team(request):
         return render(request,'trainingTemplates/team.html')

def faq(request):
         return render(request,'trainingTemplates/faq.html')

def privacy(request):
         return render(request,'trainingTemplates/privacy.html')

def membership(request):
   if accounts.objects.filter(NewUser_id=request.user.id).exists():
      getMembership = accounts.objects.filter(NewUser_id=request.user.id).last()
   else:
      getMembership = ''
   context = {
      'getMembership':getMembership,
      'todaysdate': date.today()
   }
   return render(request,'trainingTemplates/membership.html',context)

def loginpopup(request):
         return render(request,'trainingTemplates/loginpopup.html')

def Trainees(request):
         if request.user.user_type == 'Trainer':
            CustomerDataTrainer = NewUser.objects.filter(trainer_name=request.user.first_name).exclude(is_superuser = True).exclude(user_type = 'Trainer')
            return render(request,'trainingTemplates/trainees.html',{'CustomerDataTrainer':CustomerDataTrainer})
         else:
            return render(request,'trainingTemplates/index.html')

def adminSetting(request):
         if request.user.is_superuser:
            return render(request,'trainingTemplates/adminSetting.html')
         else:
            return render(request,'trainingTemplates/index.html')

def customerList(request):
         if request.user.is_superuser:
            Customerdata = NewUser.objects.all().exclude(is_superuser = True)
            return render(request,'trainingTemplates/customerList.html',{'CustomerValue':Customerdata})
         else:
            return render(request,'trainingTemplates/index.html')

def visitorList(request):
         if request.user.is_superuser:
            Visitordata = Contact.objects.all()
            return render(request,'trainingTemplates/visitorList.html',{'VisitorValue':Visitordata})
         else:
            return render(request,'trainingTemplates/index.html')

def registerUser(request):
   if request.POST:
      firstName = request.POST['firstName']
      lastName = request.POST['lastName']
      registerEmail = request.POST['registerEmail']
      registerMob = request.POST['registerMob']
      registerPass = request.POST['registerPass']
      registerConPass = request.POST['registerConPass']
      registerUserName = request.POST['registerUserName']
      currentdate = date.today()
      if registerPass == registerConPass :
         # registerPass = make_password(registerPass)
         registerNewUser = NewUser.objects.create_user(registerEmail,registerUserName,firstName,registerMob,registerPass)
         registerNewUser.last_name = lastName
         registerNewUser.mobile = registerMob
         registerNewUser.start_date = currentdate
         # Now active the user
         registerNewUser.is_active = True
         registerNewUser.save()
         user = authenticate(username=registerEmail, password=registerPass)
         login(request,user)
         response = redirect('/index')
         return response
      else :
         response = redirect('/index')
         return response

def loginUser(request):
   if request.POST:
      loginEmail = request.POST['loginEmail']
      loginPass= request.POST['loginPass']
      # loginPass = make_password(loginPass)
      user = authenticate(username=loginEmail, password=loginPass)
      if user is not None:
          login(request,user)
          loginUserFristName = user.first_name
          response = redirect('/index')
          return response
      else:
         response = redirect('/index')
         return response

def curdOperation(request,person_type,person_id):
      if person_type == 'contactDel':
         member = Contact.objects.get(id=person_id)
         member.delete()
         response = redirect('/visitorList')
         return response
      elif person_type == 'userActivate':
         member = NewUser.objects.get(id=person_id)
         member.is_active = True
         member.save()
         response = redirect('/customerList')
         return response
      elif person_type == 'userDeactive':
         member = NewUser.objects.get(id=person_id)
         member.is_active = False
         member.save()
         response = redirect('/customerList')
         return response

      accountsValue = accounts.objects.get(id=person_id)

def UpdateOperation(request):
      if request.POST:
         visitorType = request.POST['visitorType']
         visitorId = request.POST['visitorId']
         visitorStatus = request.POST['visitorStatus']
         if visitorType == 'UpdateVisitor':
            visitorUpdate = Contact.objects.get(id=visitorId)
            visitorUpdate.contact_status = visitorStatus
            visitorUpdate.save()
            response = redirect('/visitorList')
            return response

def curdAdmin(request):
      if request.POST:
         curUpdateFormData = request.POST['curUpdateFormData']
         userId = request.POST['userId']
         userType = request.POST['userType']
         if curUpdateFormData == 'trainerData':
            remainingPayTime = request.POST['remainingPayTime']
            tamount = request.POST['tamount']
            adminUpdate = NewUser.objects.get(id=userId)
            adminUpdate.user_type = userType
            adminUpdate.save()
            accountsObject = accounts.objects.create(
               next_pay_date_trainer = remainingPayTime,
               account_tamount = tamount,
               NewUser = adminUpdate
            )
            accountsObject.save()
            trainerEntry = Trainers.objects.create(trainer_name=adminUpdate.first_name,trainer_email = adminUpdate.email,trainer_mobile = adminUpdate.mobile,
            NewUser=adminUpdate)
            trainerEntry.save()
            response = redirect('/customerList')
            return response
         elif curUpdateFormData == 'customerData':
            membershipType = request.POST['membershipType']
            camount = request.POST['camount']
            remainingTime = request.POST['remainingTime']
            trainerName = request.POST['trainerName']
            adminUpdate = NewUser.objects.get(id=userId)
            adminUpdate.user_type = userType
            adminUpdate.trainer_name = trainerName
            adminUpdate.save()
            accountsObject = accounts.objects.create(
               next_pay_date_cust = remainingTime,
               account_camount = camount,
               account_membership = membershipType,
               NewUser = adminUpdate
            )
            accountsObject.save()
            if Trainers.objects.filter(trainer_email = adminUpdate.email).exists():
               Trainers.objects.filter(trainer_email = adminUpdate.email).delete()
            response = redirect('/customerList')
            return response

def curdTrainerInsert(request):
      if request.POST:
         dayMonday = request.POST['dayMonday']
         classMonday = request.POST['classMonday']
         dayTuesday = request.POST['dayTuesday']
         classTuesday = request.POST['classTuesday']
         dayWednesday = request.POST['dayWednesday']
         classWednesday = request.POST['classWednesday']
         dayThrusday = request.POST['dayThrusday']
         classThrusday = request.POST['classThrusday']
         dayFriday = request.POST['dayFriday']
         classFriday = request.POST['classFriday']
         daySaturday = request.POST['daySaturday']
         classSaturday = request.POST['classSaturday']
         daySunday = request.POST['daySunday']
         classSunday = request.POST['classSunday']
         classMessage = request.POST['classMessage']
         trainerCustId = request.POST['trainerCustId']
         trainerId = request.POST['trainerId']
         trainerCustomerIdGet = NewUser.objects.get(id=trainerCustId)
         trainerIdGet = Trainers.objects.get(NewUser_id=trainerId)
         if ClassesDay.objects.filter(NewUser_id=trainerCustId).exists():
            ClassesDayObjectGet = ClassesDay.objects.get(NewUser_id=trainerCustId)
            ClassesDayObjectGet.ClassesDay_Mon = dayMonday
            ClassesDayObjectGet.ClassesDay_Mon_class=classMonday
            ClassesDayObjectGet.ClassesDay_Tue=dayTuesday
            ClassesDayObjectGet.ClassesDay_Tue_class=classTuesday
            ClassesDayObjectGet.ClassesDay_Wed=dayWednesday
            ClassesDayObjectGet.ClassesDay_Wed_class=classWednesday
            ClassesDayObjectGet.ClassesDay_Thru=dayThrusday
            ClassesDayObjectGet.ClassesDay_Thru_class=classThrusday
            ClassesDayObjectGet.ClassesDay_Fri=dayFriday
            ClassesDayObjectGet.ClassesDay_Fri_class=classFriday
            ClassesDayObjectGet.ClassesDay_Sat=daySaturday
            ClassesDayObjectGet.ClassesDay_Sat_class=classSaturday
            ClassesDayObjectGet.ClassesDay_Sun=daySunday
            ClassesDayObjectGet.ClassesDay_Sun_class=classSunday
            ClassesDayObjectGet.ClassMessage=classMessage
            ClassesDayObjectGet.save()
         else:    
            ClassesDayObject = ClassesDay.objects.create(
               ClassesDay_Mon = dayMonday,
               ClassesDay_Mon_class=classMonday,
               ClassesDay_Tue=dayTuesday,
               ClassesDay_Tue_class=classTuesday,
               ClassesDay_Wed=dayWednesday,
               ClassesDay_Wed_class=classWednesday,
               ClassesDay_Thru=dayThrusday,
               ClassesDay_Thru_class=classThrusday,
               ClassesDay_Fri=dayFriday,
               ClassesDay_Fri_class=classFriday,
               ClassesDay_Sat=daySaturday,
               ClassesDay_Sat_class=classSaturday,
               ClassesDay_Sun=daySunday,
               ClassesDay_Sun_class=classSunday,
               ClassMessage=classMessage,
               NewUser=trainerCustomerIdGet,
               Trainers=trainerIdGet
            )
            ClassesDayObject.save()
         response = redirect('/Trainees')
         return response
         
def logoutUser(request):
    logout(request)
    response = redirect('/index')
    return response

def adminUpdatePopup(request ,id=None):
      if NewUser.objects.filter(id=id).exists():
         instance = get_object_or_404(NewUser,id=id)
      else:
         instance = ''
      if accounts.objects.filter(NewUser_id=id).exists():
         instanceAcc = accounts.objects.filter(NewUser_id=id).last()
      else:
         instanceAcc = ''
      TrainersData = Trainers.objects.all()
      context = {
         'instance':instance,
         'instanceAcc':instanceAcc,
         'TrainersData':TrainersData
      }
      return render(request,'trainingTemplates/adminUpdatePopup.html',context)

def TrainerCurd(request, id=None):
   if NewUser.objects.filter(id=id).exists():
      instance = get_object_or_404(NewUser,id=id)
   else:
      instance = ''
   if ClassesDay.objects.filter(NewUser_id=id).exists():
      instanceClass = get_object_or_404(ClassesDay,NewUser_id=id)
   else:
      instanceClass = ''
   context = {
         'instance':instance,
         'instance':instance
      }
   return render(request,'trainingTemplates/TrainerCurd.html',context)