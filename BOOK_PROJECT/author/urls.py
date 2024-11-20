from django.urls import path
from . import views

urlpatterns=[
    path("authorhome",views.authorhome,name='authorhome'),
    path('<int:author_id>', views.authordetail, name='authordetail'),
    path('<int:author_id>/createauthorreview', views.createauthorreview, name='createauthorreview'),
    path('review/<int:review_id>', views.updateauthorreview, name='updateauthorreview'),
    path('review/<int:review_id>/delete', views.deleteauthorreview, name='deleteauthorreview'),
]