from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('note', views.NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
