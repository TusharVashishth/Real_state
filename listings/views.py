from django.shortcuts import render
from django.core.paginator import Paginator
from listings.choices import choice_bedrooms, choice_price, choices_state
from .models import Listing


def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listing, 6)
    page_number = request.GET.get('page')
    page_listing = paginator.get_page(page_number)
    context = {
        'listings': page_listing
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    context = {
        'listing': listing
    }
    # print("Data", context)
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # For keyword Searching
    if 'keywords' in request.POST:
        keywords = request.POST['keywords']

        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # For City Search
    if 'city' in request.POST:
        city = request.POST['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # For State filtering
    if 'state' in request.POST:
        state = request.POST['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # For Bedrooms Filtering
    if 'bedrooms' in request.POST:
        bedrooms = request.POST['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # For Price Filtering
    if 'price' in request.POST:
        price = request.POST['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'states': choices_state,
        'prices': choice_price,
        'bedrooms': choice_bedrooms,
        'listings': queryset_list,
        'values': request.POST
    }
    return render(request, 'listings/search.html', context)
