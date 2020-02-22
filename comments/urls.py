from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', views.PostListView.as_view(), name='posts_list'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('blog/<int:pk>/comment', views.PostMaker.as_view(), name='comment_form'),
]