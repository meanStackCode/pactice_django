from django.urls import path
import views

urlpatterns = [
   path('', views.homepage, name='home'),
   path("count/", views.countpage, name='count'),
   path("about/", views.aboutpage, name='about')
]
