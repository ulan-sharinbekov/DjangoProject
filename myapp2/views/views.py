from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from myapp2.models import Club, Footballer
import json
from myapp2.forms import addClubForm, addFootballerForm
from myapp2.testForms import NewForms, ContactForm

# Create your views here.
def addClub(request):
    if request.method == 'POST':
        form1 = addClubForm(request.POST)
        print(form1)
        if form1.is_valid():
            try:
                print(form1.cleaned_data)
                form1.save()
                return redirect('add_page')
            except:
                form1.add_error(None, "Ошибка добавления")
    else:
        form1 = addClubForm()
    return render(request, 'addClub.html', {'form': form1})


def addFootballer(request):
    if request.method == 'POST':
        form = addFootballerForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                form.save()
                return redirect('add_page')
            except:
                form.add_error(None, "Ошибка добавления")
    else:
        form = addFootballerForm()
    return render(request, 'addFootballer.html', {'form': form})


def get_Club(request):
    clubs = Club.objects.all()
    return render(request, 'club_list.html', {
        "title": "Вторая страница",
        "clubs": clubs
    })


def get_Footballer(request):
    footbal = Footballer.objects.all()
    return render(request, 'footballer_list.html', {
        "title": "Вторая страница",
        "footbal": footbal
    })

def get_name(request):
    if request.method == 'POST':
        form = NewForms(request.POST)

        if form.is_valid():
            return HttpResponse('/thanks/')

    else:
        form = NewForms()

    return render(request, 'name.html', {'form': form})


def get_Contact(request):
    if request.method == 'POST':
        print("postt")
        form = ContactForm(request.POST)

        if form.is_valid():

            return HttpResponse('/thanks/')

    else:
        print("gett")
        form = ContactForm()

    return render(request, 'name.html', {'form': form})