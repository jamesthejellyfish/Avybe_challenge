from django.urls import path
from . import views

urlpatterns = [
    path('', views.ImageListView.as_view(), name='index'),
    path('search/<str:search>', views.search, name='search'),
    path('upload', views.upload_file, name='upload'),
    path('image/<int:pk>', views.image_request, name='image'),
    path('register', views.register, name='register'),
    path('edit/<int:pk>', views.edit_file, name='edit_image'),
    path('search/edit/<int:pk>', views.edit_file, name='edit_image'),
    path('user/<str:username>', views.user, name='user')
]
