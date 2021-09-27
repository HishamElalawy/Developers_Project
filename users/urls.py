from django.urls import path
from . import views

urlpatterns = [
    path('',views.profiles , name="profiles"),
    path('profile/<str:pk>/' , views.userProfile , name="profile"),
    path('login/' , views.loginUser , name="login"),
    path('logout/' , views.logoutUser , name="logout"),
    path('signup/' , views.registerUser , name="signup"),
    path('account/' , views.userAccount , name="account"),
    path('edit-account/' , views.editUserAccount , name="edit-account"),
    path('create-skill/',views.createSkill , name="create-skill"),
    path('edit-skill/<str:pk>/',views.updateSkill,name="edit-skill"),
    path('delete-skill/<str:pk>/',views.deleteSkill,name="delete-skill"),
    path('inbox/',views.inbox,name="inbox"),
    path('view-message/<str:pk>/',views.viewMessage,name="view-message"),
    path('send-message/<str:pk>/',views.createMessage,name="send-message"),
]