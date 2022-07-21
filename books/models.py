from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):

    name = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)
    date_of_relase = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.author}"


class Comment(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="comments")
    owner_of_comment = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)
    raiting = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.raiting} - {self.owner_of_comment}"
