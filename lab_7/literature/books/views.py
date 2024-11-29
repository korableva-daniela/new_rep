from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.shortcuts import render
from django.http import  HttpResponse
from .form import AuthorForm
from .form import BookForm
from .models import Book
from .models import Author
from django.views.generic import DetailView, UpdateView
def author_create(request):
    form=AuthorForm()
    if request.method=='POST':
        firs_name=request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        email = request.POST.get('email')

        Author.objects.create(first_name=firs_name,second_name=second_name,
                              email=email)
    context={
    'form':form,
    }
    return render(request, 'add_author.html', context)


def author_update(request,id1):
    instance = get_object_or_404(Author, id=id1)
    form=AuthorForm(request.POST,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        form.cleaned_data.get('second_name')
    context={
        'form':form,
        'instance':instance,
        'id':id1,
    }
    return render(request, 'update_author.html', context)

def author_info(request,id):
    instance=get_object_or_404(Author,id=id)
    context=\
        {
            'instance': instance,
            'title': 'Дополнительная информация об авторе',
        }
    return render(request, 'info_author.html', context)
def author_list(request):
    queryset=Author.objects.all()
    context = {
        'queryset': queryset,
        'title': 'Список всех авторов',
        'name':'Авторы'
    }
    return render(request,'all_author.html',context)

def book_create(request):
    form=BookForm()
    if request.method=='POST':
        title=request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status')
        post_author=request.POST.get('post_author')

        Book.objects.create(title=title,content=content,status=status)
    context={
    'form':form,
    }
    return render(request, 'add_book.html', context)


def book_update(request,id1):
    instance = get_object_or_404(Book, id=id1)
    form=BookForm(request.POST,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        form.cleaned_data.get('title')
    context={
        'form':form,
        'instance':instance,
        'id':id1,
    }
    return render(request, 'update_book.html', context)

def book_info(request,id):
    instance=get_object_or_404(Book,id=id)
    context=\
        {
            'instance': instance,
            'title': 'Дополнительная информация о книге',
        }
    return render(request, 'info_book.html', context)
def book_list(request):
    queryset=Book.objects.all()
    context = {
        'queryset': queryset,
        'title': 'Список всех книг ',
        'name':'Книги'
    }
    return render(request,'all_book.html',context)