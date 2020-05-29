from django.db import models


class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150, verbose_name="Başlık", blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    icon = models.ImageField(blank=True, upload_to='images/')
    logo = models.ImageField(blank=True, upload_to='images/')
    company = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=50, blank=True)
    smtpserver = models.CharField(max_length=20, blank=True)
    smtpemail = models.CharField(max_length=20, blank=True)
    smtppassword = models.CharField(max_length=10, blank=True)
    smtpport = models.CharField(blank=True, max_length=5)
    facebook = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    aboutus = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    references = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    def __str__(self):
        return self.title

