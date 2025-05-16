from django.urls import path
from .views import home, useradmin  
from .views import home, useradmin, new_article, edit_article, delete_article, about, search
from .views import home, article_detail 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"), 
    path('about/', about, name='about'),  # Page À propos
    path('search/', search, name='search'),  # Page de recherche
    path("useradmin/", useradmin, name="useradmin"),  #  la page d'administration utilisateur
    path('new_article/', new_article, name='new_article'),  # Page pour créer un nouvel article
    path('edit_article/<int:id>/', edit_article, name='edit_article'),  # Modifier un article
    path('delete_article/<int:id>/', delete_article, name='delete_article'),  # Supprimer un article
    path('article/<int:id>/', article_detail, name='article_detail'),  # Détail de l'article
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
