from django.conf.urls import include, url
from .views import BookRentView

urlpatterns = [
    url(r'^form/$', BookRentView.as_view(), name='rent-form'),
]