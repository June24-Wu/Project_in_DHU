"""food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from signup_login import views as signup_login_view
from health import views as health_view
from food_check import views as food_check_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls. static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', signup_login_view.login,name='login'),
    url(r'^register/', signup_login_view.register,name='register'),
    url(r'^$',signup_login_view.index),
    url(r'^jump',signup_login_view.weight_picture,name='jump'),
    url(r'^weight/',signup_login_view.weight,name='update'),
    url(r'^height/',signup_login_view.height,name='height'),
    url(r'^waist/',signup_login_view.waist,name='waist'),
    url(r'^blood_sugar/',signup_login_view.blood_sugar,name='blood_suagar'),
    url(r'^blood_pressure/',signup_login_view.blood_pressure,name='blood_fat'),
    url(r'^health_check/',health_view.health_check,name="health_check"),
    url(r'^food_check/',signup_login_view.food_check,name='food_check'),
    url(r'^food01_check/',food_check_view.food01_check,name='f01'),
    url(r'^food02_check/',food_check_view.food02_check,name='f02'),
    url(r'^food03_check/',food_check_view.food03_check,name='f03'),
    url(r'^food04_check/',food_check_view.food04_check,name='f04'),
    url(r'^food05_check/',food_check_view.food05_check,name='f05'),
    url(r'^food06_check/',food_check_view.food06_check,name='f06'),
    url(r'^food07_check/',food_check_view.food07_check,name='f07'),
    url(r'^food08_check',food_check_view.food08_check,name='f08'),
    url(r'^food09_check',food_check_view.food09_check,name='f09'),
    url(r'^food10_check',food_check_view.food10_check,name='f10'),
    url(r'^food11_check',food_check_view.food11_check,name='f11'),
    url(r'^food12_check',food_check_view.food12_check,name='f12'),
    url(r'^food13_check',food_check_view.food13_check,name='f13'),
    url(r'^food14_check',food_check_view.food14_check,name='f14'),
    url(r'^food15_check',food_check_view.food15_check,name='f15'),
    url(r'^food16_check',food_check_view.food16_check,name='f16'),
    url(r'^food17_check',food_check_view.food17_check,name='f17'),
    url(r'^food18_check',food_check_view.food18_check,name='f18'),
    url(r'^food19_check',food_check_view.food19_check,name='f19'),
    url(r'^food20_check',food_check_view.food20_check,name='f20'),
    url(r'^food21_check',food_check_view.food21_check,name='f21'),


]+ static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
