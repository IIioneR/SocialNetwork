
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls'), name='api'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]

if settings.DEBUG:

    from rest_framework import permissions
    from django.urls import path
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="StarNavi API docs",
            default_version='v1',
            description="StarNavi UI API Definition",
        ),
        public=False,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns = [
        path('schema/', schema_view.with_ui('swagger',
                                            cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc',
                                           cache_timeout=0), name='schema-redoc'),
    ] + urlpatterns
