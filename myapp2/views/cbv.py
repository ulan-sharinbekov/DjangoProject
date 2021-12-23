from django.views import View
from django.shortcuts import render, redirect

from myapp2.forms import addClubForm, addFootballerForm


class Club(View):

    def get(self, request):
        form = addClubForm()
        return render(request, 'addClub.html', {'form': form})

    def post(self, request):
        form = addClubForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                form.save()
                return redirect('add_page')
            except:
                form.add_error(None, "Ошибка добавления")
        return render(request, 'addClub.html', {'form': form})


class Footballer(View):

    def get(self, request):
        form =addFootballerForm()
        return render(request, 'addFootballer.html', {'form': form})

    def post(self, request):
        form = addFootballerForm()
        print(form)
        if form.is_valid():
            try:
                form.save()
                print('saved')
            except:
                form.add_error(None, "Ошибка добавления")
                print('error')
        return render(request, 'addFootballer.html', {'form': form})
