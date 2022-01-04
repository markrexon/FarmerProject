from django.contrib.auth import views as auth_views
from django.urls import path
from .views import Addpost, HomeView,updatePost,about,index,LikeView,AddComment,ArticleDetail,CustomerForm,UserChanges

app_name = 'blogpost'
 
urlpatterns = [
    path('',index,name="home"),
    path('about/',about,name="about"), 
    path('myblog/',HomeView.as_view(),name="homing"),
    path('myblog/<int:pk>/',HomeView.as_view(),name="homepage"),
    path("article/<int:pk>/",ArticleDetail.as_view(),name="article-detail"),
    path("addPost/",Addpost.as_view(),name="add"),
    path("article/edit/<int:pk>/",updatePost.as_view(),name="updating"),
    path("like/<int:pk>",LikeView,name="like_post"),
    path('article/<int:pk>/comment/',AddComment.as_view(),name="addComments"),
    path('feed/',CustomerForm,name="feedbacks"),
    path("edit_profile/",UserChanges.as_view(),name="profile_edit"),
    path("password/",auth_views.PasswordChangeView.as_view(template_name="change_password.html")),

]
    
