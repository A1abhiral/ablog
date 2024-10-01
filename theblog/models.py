from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        #return reverse("article-detail", args=(str(self.id)))
        return reverse("home")

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE )
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/profile/")
    facebook_url = models.CharField(null=True,blank=True,max_length=255)
    instagram_url = models.CharField(null=True,blank=True,max_length=255)
    X_url = models.CharField(null=True,blank=True,max_length=255)
    linkedin_url = models.CharField(null=True,blank=True,max_length=255)

    

    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse("home")
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(upload_to='images/', blank=True, null=True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255,default="defaut category")
    #body = RichTextField(blank=True,null=True)
    snippet = models.CharField(max_length=255,default="this is default snippet")
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse("article-detail", args=(str(self.id)))
        return reverse("home")



    
    