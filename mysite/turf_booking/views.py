from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import NewUser, NewTurf, NewSlot, LogUser, LogTurf
from .models import Turf, Slot, Bookie
from datetime import datetime, date

# Create your views here.


def create_turf(request):
    form = NewTurf(request.POST, request.FILES)

    if request.method == "POST":
        form = NewTurf(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(login_turf)
    context = {
        'form': form,
    }
    return render(request, 'turf_booking/index.html', context)


def login_turf(request):
    form = LogTurf()
    check = False
    if request.method == "POST":
        form = LogTurf(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            try:
                turf = Turf.objects.get(name=name)
                if turf.password == password:
                    pk = turf.pk
                return redirect('turf_detail', pk)
            except Exception:
                check = True
                print("User absent")
    context = {
        'form': form,
        'check': check,
    }
    return render(request, 'turf_booking/login_turf.html', context)


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
    check = False
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
                check = True
                print("User absent")
    context = {
        'form': form,
        'check': check,
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
        if slot.date < date.today():
            slot.delete()
    form = NewSlot()
    check = False
    if request.method == "POST":
        form = NewSlot(request.POST)
        if form.is_valid():
            time = form.cleaned_data['timing']
            for slot in slot_list:
                td = datetime.combine(slot.date, slot.timing) - datetime.combine(slot.date, time)
                et = divmod(td.total_seconds(), 60)
                print(et)
                if abs(et[0]) < 60:
                    check = True
            if check:
                context = {
                    'slot_list': slot_list,
                    'turf_id': tpk,
                    'user_id': upk,
                    'form': form,
                    'check': check,
                }
                print('Slot Booked')
                return render(request, 'turf_booking/slot.html', context)
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
        'check': check,
    }
    return render(request, 'turf_booking/slot.html', context)


def turf_detail(request, pk):
    try:
        turf = Turf.objects.get(id=pk)
        slot_list = turf.slot_set.all()
        context = {
            'slot_list': slot_list,
            'turf': turf,
        }
        return render(request, 'turf_booking/turf_detail.html', context)
    except Exception:
        print("Non Found")
    context = {
        'slot_list': [],
    }
    return render(request, 'turf_booking/turf_detail.html', context)


def home(request):
    return render(request, 'turf_booking/home.html')
