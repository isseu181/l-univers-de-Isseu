from django.shortcuts import render
from .models import Article
from django.shortcuts import render, redirect
from .forms import ArticleForm  # Formulaire à créer
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm  # Formulaire à créer

def home(request):
    articles = Article.objects.all()  # Récupère tous les articles
    return render(request, "index.html", {"articles": articles})  # Passe les articles au template
def useradmin(request):
    return render(request, "useradmin.html")  # Affiche le template useradmin.html

def about(request):
    return render(request, "about.html")  # Page À propos
def search(request):
    query = request.GET.get('query', '')  # Récupère la requête de recherche
    results = []

    if query:
        # Rechercher dans le modèle 'Article' par le titre (ou un autre champ pertinent)
        results = Article.objects.filter(title__icontains=query)

    return render(request, 'search.html', {'results': results, 'query': query})

def useradmin(request):
    articles = Article.objects.all()  # Récupérer tous les articles (filtrer par auteur si nécessaire)
    return render(request, "useradmin.html", {"articles": articles})


def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('useradmin')  # Redirige vers la page admin après création
    else:
        form = ArticleForm()
    return render(request, 'new_article.html', {'form': form})

def edit_article(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('useradmin')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'new_article.html', {'form': form}) 
def delete_article(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('useradmin')

from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

from django.shortcuts import render, get_object_or_404
from .models import Article

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})

