from django.urls import path

from .views import (
    index,
    UserDetailView,
    SiteListView,
    SiteDetailView, profile_view, RegisterView,
)

urlpatterns = [
    path("", index, name="index"),
    path("profile", profile_view, name="profile"),
    path("register/", RegisterView.as_view(), name="register"),
    path("sites/", SiteListView.as_view(), name="site-list"),
    path("sites/<int:pk>/", SiteDetailView.as_view(), name="site-detail"),
    path(
        "users/<int:pk>/", UserDetailView.as_view(), name="user-detail"
    ),
]

app_name = "vpn"
