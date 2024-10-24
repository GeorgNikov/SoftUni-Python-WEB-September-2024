from django.urls import path, include

from . import views


urlpatterns = [
    path('add/', views.CreateAlbumView.as_view(), name='album-add'),
    path('<int:id>/', include([
        path('details/', views.DetailsAlbumViews.as_view(), name='album-details'),
        path('edit/', views.EditAlbumView.as_view(), name='album-edit'),
        path('delete/', views.DeleteAlbumViews.as_view(), name='album-delete'),
    ])),
]