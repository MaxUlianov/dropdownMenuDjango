from django.urls import path
from .views import page

app_name = 'menuApp'

urlpatterns = [
    path('menu', page, name='basic_page'),
    path('menu/<str:menus>/', page, name='menus_page'),
    path('menu/<str:menus>/<str:active>/', page, name='active_menu_page')
]
