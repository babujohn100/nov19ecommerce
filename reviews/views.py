from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Review
from .forms import PostForm
from django.contrib.auth.decorators import permission_required

# Create your views here.

# def get_index(request):
#     reviews = Review.objects.filter(published_date__lte = timezone.now())
#     return render(request, "ecommerce/base.html", {'reviews': reviews})

def user_can_edit_review(request, review):
    wrote_the_review = review.author == request.user
    superuser = request.user.is_superuser
    return wrote_the_review or superuser
    
    
def read_review(request, id):
    review = Review.objects.get(pk=id)

    can_edit = user_can_edit_review(request, review)

    return render(request, "reviews/read_review.html", 
        {
            'review': review, 
            'can_edit': can_edit
        })


@login_required
def write_review(request, id):
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        review = form.save(commit=False)
        review.author = request.user
        review.save()
        return redirect("product_detail", id = id)
    else:
        form = PostForm()
        return render(request, "reviews/review_form.html", {'form': form})



def edit_review(request, id):
    review = get_object_or_404(Review, pk=id)
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES, instance=review)
        form.save()
        return redirect(read_review, id)
    else:
        form = PostForm(instance=review)
        return render(request, "reviews/review_form.html", {'form': form})   



@permission_required('review.can_publish')
def publish_review(request, id):
    review = get_object_or_404(Post, pk=id)
    review.published_date = timezone.now()
    review.save()
    return redirect(read_review, review.id)        
    
