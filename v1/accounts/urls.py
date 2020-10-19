from django.urls import path
from .views.accept_invitation import AcceptInvitationView
from .views.login import LoginView
from .views.logout import LogoutView
from .views.profile import ProfileView, ProfileDetail
from .views.reset_password import ResetPasswordView
from .views.update_password import UpdatePasswordView
from .views.user import UserView, UserDetail

app_name = "accounts"

urlpatterns = [

    # Accept invitation
    path('accept_invitation/', AcceptInvitationView.as_view()),

    # Login / logout
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    # Password management
    path('reset_password/', ResetPasswordView.as_view()),
    path('update_password/', UpdatePasswordView.as_view()),

    # Profiles
    path('profiles/', ProfileView.as_view()),
    path('profiles/<profile_id>/', ProfileDetail.as_view()),

    # Users
    path('users/', UserView.as_view()),
    path('users/<user_id>/', UserDetail.as_view()),

]
