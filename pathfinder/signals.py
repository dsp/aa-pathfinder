import logging

from django.dispatch import receiver

from django.db.models.signals import post_save
from allianceauth.authentication.models import CharacterOwnership

from .tasks import sync_characters

logger = logging.getLogger(__name__)

@receiver(post_save, sender=CharacterOwnership)
def removed_character(sender, instance, **kwargs):
    try:
        sync_characters()
    except Exception as e:
        logger.error(e)
        pass