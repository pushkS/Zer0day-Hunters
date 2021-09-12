from django.shortcuts import redirect, render, HttpResponse
from home.models import Contact
from django.core.mail import send_mail
from home.models import Index, Career, About, Training
from django.contrib import messages


def thankyou(request):
    return render(request,'thankyou.html')


def base(request):
        return render(request,'base.html')


# Create your views here.
def index(request):
    ind = Index.objects.all()
    context = {'ind':ind}
    return render(request,'index.html', context)


def about(request):
    ab = About.objects.all()
    context = {'ab': ab}
    return render(request,'about.html', context)


def career(request):
    carr = Career.objects.all()
    context = {'carr':carr}
    return render(request,'career.html', context)


def training(request):
    tra = Training.objects.all()
    context = {'tra':tra}
    return render(request,'training.html', context)


def WhatsappData(sub):
    import time 
    import webbrowser as web
    import pyautogui as pg
    # print("Im here")
    web.open_new_tab('https://web.whatsapp.com/send?phone=917666794499'+'&text='+sub)
    time.sleep(30)
    pg.press('enter')
    # return redirect('https://web.whatsapp.com/send?phone=917666794499'+'&text='+sub)

def contact(request):
    import webbrowser as web
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        sub = "Name: " + name + "\n" + "Email: " + email + "\n\n\n" + "Message: " + message

        print(sub )
        # url = 'https://web.whatsapp.com/send?phone=917666794499'+'&text='+sub
        # web.open(url)
        # return redirect(url)
        WhatsappData(sub)
        

        # #send mail
        messages.success(request, "Thank You" )
        # send_mail(
        #    subject,#suject 
        #    sub,#msg
        #    email, #from 
        #    ['zer0dayhunters@gmail.com'], #to zer0dayhunters@gmail.com

        # )


        print(sub )
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        
    return render(request,'contact.html')