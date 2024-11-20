from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author,Review1
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def authorhome(request):
    searchTerm = request.GET.get('searchAuthor')
    if searchTerm:
        author_list  = Author.objects.filter(title__contains=searchTerm)
    else:
        author_list =Author.objects.all()
        paginator = Paginator(author_list, 2)
        page_number = request.GET.get('page', 1)
        authors = paginator.page(page_number)
        return render(request,'authorhome.html',{'searchTerm':searchTerm,'authors':authors})

def authordetail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    reviews = Review1.objects.filter(author=author)
    return render(request, 'authordetail.html', {'author': author,'reviews':reviews})

@login_required
def createauthorreview(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'GET' :
        return render(request, 'createauthorreview.html' ,
        {'form':ReviewForm , 'author':author})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.author = author
            newReview.save()
            return redirect('authordetail',newReview.author.id)
        except ValueError:
            return render(request,'createauthorreview.html', {'form':ReviewForm, 'error':'非法数据'})

@login_required
def updateauthorreview(request, review_id) :
    review = get_object_or_404(Review1, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updateauthorreview.html', {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('authordetail', review.author.id)
        except ValueError:
            return render(request, 'updateauthorreview.html', {'review':review, 'form':form, 'error':'提交非法数据'})

@login_required
def deleteauthorreview(request, review_id) :
    review = get_object_or_404(Review1, pk=review_id, user=request.user)
    review.delete()
    return redirect('authordetail', review.author.id)