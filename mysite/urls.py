from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/studybuddy/login/")),  # root redirects to login  # noqa: E501
    path("studybuddy/", include("studybuddy.urls")),
    path("admin/", admin.site.urls),
]
