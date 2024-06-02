from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def contact(request):
    if request.method == "POST":
           # Process the data in form.cleaned_data
            message_name = request.POST['message_name']
            message_email = request.POST['message_email']
            message_subject = request.POST['message_subject']
            umessage = request.POST['umessage']
            
            return render(request,'contact.html',{'message_name': message_name})
    else:   
        return render(request,'contact.html',{})