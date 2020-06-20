from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('createProduct/',views.create,name='create'),
    path('products/<int:id>/',views.product,name='product'),
    path('products/<int:id>/upvote',views.upvote,name='upvote')
]
