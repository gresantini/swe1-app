from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Root URL redirects to login page
    path("", RedirectView.as_view(url="/studybuddy/login/")),  # noqa: E501
    # Include the studybuddy app URLs with namespace
    path(
        "studybuddy/",
        include(("studybuddy.urls", "studybuddy"), namespace="studybuddy"),
    ),
    # Include the polls app URLs
    path("polls/", include("polls.urls")),
    # Admin site
    path("admin/", admin.site.urls),
]
