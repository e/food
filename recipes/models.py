from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='images')
    votes_up = models.IntegerField()
    votes_down = models.IntegerField()

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)
    recipes = models.ManyToManyField(Recipe)

    def __unicode__(self):
        return self.name
