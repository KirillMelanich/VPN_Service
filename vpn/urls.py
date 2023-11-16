from django.urls import path

from .views import (
    index,
    UserDetailView,
    SiteListView,
    SiteDetailView, profile_view, RegisterView, SiteCreateView, SiteUpdateView, SiteDeleteView, UserUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("profile", profile_view, name="profile"),
    path("register/", RegisterView.as_view(), name="register"),
    path("sites/", SiteListView.as_view(), name="site-list"),
    path(
        "sites/create/",
        SiteCreateView.as_view(),
        name="site-create",
    ),
    path(
        "sites/<int:pk>/update/",
        SiteUpdateView.as_view(),
        name="site-update",
    ),
    path(
        "sites/<int:pk>/delete/",
        SiteDeleteView.as_view(),
        name="site-delete",
    ),
    path("sites/<int:pk>/", SiteDetailView.as_view(), name="site-detail"),
    path(
        "users/<int:pk>/", UserDetailView.as_view(), name="user-detail"
    ),
    path(
        "users/<int:pk>/", UserUpdateView.as_view(), name="user-update"
    ),
]

app_name = "vpn"
