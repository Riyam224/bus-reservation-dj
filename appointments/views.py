from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request , 'index.html' , {})


def appointments(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        country = request.POST['country']
        schaduale = request.POST['schaduale']
        yourtime = request.POST['yourtime']
        message = request.POST['message']


        return render(request , 'appointments.html',
         {  'name': name,
            'phone': phone,
            'email': email, 
            'country': country,
            'schaduale': schaduale,
            'yourtime':yourtime,
            'message': message})

    return render(request , 'index.html', {})