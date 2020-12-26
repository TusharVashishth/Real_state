from django.shortcuts import redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        # Check if user already done enquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_connected = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_connected:
                messages.error(request, 'You have already made an enquiry for this listing')
                return redirect('listing', listing_id)
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                          user_id=user_id)
        contact.save()
        # Send Email
        send_mail(
            'Property Listing Inquiry',
            'There has been inquiry for' + listing + '. Sign into the admin panel for more info',
            'tusharvashisth4@gmail.com',
            [email , 'tusharvashishth29@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted , a realtor will get back to')
        return redirect('listing', listing_id)
