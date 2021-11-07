from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/detail/', views.detail_list_question, name='details'),
    path('list/', views.question_list, name='question_list'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/votes/', views.total_vote, name='votes')

]
