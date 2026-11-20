from django.apps import AppConfig


class PokemonConfig(AppConfig):
    """Настройки приложения Pokémon."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pokemon'