from django.utils.translation import ugettext_lazy as _

from .tasks import sync_characters

from allianceauth import hooks
from allianceauth.services.hooks import ServicesHook

class PathfinderService(ServicesHook):
    def __init__(self):
        pass
        ServicesHook.__init__(self)
        self.urlpatterns = []

    def update_groups(self, user):
        sync_characters()


@hooks.register('services_hook')
def register_service():
    return PathfinderService()
