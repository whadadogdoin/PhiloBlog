from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
    path('drafts/',views.drafts_list,name='drafts_list'),
    path('post/<pk>/publish/',views.post_publish,name='post_publish'),
    path('post/<pk>/delete/',views.post_delete,name='post_delete'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove')
]