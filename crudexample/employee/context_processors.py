from django.conf import settings

def labels(request):
    """
    Inject LABELS from settings into templates so you can use:
      {{ labels.form_title }}, {{ labels.field_1_label }}, etc.
    """
    return {
        'labels': getattr(settings, 'LABELS', {})
    }
