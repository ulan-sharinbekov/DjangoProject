from django.urls import path
from myapp2.views.views import addClub, addFootballer, get_Club, get_Footballer, get_name, get_Contact

#from myapp2.views.views import Clu
from .views.cbv import Club, Footballer

urlpatterns = [

    path('cbv/club', Club.as_view(), name='add_page'),
    path('create/club', addClub, name='add_page'),
    path('cbv/Footballer', Footballer.as_view(), name='add_page'),
    path('create/Footballer', addFootballer, name='add_page'),

    path('club', get_Club),
    path('footbal', get_Footballer),
    path('newForm', get_name),
    path('contact',get_Contact),



]