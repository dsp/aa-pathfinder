from django.conf import settings

# put your app settings here


PATHFINDER_WHITELIST = getattr(settings, "PATHFINDER_WHITELIST", None)
PATHFINDER_GROUPS = getattr(settings, "PATHFINDER_GROUPS", None)
