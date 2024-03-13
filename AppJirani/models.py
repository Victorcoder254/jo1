from django.db import models

class Services(models.Model):
    Service_name1 = models.CharField(max_length=100, null=True, blank=True)
    description1 = models.TextField(null=True, blank=True)
    Service_name2 = models.CharField(max_length=100, null=True, blank=True)
    description2= models.TextField(null=True, blank=True)
    Service_name3 = models.CharField(max_length=100, null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)

class About(models.Model):
    Years_1 = models.CharField(max_length=100, null=True, blank=True)
    Headline1 = models.CharField(max_length=100, null=True, blank=True)
    about1 = models.TextField(null=True, blank=True)
    Years_2 = models.CharField(max_length=100, null=True, blank=True)
    Headline2 = models.CharField(max_length=100, null=True, blank=True)
    about2 = models.TextField(null=True, blank=True) 
    Years_3 = models.CharField(max_length=100, null=True, blank=True)
    Headline3 = models.CharField(max_length=100, null=True, blank=True)
    about3 = models.TextField(null=True, blank=True)
    Years_4 = models.CharField(max_length=100, null=True, blank=True)
    Headline4 = models.CharField(max_length=100, null=True, blank=True)
    about4 = models.TextField(null=True, blank=True) 

class ForThoseWho(models.Model):
    title_1 = models.CharField(max_length=100, null=True, blank=True)
    description1 = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='ForThose/', null=True, blank=True)  
    title_2 = models.CharField(max_length=100, null=True, blank=True)
    description2 = models.TextField( null=True, blank=True)
    image2 = models.ImageField(upload_to='ForThose/', null=True, blank=True)  
    title_3 = models.CharField(max_length=100, null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    image3 = models.ImageField(upload_to='ForThose/', null=True, blank=True) 

class Testimonials(models.Model):
    name_1 = models.CharField(max_length=100, null=True, blank=True)
    description1 = models.TextField( null=True, blank=True)
    image1 = models.ImageField(upload_to='Testimonial/', null=True, blank=True)  
    name_2 = models.CharField(max_length=100, null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    image2 = models.ImageField(upload_to='Testimonial/', null=True, blank=True)  
    name_3 = models.CharField(max_length=100, null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    image3 = models.ImageField(upload_to='Testimonial/', null=True, blank=True) 



class AmazingTeam(models.Model):
    name1 = models.CharField(max_length=100, null=True, blank=True)
    role1 = models.CharField(max_length=100, null=True, blank=True)
    image1 = models.ImageField(upload_to='Team/', null=True, blank=True) 
    twitter1 = models.URLField(max_length=150, null=True, blank=True) 
    facebook1 = models.URLField(max_length=150, null=True, blank=True) 
    linkeldin = models.URLField(max_length=150, null=True, blank=True) 
    name2 = models.CharField(max_length=100, null=True, blank=True)
    role2 = models.CharField(max_length=100, null=True, blank=True)
    image2 = models.ImageField(upload_to='Team/', null=True, blank=True)  
    twitter2 = models.URLField(max_length=150, null=True, blank=True) 
    facebook2 = models.URLField(max_length=150, null=True, blank=True) 
    linkeldin2 = models.URLField(max_length=150, null=True, blank=True)  
    name3 = models.CharField(max_length=100, null=True, blank=True)
    role3 = models.CharField(max_length=100, null=True, blank=True)
    image3 = models.ImageField(upload_to='Team/', null=True, blank=True)  
    twitter3 = models.URLField(max_length=150, null=True, blank=True) 
    facebook3 = models.URLField(max_length=150, null=True, blank=True) 
    linkeldin3 = models.URLField(max_length=150, null=True, blank=True)  
    closingRemark = models.TextField(null=True, blank=True)

class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class OurSocials(models.Model):
    facebook = models.URLField(max_length=150, null=True, blank=True)
    twitter = models.URLField(max_length=150, null=True, blank=True)
    linkedin = models.URLField(max_length=150, null=True, blank=True)

class PrivacyPolicy(models.Model):
    policy = models.TextField(null=True, blank=True)

class TermsAndConditions(models.Model):
    terms = models.TextField(null=True, blank=True)     

class Copyright(models.Model):
    text = models.TextField(null=True, blank=True) 
    date = models.CharField(max_length=100, null=True, blank=True) 


