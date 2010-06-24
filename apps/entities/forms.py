from entities.models import Entity
from perms.forms import TendenciBaseForm

class EntityForm(TendenciBaseForm):
    class Meta:
        model = Entity
        fields = (
        'entity_name',
        'contact_name',
        'phone',
        'fax',
        'email',
        'website',
        'summary',
        'notes',
        'admin_notes',
        )
      
    def __init__(self, user=None, *args, **kwargs):
        self.user = user 
        super(EntityForm, self).__init__(user, *args, **kwargs)