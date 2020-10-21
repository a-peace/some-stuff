from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView
from . import views
import sys
sys.path.append('..')
from accounts.views import RegisterView, guest_register_view, login_page, LoginView

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about-us/$', views.about, name='about'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^create_delivery_contract/$', views.create_delivery_contract, name='create_delivery_contract'),
    url(r'^add-calendar/$', views.add_calendar, name='add_calendar'),
    url(r'uploads/$', views.uploads, name='uploads'),
    url(r'^create/$', views.create_doc, name='create'),

    # Контракт
    url(r'^create_contract/<pk>/$', views.update_contract, name='create_contract'),
    url(r'^update_contract/<pk>/$', views.update_contract, name='update_contract'),
    url(r'^delete_contract/<pk>/$', views.delete_contract, name='delete_contract'),

    # Сроки
    url(r'^table/$', views.table, name='table'),
    url(r'^create_timing/$', views.create_timing, name='create_timing'),
    url(r'^update_timing/<kek>/$', views.update_timing, name='update_timing'),
    url(r'^delete_timing/<kek>/$', views.delete_timing, name='delete_timing'),
]
