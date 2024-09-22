from typing import Any
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from reviews.models import Review

from .forms import ReviewForm

# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"  
    
class ThankYouView(TemplateView):
    template_name="reviews/thank_you.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
    # def get_queryset(self):
    #    base_query = super().get_queryset()
    #    data = base_query.filter(rating__gte=4)
    #    return data          
    
class SingleReviewView(DetailView):     
    template_name = "reviews/single_review.html"
    model = Review
    
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