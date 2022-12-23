"""qabd_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from users import urls as users_urls # Import sub url path from users/urls.py file
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), #Step4 for auth token and step5 you have run cmd: python manage.py makemigrations and python manage.py migrate
    path("users/", include(users_urls)), # All Users related link will be used http://127.0.0.1:8000/users/ this link and sub path will be come from users/urls.py file
]

