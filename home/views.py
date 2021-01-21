from django.shortcuts import render
from bigstore import settings

# Email Part
from django.core.mail import send_mail
from django.template.loader import render_to_string
import email.message
import smtplib

# Message
from django.contrib import messages

# Model
from home.models import Home,Staples,Snacks,Fruits_Vegetables,Breakfast_Cereal
from other.models import Offer, special_offer


def home(request):
    hst = Staples.objects.all()
    hsn = Snacks.objects.all()
    fv = Fruits_Vegetables.objects.all()
    bkf = Breakfast_Cereal.objects.all()
    offers = special_offer.objects.all()
    print("you'r Email", request.session.get('email'))
    return render(request, 'home/index.html', {"BASE_URL": settings.BASE_URL,
                'offers': offers,'hst':hst,'hsn':hsn,'fv':fv,'bkf':bkf})


def about(request):
    return render(request, 'home/about.html', {"BASE_URL": settings.BASE_URL})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email_user = request.POST['email']
        msg = request.POST['msg']

        data_content = {"yourname": name,
                        'user_email': email_user, 'msg': msg}
        email_content = render_to_string('home/mail.html', data_content)

        mess = email.message.Message()
        mess['Subject'] = 'Welcome to BIG-Store'
        mess['From'] = settings.EMAIL_HOST_USER
        mess['To'] = 'shubhamupadhyay1014@gmail.com'
        password = settings.EMAIL_HOST_PASSWORD
        mess.add_header('Content-Type', 'text/html')
        mess.set_payload(email_content)
        s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
        s.starttls()
        s.login(mess['From'], password)
        s.sendmail(mess['From'], [mess['To']], mess.as_string())
        messages.info(
            request, 'Thankyou for contact us, we will reply you shortly')
    return render(request, 'home/contact.html', {"BASE_URL": settings.BASE_URL})
