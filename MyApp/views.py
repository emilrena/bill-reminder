import datetime
import os
from django.core.mail import send_mail
from django.conf import settings

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from MyApp.models import *
from bill_reminder_application import settings

try:
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 8000))
    print('Starting development server at: http://' + s.getsockname()[0] + ':8000')
except:
    pass
# Create your views here.

def login(request):
    username=request.POST['username']
    password=request.POST['password']
    if Login.objects.filter(Username=username,Password=password).exists():
        obj=Login.objects.get(Username=username,Password=password)
        if obj.Type=="admin":
            return JsonResponse({'status': 'ok', 'TYPE':'admin','id':obj.id})
        elif obj.Type=='USER':
            return JsonResponse({'status': 'ok', 'TYPE':'user','id':obj.id})
        else:
            return JsonResponse({'status': 'not ok'})
    else: return JsonResponse({'status': 'not ok'})


def forgotpassword(request):
    forgotpassword=request.POST['FORGOT_PASSWORD']

def category(request):
    category=request.POST['CATEGORY']
    cat = Category()
    cat.categoryname = category
    cat.save()


    return JsonResponse({'status':'ok'})

def categoryview(request):
    search=request.POST['search']
    uk = Category.objects.filter(categoryname__icontains=search)
    l = []
    for i in uk:
        l.append({'id': i.id, 'categoryname': i.categoryname })
    return JsonResponse({'status':'ok','data':l})

def viewcomplaint(request):
    up = Complaint.objects.all().order_by('-Date')
    l = []
    for i in up:
        l.append({'id':i.id,'name':i.USER.name,'Date':i.Date,'complaint':i.complaint,'statuss':i.Status ,'reply':i.Reply})
    print(l)
    return JsonResponse({'status':'ok','data':l})

def sendreply(request):
    reply=request.POST['reply']
    cid=request.POST['cid']
    v=Complaint.objects.filter(id=cid).update(Reply=reply,Status='Replied')

    return JsonResponse({'status':'ok'})




def AddSubCategory(request):
    subcategory=request.POST['subcategory']
    cid=request.POST['cid']
    lid=request.POST['lid']
    lobj=Login.objects.get(id=lid)
    uid=User.objects.get(LOGIN=lobj)
    import datetime
    date=datetime.datetime.now().date()
    v=Subcategory()
    v.subcategoryname=subcategory
    v.Date=date
    v.CATEGORY_id=cid
    v.USER_id=uid.id
    v.save()
    return JsonResponse({'status':'ok'})

def changepassword(request):
    lid = request.POST['lid']
    CurrentPassword=request.POST['CurrentPassword']
    NewPassword=request.POST['NewPassword']
    conformpassword=request.POST['conform password']
    print(CurrentPassword, lid)
    if Login.objects.filter(id=lid, Password=CurrentPassword).exists():
        obj = Login.objects.filter(id=lid, Password=CurrentPassword).update(Password=NewPassword)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'not ok'})

def editcategory(request):
    edit =request.POST['edit']
    cid=request.POST['cid']
    print(cid)
    s=Category.objects.filter(id=cid).update(categoryname=edit)

    return JsonResponse({'status':'ok'})

def editsubcategory(request):
    category =request.POST['edit']
    cid=request.POST['cid']
    s=Subcategory.objects.filter(id=cid).update(Subcategory=category)

    return JsonResponse({'status':'ok'})

def deletecategory(request):
    cid=request.POST['cid']
    s=Category.objects.filter(id=cid).delete()

    return JsonResponse({'status':'ok'})

def deletesubcategory(request):
    cid=request.POST['cid']
    s=Subcategory.objects.filter(id=cid).delete()

    return JsonResponse({'status':'ok'})


def registerduserview(request):
    us = User.objects.all()
    l = []
    for i in us:
        l.append({'id':i.id,})
    print(len(l))
    return JsonResponse({'status':'ok', 'data':l,'len':len(us)})

def viewfeedback(request):
    ur = feedback.objects.all().order_by('-Date')
    l = []
    for i in ur:
        l.append({'id':i.id, 'name':i.USER.name,'Date':i.Date,'feedback':i.feedback,'rating':i.Rating})

    return JsonResponse({'status':'ok','data':l})




