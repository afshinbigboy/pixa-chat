from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
from .models import Room


def user_list(request):
    return render(request, 'chat/user_list.html')


def index(request):
    if request.user.is_authenticated:
    	room_list = Room.objects.all()

    	return render(request, 'chat/index.html', {'rooms': room_list})
    else:
    	return redirect('account:sign_in')


def room_list(request):
    if request.user.is_authenticated:
    	room_list = Room.objects.all()

    	return render(request, 'chat/room_list.html', {'rooms': room_list})
    else:
    	return redirect('account:sign_in')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })