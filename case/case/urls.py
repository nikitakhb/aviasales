from django.urls import path, include
from anagram.views import LoadWordsView, FindAnagramView

from rest_framework.routers import SimpleRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


router = SimpleRouter()
router.register('load', LoadWordsView, basename='load')
router.register('get', FindAnagramView, basename='find')

schema = get_schema_view(
    openapi.Info(
        title='Aviasales API',
        default_version='0.9',
    ),
    public=True,
)

urlpatterns = [
    path('', include(router.urls)),
    path('', schema.with_ui('swagger'), name='swagger')
]
