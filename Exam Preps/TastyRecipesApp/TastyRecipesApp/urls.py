
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TastyRecipesApp.core.urls')),
    path('recipe/', include('TastyRecipesApp.recipe.urls')),
    path('profile/', include('TastyRecipesApp.user_profile.urls')),
]
