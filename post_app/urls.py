from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import  UserSignupView, PostCreateView, PostListView, LikePostView, signup_page, login_page, posts_page

urlpatterns = [
    path('', signup_page, name='signup_page'),
    path('login/', login_page, name='login_page'),
    path('posts/', posts_page, name='posts_page'),
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('api/signup/', UserSignupView.as_view(), name='user-signup'),
    path('api/posts/create/', PostCreateView.as_view(), name='post-create'),
    path('api/posts/', PostListView.as_view(), name='post-list'),  # Make sure this path is correct
    path('api/posts/<int:post_id>/like/', LikePostView.as_view(), name='post-like'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
