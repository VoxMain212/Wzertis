from django.urls import path
from . import views


urlpatterns = [
    path('author/profile/', views.author_info_api, name='author_profile'),
    path('groups/', views.get_groups, name='groups'),
    path('artworks/', views.get_artworks, name='artworks'),
    path('fav_works/', views.get_fav_artworks, name='fav_works'),
    path('groups/<int:group_id>/', views.get_group_by_id, name='group_id'),
    path('appeal/', views.send_appeal, name='appeal')
]