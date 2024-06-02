from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST.get('message_name')
        message_email = request.POST.get('message_email')
        message_subject = request.POST.get('message_subject')
        umessage = request.POST.get('umessage')

        # Check if all required fields are provided
        if message_name and message_email and message_subject and umessage:
            try:
                send_mail(
                    subject=message_subject,
                    message=f"Message from {message_name} ({message_email}):\n\n{umessage}",
                    from_email=message_email,
                    recipient_list=['ankitchoudhary2451@gmail.com'],
                    fail_silently=False,
                )
                return render(request, 'contact.html', {'message_name': message_name, 'success': True})
            except Exception as e:
                return render(request, 'contact.html', {'message_name': message_name, 'error': str(e)})
        else:
            return render(request, 'contact.html', {'error': 'Please fill in all fields.'})
    else:
        return render(request, 'contact.html')
