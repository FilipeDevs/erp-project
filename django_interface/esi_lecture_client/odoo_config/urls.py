from django.urls import path
from . import views
from .views import IndexView, test_connect

app_name = 'odoo_config'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('test_connect/', views.test_connect, name='test_connect'),
]
