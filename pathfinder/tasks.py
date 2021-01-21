import logging
import os
import tempfile

from .app_settings import PATHFINDER_WHITELIST, PATHFINDER_GROUPS

from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from allianceauth.authentication.models import CharacterOwnership

from celery import shared_task

logger = logging.getLogger(__name__)

def sync_characters():
    if not PATHFINDER_WHITELIST:
        logger.warn("PATHFINDER_WHITELIST not set")
        return
    if not PATHFINDER_GROUPS:
        logger.warn("PATHFINDER_GROUPS not set")
        return

    groups = Group.objects.filter(name__in=PATHFINDER_GROUPS)
    users = User.objects.filter(groups__in=groups)
    chars = CharacterOwnership.objects.filter(user__in=users)
    
    if not PATHFINDER_WHITELIST:
        logger.warn("PATHFINDER_WHITELIST not set")
        return

    with tempfile.NamedTemporaryFile(delete=False) as f:
        for char in chars:
            character_id = char.character.character_id
            f.write(str.encode(f"{character_id:d}\n"))
        os.replace(f.name, PATHFINDER_WHITELIST)
        os.chmod(PATHFINDER_WHITELIST, 0o666)

@shared_task
def sync(): 
    sync_characters()
