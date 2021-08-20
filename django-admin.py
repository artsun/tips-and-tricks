from django.contrib import admin


class LimitedAdmin(admin.ModelAdmin):
    """
    Used to make entities read-only. readonly_fields and render_change_form methods acts equivalently
    with has_change_permission method, but makes entities available via horizontal menu drop-downs
    """

    @property
    def readonly_fields(self):
        return [field.name for field in self.model._meta.get_fields() if not field.one_to_many and not field.one_to_one]

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        response = super().render_change_form(request, context, add, change, form_url, obj)
        response.context_data['has_change_permission'] = False
        return response

    def has_add_permission(self, request, obj=None):  # pylint: disable=W0221, W0613
        """disable add button"""
        return False

    def has_delete_permission(self, request, obj=None):
        """disable delete button"""
        return False

    def get_actions(self, request):  # hide default delete action
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
