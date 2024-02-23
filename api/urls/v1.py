import os

from django.urls import include, path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


app_name = os.getcwd().split(os.sep)[-1]



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = (
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("auth/", include("module.auth.urls", namespace="auth")),
    path("account/", include("module.account.urls", namespace="account")),
)
