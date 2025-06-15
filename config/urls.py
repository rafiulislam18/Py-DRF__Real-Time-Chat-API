from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Real-time Chat API",
        default_version='v1',
        description=(
            "API documentation for Real-time Chat API\n"
            "GitHub Profile: https://github.com/rafiulislam18/\n"
            "GitHub Repo (codes): https://github.com/rafiulislam18/Py-DRF__Real-Time-Chat-API"
        ),
        contact=openapi.Contact(email="cmmnacrafiulislam0170@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/swagger/', permanent=False), name='landing'),

    # Config URLs for custom apps
    path('auth/', include('apps.authentication.urls')),
    # path('rtchat/', include('apps.rtchat.urls')),

    # Config URLs for Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # example path: domain/swagger.json/
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
]
