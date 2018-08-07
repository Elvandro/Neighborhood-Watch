from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles', blank=True, default='../static/images/user.png')
    bio = models.TextField(max_length=500, default="I am Awesome")

    def __str__(self):
        return self.user

class Neighbourhood(models.Model):
    COUNTY_CHOICES = (
('Baringo','Baringo County'),
('Bomet','Bomet County'),
('Bungoma','Bungoma County'),
('Busia','Busia County'),
('Elgeyo Marakwet','Elgeyo Marakwet County'),
('Embu','Embu County'),
('Garissa','Garissa County'),
('Homa Bay','Homa Bay County'),
('Isiolo','Isiolo County'),
('Kajiado','Kajiado County'),
('Kakamega','Kakamega County'),
('Kericho','Kericho County'),
('Kiambu','Kiambu County'),
('Kilifi','Kilifi County'),
('Kirinyaga','Kirinyaga County'),
('Kisii','Kisii County'),
('Kisumu','Kisumu County'),
('Kitui','Kitui County'),
('Kwale','Kwale County'),
('Laikipia','Laikipia County'),
('Lamu','Lamu County'),
('Machakos','Machakos County'),
('Makueni','Makueni County'),
('Mandera','Mandera County'),
('Meru','Meru County'),
('Migori','Migori County'),
('Marsabit','Marsabit County'),
('Mombasa','Mombasa County'),
('Muranga','Muranga County'),
('Nairobi','Nairobi County'),
('Nakuru','Nakuru County'),
('Nandi','Nandi County'),
('Narok','Narok County'),
('Nyamira','Nyamira County'),
('Nyandarua','Nyandarua County'),
('Nyeri','Nyeri County'),
('Samburu','Samburu County'),
('Siaya','Siaya County'),
('Taita Taveta','Taita Taveta County'),
('Tana River','Tana River County'),
('Tharaka Nithi','Tharaka Nithi County'),
('Trans Nzoia','Trans Nzoia County'),
('Turkana','Turkana County'),
('Uasin Gishu','Uasin Gishu County'),
('Vihiga','Vihiga County'),
('Wajir','Wajir County'),
('West Pokot','West Pokot County'),

    )
    name = models.CharField(max_length = 300)
    description = models.TextField(max_length = 300)
    location = models.CharField(max_length = 100, choices=COUNTY_CHOICES)
    population = models.IntegerField()
    user = models.ForeignKey(User)

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def search_hood(cls,search_term):
        hood = cls.objects.filter(name__icontains = search_term)
        return hood

    def __str__(self):
        return self.name

class Join(models.Model):
    user_id = models.OneToOneField(User)
    hood_id = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return self.user_id

class Business(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    email_address = models.EmailField()
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbourhood)

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbourhood)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment
