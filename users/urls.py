from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("profile/", views.profile, name="profile"),
    path("create_account/", views.create_account, name="create_account"),
    path("del_user/", views.del_user, name="del_user"),
    path("friends_list/", views.friends_list, name="friends_list"),
    path("add_friend/", views.add_friend, name="add_friend"),
    path("accept_request/", views.accept_request, name="accept_request"),
    path("remove_friend/", views.remove_friend, name="remove_friend"),
    path("friends_figurine/<int:id>", views.friends_figurine, name="friends_figurine"),
    path(
        "friends_figurine_search/",
        views.friends_figurine_search,
        name="friends_figurine_search",
    ),
]
