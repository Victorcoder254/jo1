from django.contrib import admin
from .models import*

models = [Services, About, ForThoseWho, Testimonials, AmazingTeam, ContactUs, OurSocials, TermsAndConditions, PrivacyPolicy, Copyright]

admin.site.register(models)

