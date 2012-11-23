import autocomplete_light

from models import Project, Member


autocomplete_light.register(Project,
    search_fields=('name',),
    autocomplete_js_attributes={'placeholder': 'Project...'}
)

autocomplete_light.register(Member,
    search_fields=('name',),
    autocomplete_js_attributes={'placeholder': 'Member...'}
)
