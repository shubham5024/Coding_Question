from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('add_item',views.add_item,name="add_item"),
    path('update_item',views.update_item,name='update_item'),
    path('add_submit',views.add_submit,name='add_submit'),
    path('view_list',views.view_list,name='view_list')
]
