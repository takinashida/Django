from django.urls import path, include
from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


app_name = BlogConfig.name

urlpatterns = [
    path('blog/', PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blog/create/', PostCreateView.as_view(), name='post_form'),
    path('blog/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('blog/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
