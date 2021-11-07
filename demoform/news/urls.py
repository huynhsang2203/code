from django.urls import path
from .import views

urlpatterns = [
    path('',views.ClassIndex.as_view(), name='index'),
    path('email/', views.email, name='email'),
    path('list_mail',views.list_mail, name='list_mail' ),
    path('add/', views.ClassPost.as_view(), name='add'),
    path('save/', views.post_view, name='save'),
]
