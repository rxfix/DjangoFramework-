from django.urls import path
import mainapp.views as mainapp
from .views import products,product

app_name = 'mainapp'
urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('category/<int:pk>', products, name='category'),
    path('product/<int:pk>/', product, name='detail'),
]
