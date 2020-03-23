from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import NewUser, NewTurf, NewSlot, LogUser
from .models import Turf, Slot, Bookie
import datetime

# Create your views here.


def create_turf(request):
    form = NewTurf()

    if request.method == "POST":
        form = NewTurf(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'turf_booking/index.html', context)


def create_slot(request, pk):
    turf = Turf.objects.get(id=pk)
    slot_list = turf.slot_set.all()
    for slot in slot_list:
        if slot.book_timing.date() != datetime.date.today():
            slot.delete()
    form = NewSlot()
    if request.method == "POST":
        form = NewSlot(request.POST)
        if form.is_valid():
            time = form.cleaned_data['timing']
            check = False
            for slot in slot_list:
                if slot.timing == time:
                    check = True
            if check:
                HttpResponse("Slot Already Booked")
            else:
                slot = form.save()
                turf.slot_set.add(slot)
        return redirect('set_slot', pk)
    context = {
        'slot_list': slot_list,
        'turf_id': pk,
        'form': form,
    }
    return render(request, 'turf_booking/slot.html', context)


def create_user(request):
    form = NewUser()
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            pk = Bookie.objects.get(name=name).pk
        return redirect('listings', pk)
    context = {
        'form': form,
    }
    return render(request, 'turf_booking/user.html', context)


def user_login(request):
    form = LogUser()
    if request.method == "POST":
        form = LogUser(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            try:
                user = Bookie.objects.get(name=name)
                if user.password == password:
                    pk = user.pk
                return redirect('listings', pk)
            except Exception:
                print("User absent")
    context = {
        'form': form,
    }
    return render(request, 'turf_booking/user.html', context)


def listings(request, pk):
    context = {
        'turf_list': Turf.objects.all(),
        'upk': str(pk),
        'user': Bookie.objects.get(pk=pk)
    }
    return render(request, 'turf_booking/listings.html', context)


def new_slot(request, upk, tpk):
    user = Bookie.objects.get(pk=upk)
    turf = Turf.objects.get(pk=tpk)
    slot_list = turf.slot_set.all()
    for slot in slot_list:
        if slot.book_timing.date() != datetime.date.today():
            slot.delete()
    form = NewSlot()
    if request.method == "POST":
        form = NewSlot(request.POST)
        if form.is_valid():
            time = form.cleaned_data['timing']
            check = False
            for slot in slot_list:
                if slot.timing == time:
                    check = True
            if check:
                HttpResponse("Slot Already Booked")
            else:
                slot = form.save()
                turf.slot_set.add(slot)
                user.slot_set.add(slot)

        return redirect('new_slot', upk, tpk)
    context = {
        'slot_list': slot_list,
        'turf_id': tpk,
        'user_id': upk,
        'form': form,
    }
    return render(request, 'turf_booking/slot.html', context)



def home(request):
    return render(request, 'turf_booking/home.html')