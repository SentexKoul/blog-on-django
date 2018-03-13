"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Articles


urlpatterns = [
    # Выводит первые 20 статей, сортируя по date
    url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by('-date')[:20],
                                template_name="blog/posts.html")),

    # Cмотрит чтобы в адресе после /blog/... был id поста
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles,
                                             template_name="blog/post.html"))
]
