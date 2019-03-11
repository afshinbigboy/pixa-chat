from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contact
from itertools import chain
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


@login_required
def list(request):

    if request.method == 'POST':
        contact_username = request.POST.get('contact_username', '')
        try:
            user = User.objects.get(username=contact_username)
            if not user == request.user:
                contact = Contact(owner=request.user, user=user)
                contact.save()
                contact = Contact(user=request.user, owner=user)
                contact.save()
                messages.success(request, '@{} added to your contact list successfully'.format(contact_username))
            else:
                messages.error(request, '@{} is yourself!'.format(contact_username))
        except:
            messages.error(request, 'Ops... There is no @{} account.'.format(contact_username))



    contact_list = Contact.objects.filter(owner=request.user) | Contact.objects.filter(user=request.user)

    return render(request, 'contact/list.html', {'contacts': contact_list})