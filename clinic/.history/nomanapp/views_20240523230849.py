from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request, 'about.html',{} )

def doctors(request):
    return render(request, 'doctors.html',{} )

def blog(request):
    return render(request, 'blog.html',{} )

def services(request):
    return render(request, 'services.html',{} )

def blogsingle(request):
    return render(request, 'blog-single.html',{} )

def contact(request):
    if request.method == "POST":
           # Process the data in form.cleaned_data
            message_name = request.POST.get('message-name', '')

            message_email = request.POST.get('message-email', '')

            message_subject = request.POST.get('message_subject','')
            umessage = request.POST.get('umessage','')
            
            send_mail(
                message_subject,
                umessage,
                message_email,
                ['ankitchoudhary2451@gmail.com']
            )
            
            return render(request,'contact.html',{'message_name': message_name})
    else:   
        return render(request,'contact.html',{})