from django.urls import path
from .views import list_bonds, create_bond, update_bond, delete_bond

urlpatterns = [
    path('list', list_bonds, name='list_bonds'),
    path('new', create_bond,name='create_bond'),
    path('/update/<int:id>', update_bond, name='update_bond'),
    path('/delete/<int:id>', delete_bond, name='delete_bond'),
]