def registor(request):
    name = request.POST['Name']
    password = request.POST['Password']
    conformPassword = request.POST['conformpassword']
    place = request.POST['place']
    house = request.POST['house']
    district = request.POST['district']
    state = request.POST['state']
    pin = request.POST['pin']
    email = request.POST['email']
    phone = request.POST['phone']
    gender = request.POST['gender']

    log = Login()
    log.Username=email
    log.Password=conformPassword
    log.Type="USER"
    log.save()



    REG = User()
    REG.name=name
    REG.place=place
    REG. house=house
    REG.state=state
    REG.pin=pin
    REG.email=email
    REG.phone=phone
    REG.gender=gender
    REG.LOGIN=log
    REG.save()

    return JsonResponse({'status': 'ok'})


def edit_profile(request):
    lid = request.POST['lid']

    name = request.POST['Name']
    place = request.POST['place']
    house = request.POST['house']
    state = request.POST['state']
    pin = request.POST['pin']
    email = request.POST['email']
    phone = request.POST['phone']
    gender = request.POST['gender']

    REG = User.objects.get(LOGIN_id=lid)
    REG.name=name
    REG.place=place
    REG. house=house
    REG.state=state
    REG.pin=pin
    REG.email=email
    REG.phone=phone
    REG.gender=gender

    REG.save()

    return JsonResponse({'status': 'ok'})

def reminderset(request):
    Title = request.POST['Title']
    lid = request.POST['lid']
    Description = request.POST['Describtion']
    date = request.POST['Date']
    time = request.POST['Time']
    # type = request.POST['Type']
    FrontPhoto = request.POST['Photo_Front']
    BackPhoto = request.POST['Photo_Back']
    Category = request.POST['category']

    import datetime, base64
    f = base64.b64decode(FrontPhoto)
    b = base64.b64decode(BackPhoto)
    dt1= datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
    dt2= datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
    rem = Reminder()
    fp = os.path.join(settings.BASE_DIR, 'media\\user\\front_photo')
    bp = os.path.join(settings.BASE_DIR, 'media\\user\\back_photo')
    open(fp+'\\'+dt1,'wb').write(f)
    open(bp+'\\'+dt2,'wb').write(b)
    rem.Title=Title
    rem.SUBCATEGORY_id=Category
    rem.Date=date
    rem.Time=time
    rem.description=Description
    rem.fphoto='/media/user/front_photo/'+dt1
    rem.bphoto='/media/user/back_photo/'+dt2
    rem.Type='None'
    rem.status='pending'
    rem.amount=0
    rem.USER=User.objects.get(LOGIN_id=lid)
    rem.save()
    return JsonResponse({'status':'ok'})

def ViewHistory(request):
    lid = request.POST['lid']
    import datetime
    # uf = Reminder.objects.filter(Date__lte=datetime.date.today(), USER__LOGIN_id=lid)
    uf = Reminder.objects.filter(USER__LOGIN_id=lid).order_by('-Date')
    l = []
    for i in uf:
        l.append({'id': i.id, 'name': i.USER.name,'stat':i.status,'category':i.SUBCATEGORY.CATEGORY.categoryname, 'subcategory':i.SUBCATEGORY.subcategoryname,'Date': i.Date,'time': i.Time, 'Title': i.Title, 'description': i.description,'fphoto':i.fphoto,'bphoto':i.bphoto})

    return JsonResponse({'status':'ok','data':l})

def viewComplaints(requset):
    lid = requset.POST['lid']
    um = Complaint.objects.filter(USER__LOGIN_id=lid).order_by('-Date')
    l = []
    for i in um:
        l.append({'id': i.id, 'Status': i.Status, 'Date': i.Date, 'complaints': i.complaint, 'Reply': i.Reply})

    return JsonResponse({'status':'ok','data':l})



def viewSubcategory(requset):
    cid = requset.POST['cid']
    lid = requset.POST['lid']
    _searchText = requset.POST['_searchText']
    umm = Subcategory.objects.filter(CATEGORY_id=cid, USER__LOGIN_id=lid, subcategoryname__icontains=_searchText)
    l = []
    for i in umm:
        l.append({'id': i.id, 'date': i.Date, 'subcategory': i.subcategoryname, })
    return JsonResponse({'status':'ok','data':l})



