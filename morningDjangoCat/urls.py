"""morningDjangoCat URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indx, name='Agency-index'),
    path('about/', views.about, name='Agency-about'),
    path('agent-single/', views.agent_single, name='Agency-agent-single'),
    path('agents-grid/', views.agents_grid, name='Agency-agents-grid'),
    path('blog-grid/', views.blog_grid, name='Agency-blog-grid'),
    path('blog-single/', views.blog_single, name='Agency-blog-single'),
    path('contact/', views.contact, name='Agency-contact'),
    path('property-grid/', views.property_grid, name='Agency-property-grid'),
    path('property-single/', views.property_single, name='Agency-property-single'),
    path('register/', views.register, name='users-registration')
]
