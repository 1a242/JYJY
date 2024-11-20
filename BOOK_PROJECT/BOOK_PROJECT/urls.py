"""
URL configuration for BOOK_PROJECT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from book import views
from django.conf.urls.static import static
from django.conf import settings
# from author import views as authorviews


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('bookhome',views.bookhome,name='bookhome'),
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    # path('authorhome',authorviews.authorhome,name='authorhome'),
    path('book/',include('book.urls')),
    path('author/',include('author.urls')),
    path('accounts/',include('accounts.urls')),
path('movie/',include('movie.urls')),
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)