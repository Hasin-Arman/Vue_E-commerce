from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.LoginView.as_view(),name="login"),
    path('users/',views.SignUpView.as_view(),name="signup"),
]
