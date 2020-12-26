from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import choice_bedrooms ,choice_price ,choices_state

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'states': choices_state,
        'bedrooms': choice_bedrooms,
        'prices':choice_price
    }
    
    return render(request, 'pages/index.html' , context)


def about(request):
    # Getting Realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # Getting Mvp's
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request, 'pages/about.html' , context)
