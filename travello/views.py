from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dests = Destination.objects.all()

    # dest1 = Destination()
    # dest1.name= 'Dhaka'
    # dest1.desc= 'Its Sleeping time'
    # dest1.price = 700
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = False
    
    # dest2 = Destination()
    # dest2.name= 'Chittagong'
    # dest2.desc= 'Heelo Frans'
    # dest2.price = 600
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = True
    
    # dest3 = Destination()
    # dest3.name= 'Rajshahi'
    # dest3.desc= 'Ghumaya Thak'
    # dest3.price = 500
    # dest3.img = 'destination_3.jpg'
    # dest3.offer = False

    # dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests': dests})