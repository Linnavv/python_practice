from django.db import models


class Pokemon(models.Model):
    """Модель покемона в команде пользователя."""

    name = models.CharField(max_length=100, unique=True)
    pokemon_id = models.IntegerField()
    image = models.URLField()
    pokemon_type = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    abilities = models.JSONField(default=list)
    stats = models.JSONField(default=dict)

    def __str__(self):
        """Возвращает имя покемона."""
        return self.name