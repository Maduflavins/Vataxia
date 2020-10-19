from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
# ...
#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,)
# )


urlpatterns = [
    #Documentation
    # path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # API (v1)
    path('accounts/', include('v1.accounts.urls'), name='accounts'),
    path('credits/', include('v1.credits.urls'), name='credits'),
    path('posts/', include('v1.posts.urls'), name='posts'),
    path('private/', include('v1.private_messages.urls'), name='private'),
    path('replies/', include('v1.replies.urls'), name='replies'),
    path('roles/', include('v1.user_roles.urls'), name='roles'),
    path('votes/', include('v1.votes.urls'), name='votes'),

    # Core
    path('admin/', admin.site.urls),
    # path(r'^', include_docs_urls(title='Vataxia')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:

#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]
