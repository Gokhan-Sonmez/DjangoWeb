from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=100, verbose_name="Başlık")
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255, verbose_name="Açıklama")
    image = models.ImageField(blank=True, upload_to='images/', verbose_name="Resim")
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Ekleme Tarihi")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategori")
    title = models.CharField(max_length=150, verbose_name="Başlık")
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/', verbose_name="Resim")
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    def __str__(self):
        return self.title


    def image_tag(self):
        return mark_safe('<img src="{}" height="150"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Images(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   title = models.CharField(max_length=50, verbose_name="Başlık")
   image = models.ImageField(blank=True, upload_to='images/', verbose_name="Resim")

   def __str__(self):
       return self.title

