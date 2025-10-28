from django.http import HttpResponse
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
<<<<<<< HEAD
    path("", lambda request: HttpResponse("Welcome to my Django app! 🎉")),
    path("polls/", include("polls.urls")),
=======
    # Root URL redirects to login page
    path("", RedirectView.as_view(url="/studybuddy/login/")),
    # Include the studybuddy app URLs with namespace
    path(
        "studybuddy/",
        include(("studybuddy.urls", "studybuddy"), namespace="studybuddy"),
    ),
>>>>>>> 294059f (Add black, flake8, and coveralls to requirements.txt)
    path("admin/", admin.site.urls),
]
