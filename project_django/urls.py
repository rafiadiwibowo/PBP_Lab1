"""project_django URL Configuration

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
from django.urls import path, include
from wishlist.views import wishlist_xml
from wishlist.views import wishlist_json
from wishlist.views import show_json_by_id
from wishlist.views import show_xml_by_id


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('xml/', wishlist_xml, name='wishlist_xml'),
    path('json/', wishlist_json, name='wishlist_json'),
    path('json/<int:id>', show_json_by_id, name='show_jason_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]
