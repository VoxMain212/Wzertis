from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve


urlpatterns = [
    path('api/author/profile/', views.author_info_api, name='author_profile'),
    path('api/groups/', views.get_groups, name='groups'),
    path('api/artworks/', views.get_artworks, name='artworks'),
    path('api/fav_works/', views.get_fav_artworks, name='fav_works'),
    path('api/groups/<int:group_id>/', views.get_group_by_id, name='group_id'),
    path('api/appeal/', views.send_appeal, name='appeal'),
    path('', views.index, name='home')
]

# if not settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
        re_path(r'^favicon\.ico$', serve, {
            'document_root': settings.MEDIA_ROOT,
            'path': 'favicon.ico',
        }),
    ]