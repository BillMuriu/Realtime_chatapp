from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.

def HomePage(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']

        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room, username=username)

        except Room.DoesNotExist:
            new_room = Room(room_name = room)
            new_room.save()
            return redirect('room', room_name=room, username=username)

    return render(request, 'index.html')

