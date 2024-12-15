"""foody URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 管理后台URL
    url(r"^$", views.HomePage.as_view(), name="home"),  # 首页URL
    url(r"^foody_1/", include("foody_1.urls", namespace="foody_1")),  # foody_1应用的URL
    url(r"^seller/", include("seller.urls", namespace="seller")),  # seller应用的URL
    url(r"^foody_1/", include("django.contrib.auth.urls")),  # 用户认证相关URL
    url(r"^thanks/$", views.ThanksPage.as_view(), name="thanks"),  # 感谢页URL
    url(r"^test/$", views.TestPage.as_view(), name="test"),  # 测试页URL
]
