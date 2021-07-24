from django.urls import path
from . import views

"""path('new-search/', views.new_search, name='new_search' ),"""

urlpatterns = [
    path('', views.home, name='home'),
]
