from django.contrib.admin.views.autocomplete import AutocompleteJsonView


class PublicAutocompleteJsonView(AutocompleteJsonView):
    def has_permission(self, request):
        # Allow all anonymous AJAX requests
        return request.headers.get("x-requested-with") == "XMLHttpRequest"