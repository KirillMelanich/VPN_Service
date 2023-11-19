from django.urls import path

from .views import (
    index,
    SiteListView,
    SiteDetailView, RegisterView, SiteCreateView, SiteUpdateView, SiteDeleteView, ProfileDetailView, ProfileUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile-detail"),
    path("profile/<int:pk>/update/", ProfileUpdateView.as_view(), name="profile-update"),
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
]

app_name = "vpn"
