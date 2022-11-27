from django.urls import path
from blog import views


urlpatterns = [
   path('', views.post_list_create_view),
    path('<int:pk>/update', views.post_update_view),
    path('<int:pk>/delete', views.post_destroy_view),
    path('<int:pk>/detail', views.post_detail_view),
    path('comment/', views.post_list_create_view),
    path('<int:pk>/update', views.comment_update_view),
    path('<int:pk>/delete', views.comment_destroy_view),
    path('<int:pk>/detail', views.comment_detail_view),
   
]
