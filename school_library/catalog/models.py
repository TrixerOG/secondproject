from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField(max_length=1000, blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True)

    def __str__(self):
        return self.title