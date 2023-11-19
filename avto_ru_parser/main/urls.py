from django.urls import path
from .views import index, reload_auto_base, show_models

urlpatterns = [
    path('', index, name='home'),
    path('reload_auto_base', reload_auto_base, name='reload'),
    path('show_models', show_models, name='show_models')
]