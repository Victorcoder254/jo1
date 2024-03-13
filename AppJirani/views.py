from django.shortcuts import render
from .models import Services, About, ForThoseWho, Testimonials, AmazingTeam, ContactUs, OurSocials, TermsAndConditions, PrivacyPolicy, Copyright

def index(request):
    # Get specific objects for each model
    services = Services.objects.first()  # Assuming you want the first object
    about = About.objects.first()
    for_those_who = ForThoseWho.objects.first()
    testimonials = Testimonials.objects.first()
    amazing_team = AmazingTeam.objects.first()
    our_socials = OurSocials.objects.first()
    terms_and_conditions = TermsAndConditions.objects.first()
    privacy_policy = PrivacyPolicy.objects.first()
    copyright = Copyright.objects.first()

    # If the request method is POST
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Create a new ContactUs object
        contact = ContactUs.objects.create(name=name, email=email, phone=phone, message=message)

        contact.save()

    return render(request, 'website/index.html', {
        'services': services,
        'about': about,
        'for_those_who': for_those_who,
        'testimonials': testimonials,
        'amazing_team': amazing_team,
        'our_socials': our_socials,
        'terms_and_conditions': terms_and_conditions,
        'privacy_policy': privacy_policy,
        'copyright': copyright,
    })