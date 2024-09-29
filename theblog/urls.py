
from django.urls import path
from theblog.views import HomeView,ArticleDetail,AddPostView,UpdatePostView,DeletePostView,AddCategory,CategoryView,LikeView#AddComment

urlpatterns = [
   #path('',views.home, name = "home")
   path('',HomeView.as_view(), name="home"),
   path('article/<int:pk>',ArticleDetail.as_view(),name ="article-detail"),
   path('add_post/',AddPostView.as_view(),name="add_post"),
   path('article/<int:pk>/update/',UpdatePostView.as_view(),name="update_post"),
   path('article/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
   path('add_category/',AddCategory.as_view(),name="add_category"),
   path('category/<str:cat>',CategoryView,name ="category"),
   path('like/<int:pk>',LikeView,name="like_post"),
   

    
]
