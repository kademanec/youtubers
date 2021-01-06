from django.db import models



class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
    link_button = models.URLField(max_length=255, default=None)


    def __str__(self):
        return self.headline

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d/")
    created_date = models.DateTimeField(auto_now_add=True)
    youtube_link = models.URLField(max_length=255,default=None)
   

    def __str__(self):
        return self.first_name
