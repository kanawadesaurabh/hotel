from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Booking


# Create your views here.

def home(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/home.html', {'rooms': rooms})

@login_required
def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        booking = Booking(user=request.user, room=room, check_in=check_in, check_out=check_out)
        booking.save()
        room.is_available = False

        return redirect('home')
    return render(request, 'hotel/book_room.html', {'room': room})
