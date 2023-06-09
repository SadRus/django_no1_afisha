from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        'Название',
        max_length=80,
    )
    description_short = models.TextField(
        'Краткое описание',
        blank=True,
    )
    description_long = HTMLField(
        'Описание',
        blank=True,
    )
    longitude = models.FloatField(
        'Долгота',
    )
    latitude = models.FloatField(
        'Широта',
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='imgs',
        verbose_name='Место',
    )

    image = models.ImageField(
        'Картинка',
    )
    position = models.PositiveIntegerField(
        'Позиция',
        default=0,
        null=True,
        blank=True,
        db_index=True,
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.id} {self.place.title}'
