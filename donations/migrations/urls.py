from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name='home'),
    path('donors/',views.donors, name='donors_list'),
    path('request/',views.request,name='request_list'),
    path('donate/<int:request_id>/',views.donate_blood, name='donate_blood'),
]