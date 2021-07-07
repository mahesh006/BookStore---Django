from django.db import models
from django.utils.html import mark_safe

class Genre(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='2. Genre'

    def __str__(self):
        return self.title


class Language(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='3. Language'

    def __str__(self):
        return self.title



class Book(models.Model):
    image=models.ImageField(upload_to="book_imgs/",null=True)
    title=models.CharField(max_length=200,null=True)
    Author=models.CharField(max_length=200,null=True)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE,null=True)
    language=models.ForeignKey(Language,on_delete=models.CASCADE,null=True)


    class Meta:
        verbose_name_plural='1. Book'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))