def viewSubcategorySel(requset):
    cid = requset.POST['cid']
    lid = requset.POST['lid']
    _searchText = requset.POST['_searchText']
    umm = Subcategory.objects.filter(CATEGORY_id=cid, USER__LOGIN_id=lid)
    l = []
    for i in umm:
        l.append({'id': i.id, 'date': i.Date, 'subcategory': i.subcategoryname, })
    return JsonResponse({'status':'ok','data':l})

def updaterem(requset):
    rid = requset.POST['rid']
    print(rid)
    Reminder.objects.filter(id=rid).update(status='updated')
    return JsonResponse({'status':'ok'})





def SendComplaints(request):
    complaint = request.POST['complaint']
    from datetime import datetime
    sndcmplt = Complaint()
    sndcmplt.complaint=complaint
    sndcmplt.Date=datetime.now().date()
    sndcmplt.Reply='Pending'
    sndcmplt.Status='Pending'
    sndcmplt.USER=User.objects.get(LOGIN_id=request.POST["lid"])
    sndcmplt.save()

    return JsonResponse({'status':'ok'})

def SendFeedback(request):
    feedbacks = request.POST['Send_Feedback']
    Rating = request.POST['RATING']

    sndfeedback = feedback()
    sndfeedback.feedback = feedbacks
    sndfeedback.Rating = Rating
    from datetime import datetime
    sndfeedback.Date=datetime.now().strftime('%Y-%m-%d')
    lid=request.POST['lid']
    sndfeedback.USER=User.objects.get(LOGIN_id=lid)

    sndfeedback.save()

    return JsonResponse({'status':'ok'})





def profile(request):
    lid = request.POST['lid']
    us = User.objects.get(LOGIN_id=lid)
    l=({'name':us.name,'house':us.house,'place':us.place,'state': us.state,'pin':us.pin,'gender':us.gender,'email':us.email,'phone':us.phone,})
    return JsonResponse({'status': 'ok', 'data': l})


def viewNotification(requset):
    lid = requset.POST['lid']
    dt=datetime.date.today()
    uno = Reminder.objects.filter(USER__LOGIN_id=lid)
    l = []
    v=dt.day-3
    g=datetime.datetime.now().strftime("%Y-%m")+'-'+str(v)
    for i in uno:
        if Reminder.objects.filter(id=i.id, Date__gte=str(g),status='pending').exists():
            if Reminder.objects.get(id=i.id, Date__gte=str(g),status='pending'):
                l.append({'id': i.id,  'Date': i.Date, 'Time': i.Time,'title':i.Title})
                if Notification.objects.filter(REMINDER=i).exists():
                    Notification.objects.filter(REMINDER=i).delete()
                # else:
                    VNOT = Notification()
                    VNOT.Date=dt
                    VNOT.REMINDER=i
                    VNOT.Time=datetime.datetime.now().strftime("%H:%M")
                    VNOT.save()
                else:
                    VNOT = Notification()
                    VNOT.Date=dt
                    VNOT.REMINDER=i
                    VNOT.Time=datetime.datetime.now().strftime("%H:%M")
                    VNOT.save()

    uno = Notification.objects.filter(REMINDER__USER__LOGIN_id=lid).order_by('-id')
    J = []
    for i in uno:
        J.append({'id': i.id, 'nid': i.id,  'Date': i.Date, 'Time': i.Time,'title':i.REMINDER.Title,'message':i.REMINDER.Title})
    if J!= []:
        J=J[0]
        print(J)
        return JsonResponse({'status':'ok','message':J['message'], 'nid':str(J['nid'])})
    return JsonResponse({'status': 'no'})

#
# def viewNotification(requset):
#     lid = requset.POST['lid']
#     uno = Notification.objects.filter(REMINDER__USER__LOGIN_id=lid)
#     l = []
#     for i in uno:
#         l.append({'id': i.id,  'Date': i.Date, 'Time': i.Time,'title':i.REMINDER.Title})
#
#     return JsonResponse({'status':'ok','data':l})
#
#


def forgot_pass_post(request):
    em = request.POST['email']
    import random
    password = random.randint(0000,9999)
    log=Login.objects.filter(Username=em)
    if log.exists():
        logg = Login.objects.get(Username=em)
        message = 'temporary password is ' + str(password)
        send_mail(
            'temp password',
            message,
            settings.EMAIL_HOST_USER,
            [em, ],
            fail_silently=False
        )
        logg.Password=password
        logg.save()


        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'no'})

##################user




