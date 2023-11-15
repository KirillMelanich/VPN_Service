from django.urls import path

from .views import (
    index,
    UserDetailView,
    SiteListView,
    SiteDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("sites/", SiteListView.as_view(), name="site-list"),
    path("sites/<int:pk>/", SiteDetailView.as_view(), name="site-detail"),
    path(
        "users/<int:pk>/", UserDetailView.as_view(), name="user-detail"
    ),
]

app_name = "vpn"
