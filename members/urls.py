from django.urls import path
from .views import UserRegisterView,UserEditView,PasswordChange,Password_changed_successfully,ShowProfilePageView,EditProfilePageView,CreateProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name ='register'),
    path('edit/',UserEditView.as_view(),name ='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='change_password'),
    path('password/', PasswordChange.as_view(template_name='registration/change-password.html'), name='change_password'),
    path('password-changed',Password_changed_successfully,name="Password_changed_successfully"),
    path('profile/<int:pk>',ShowProfilePageView.as_view(),name ="profile"),
    path('edit_profile_page/<int:pk>',EditProfilePageView.as_view(),name ="edit_profile_page"),
    path('create_profile_page',CreateProfilePageView.as_view(),name ="create_profile_page"),



    
]
