from django.contrib import admin
from django.urls import path, include
from home import views


#admin log-in customization

admin.site.site_header = "Zer0Day-Hunter"
admin.site.site_title = "Welcome to Zer0Day-Hunter Dashboard"
admin.site.index_title = "Welcome to my ZeroDay"
urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('about', views.about, name='about'),
    path('career', views.career, name='career'),
    path('training', views.training, name='training'),
    path('contact', views.contact, name='contact'),
]