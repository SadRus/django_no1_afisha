from django.db import models


class Place(models.Model):

    title = models.CharField(
        'Название',
        max_length=80,
    )
    description_short = models.TextField(
        'Краткое описание',
    )
    description_long = models.TextField(
        'Описание',
    )
    longitude = models.FloatField(
        'Долгота',
    )
    latitude = models.FloatField(
        'Широта',
    )

    def display_description_short(self):
        return self.description_short[:100] + '...'

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
        'Картинка'
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

    def __str__(self) -> str:
        return str(self.id) + ' ' + self.place.title
