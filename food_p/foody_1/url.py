from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'foody_1'

urlpatterns = [
    url(r"^login/$", auth_views.LoginView.as_view(template_name="foody_1/login.html"),name='login'),
    ]
