from django.apps import AppConfig


class PathfinderConfig(AppConfig):
    name = "pathfinder"
    label = "pathfinder"
    verbose_name = "pathfinder"

    def ready(self):
        import pathfinder.signals