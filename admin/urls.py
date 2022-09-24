"""admin URL Configuration

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
from django.urls import include,path

from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),
    
      path("__reload__/", include("django_browser_reload.urls")),

    path('', TemplateView.as_view(template_name='registrations/login.html'),
         name='main'
         ),
    path('twostep/', TemplateView.as_view(template_name='components/twostep.html'),
         name='twostep'
         ),
    
    path('phoenix/', TemplateView.as_view(template_name='phoenix.base.html'),
         name='phoenixv2'),
    

    path('phoenix/index/', TemplateView.as_view(template_name='components/index.html'),
         name='index'
         ),

    # Login and Logout

    path('login/', auth_views.LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='registrations/login.html'
    ),
        name='login'
    ),


    # path('logout/', auth_views.LogoutView.as_view(
    #     next_page='login'
    # ),
    #     name='logout'
    # ),
]
