"""phoenix URL Configuration

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
from django.urls import include, path

from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from apps.authen.views import login_view,twofa_view
from apps.phoenix.views import dashboard_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    
    path('', login_view,name='main'),
    path('login/', login_view,name='login'),
    path('2fa/', twofa_view,name='2fa'),
    
    path('phoenix/dashboard/',dashboard_view,name='dashboard'),

    
    path('phoenix/', TemplateView.as_view(template_name='phoenix.base.html'),
         name='phoenix'),
    



    # Login and Logout

    # path('login/', auth_views.LoginView.as_view(
    #     redirect_authenticated_user=True,
    #     template_name='registrations/login.html'
    # ),
    #     name='login'
    # ),


    # path('logout/', auth_views.LogoutView.as_view(
    #     next_page='login'
    # ),
    #     name='logout'
    # ),
]
