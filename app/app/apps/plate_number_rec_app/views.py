import shutil

from django.contrib.auth import login, authenticate

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import CarPlateNumber
from .forms import CarPlateNumberForm

from .brains.run import recognise_plate


def success(request):
    return HttpResponse('successfully uploaded')


def clear(request):
    import os
    import glob

    files = glob.glob('media/images/')
    for f in files:
        shutil.rmtree(f)

    return redirect('/')


def main(request):
    if request.method == 'POST':
        form = CarPlateNumberForm(request.POST, request.FILES)

        if form.is_valid():

            cd = form.cleaned_data

            car = CarPlateNumber(car_plate_img=cd['car_plate_img'])

            # recognise_plate('app/media/images/' + car.name)

            car.name = car.car_plate_img.name
            car.save()

            return render(request, 'plate_number_rec_app/result.html', {'img': 'media/images/' + car.name,
                                                                             'name': car.name})
    else:
        form = CarPlateNumberForm()

    return render(request, 'plate_number_rec_app/main.html', {'form': form})
