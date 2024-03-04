from django.db import models

class Banner(models.Model):
    name = models.CharField(max_length=225)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Servise(models.Model):
    name = models.CharField(max_length=200)
    descrption = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='serves/logo/')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='project/img/')

    def __str__(self):
        return self.name


class Ourtem(models.Model):
    name = models.CharField(max_length=200)
    jop = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photo/')
    instagram = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    vciped = models.CharField(max_length=200)
    google = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='news/logo/')

    def __str__(self):
        return self.name


class Partyor(models.Model):
    logo = models.ImageField(upload_to='partyor/logo/')


class Contact(models.Model):
    name = models.CharField(max_length=225)
    text = models.TextField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Info(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    phone_number = models.CharField(max_length=13)
    email = models.CharField(max_length=225)
    fax = models.IntegerField()

    def __str__(self):
        return self.name





