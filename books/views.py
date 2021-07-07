from django.shortcuts import render
from .models import Book,Language,Genre
from django.http import JsonResponse
from django.template.loader import render_to_string


def home(request):
    data = Book.objects.all().order_by('-id')
    genres = Genre.objects.all().order_by('-id')
    languages = Language.objects.all().order_by('-id')
    return render(request,'books_list.html',{'data':data, 'genre':genres, 'language':languages})


def filter_data(request):
    genres=request.GET.getlist('genre[]')
    languages=request.GET.getlist('language[]')
    allbooks=Book.objects.all().order_by('-id').distinct()
    if len(genres)>0:
        allbooks=allbooks.filter(genre__id__in=genres).distinct()
    if len(languages)>0:
        allbooks=allbooks.filter(language__id__in=languages).distinct()
    
    t=render_to_string('ajax/books_list.html',{'data':allbooks})
    return JsonResponse({'data':t})


def add_books(request):
    genres = Genre.objects.all().order_by('-id')
    languages = Language.objects.all().order_by('-id')
    if request.method =="POST":
        bookname= request.POST['bookname']
        author= request.POST['author']
        photo= request.FILES['photo']
        language= request.POST['language']
        genre = Genre.objects.get(title = request.POST['genre'])
        ins = Book(title=bookname,Author=author,image=photo,genre=genre,language=Language.objects.get(title=language))
        ins.save()         
    return render(request,'Add_books.html', {'data':genres,'language':languages})
