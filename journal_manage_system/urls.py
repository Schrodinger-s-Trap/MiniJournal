from django.urls import path

from journal_manage_system import views

urlpatterns = [
    path('add_catalog', views.add_catalogs),
    path('show_catalog', views.show_catalogs),
]

