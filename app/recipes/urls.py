from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

app_name = 'recipes'

router = DefaultRouter()
router.register('tags', views.TagViewSet)

urlpatterns = [
    path('recipes/', include(router.urls)),
]
