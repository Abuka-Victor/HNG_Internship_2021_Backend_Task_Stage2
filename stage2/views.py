from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'stage2/index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        message_subject = request.POST['subject']
        message_contact = request.POST['contact']
        message_body = request.POST['message']

        send_mail(
            message_subject,
            message_body + ' from ' + message_contact,
            'chiabukz@yahoo.com',
            ['chiabukz@yahoo.com'],
        )

        return render(request, 'stage2/contact.html', {'name': name})
    else:
        return render(request, 'stage2/contact.html', {})
