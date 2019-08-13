from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/', include('accueil.urls')),
    path('aliment/', include('aliment.urls')),
    path('compte/', include('compte.urls')),
    path('resultat/', include('resultats.urls')),
]
