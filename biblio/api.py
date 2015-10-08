# tutaj definiuje struktur� mojego API
from rest_framework import routers
from shelf.api import AuthorViewSet

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet)
