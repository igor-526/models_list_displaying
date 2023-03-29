from django.shortcuts import render, HttpResponse, redirect
from books.models import Book


def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    for book in books:
        book.pub_date = str(book.pub_date)
    context = {'books': books}
    return render(request, template, context)

def books_date(request, date):
    template = 'books/books_date.html'
    books = Book.objects.filter(pub_date=date)
    all = Book.objects.all().order_by('pub_date')
    dates = []
    for book in books:
        book.pub_date = str(book.pub_date)
    for book in all:
        book.pub_date = str(book.pub_date)
        if book.pub_date not in dates:
            dates.append(book.pub_date)
    cur_page = dates.index(date)
    try:
        if cur_page == 0:
            raise
        prev_page = dates[cur_page-1]
    except:
        prev_page = ''
    try:
        next_page = dates[cur_page+1]
    except:
        next_page = ''
    context = {'books': books, 'current': date, 'prev': prev_page, 'next': next_page}
    return render(request, template, context)
