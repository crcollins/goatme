from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=400)
	filename = models.CharField(max_length=50)
	pdf = models.FileField(upload_to='articles')