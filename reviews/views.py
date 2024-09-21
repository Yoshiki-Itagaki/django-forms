from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from reviews.models import Review

from .forms import ReviewForm

# Create your views here.

class ReviewView(View):
    def get(self, request):        
        form = ReviewForm()
            
        return render(request, "reviews/review.html", {
            "form": form
        })
        
    def post(self, request):
        form = ReviewForm(request.POST)
        
        if form.is_valid():         
            form.save()           
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })
        
class ThankYouView(TemplateView):
    template_name="reviews/thank_you.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    
class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context
    
class SingleReviewView(TemplateView):     
    template_name = "reviews/single_review.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        context["review"] = selected_review
        return context

# def review(request):
    
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
        
#         if form.is_valid():         
#             form.save()           
#             return HttpResponseRedirect("/thank-you")
        
#     else:
#         form = ReviewForm()
    
#     return render(request, "reviews/review.html", {
#         "form": form
#     })

# def thank_you(request):
#     return render(request, "reviews/thank_you.html")