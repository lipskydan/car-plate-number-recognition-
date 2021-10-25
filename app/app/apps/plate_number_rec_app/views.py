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

            car = CarPlateNumber(car_img=cd['car_img'])

            car.name = car.car_img.name

            car.detected_plate_img = 'media/images/detected_plate_image.jpg'
            car.detected_each_char = 'media/images/detected_each_char.jpg'
            car.contour = 'media/images/contour.jpg'

            car.save()

            # path_to_image = car.name
            # print(f'path_to_image is {path_to_image}')

            result = recognise_plate('media/images/' + car.name)

            print(f'result = {result}')

            return render(request, 'plate_number_rec_app/result.html', {'car_img': 'media/images/' + car.name,
                                                                        'detected_plate_img': car.detected_plate_img,
                                                                        'contour': car.contour,
                                                                        'detected_each_char': car.detected_each_char,
                                                                        'result': result,
                                                                        'name': car.name})
    else:
        form = CarPlateNumberForm()

    return render(request, 'plate_number_rec_app/main.html', {'form': form})
