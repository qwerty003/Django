from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=25)
    genre = models.CharField(max_length=15)
    logo = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=15)
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title + '.' + self.file_type


class Users(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=10, null=True)
    organisation = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.id


















