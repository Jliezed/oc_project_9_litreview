from django.urls import path

import user.views

app_name = "user"
urlpatterns = [
    # Register
    path("register/", user.views.signup_page, name="register"),
]