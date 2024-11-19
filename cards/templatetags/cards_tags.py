from django import template
from django.db.models import Count
from cards.models import UserCardProgress

register = template.Library()

@register.inclusion_tag("cards/box_links.html")
def boxes_as_links():
    """
    Returns box counts for the current user's cards
    """
    boxes = UserCardProgress.objects.values('box_level').annotate(
        card_count=Count('id')
    ).order_by('box_level')
    
    return {"boxes": [
        {
            "number": box["box_level"],
            "card_count": box["card_count"],
        }
        for box in boxes
    ]}

@register.filter
def ordinal(value):
    try:
        value = int(value)
        if 10 <= value % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(value % 10, 'th')
        return f"{value}{suffix}"
    except (TypeError, ValueError):
        return value

@register.filter
def get_item(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None

@register.filter
def multiply(value, arg):
    return float(value) * float(arg)

@register.filter
def to_int(value):
    return int(value)