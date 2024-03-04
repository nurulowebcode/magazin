from django.urls import path
from .views import *

urlpatterns = [
    path('get-banner/', get_banner),
    path('get-about/', get_about),
    path('get-about/', get_about),
    path('get-servise/', get_servise),
    path('get-project/', get_project),
    path('get-ourtem/', get_ourtem),
    path('get-partyor/', get_partyor),
    path('get-info/', get_info),
    path('get-news/', get_news),
    path('get-contact/', get_contact),

]

