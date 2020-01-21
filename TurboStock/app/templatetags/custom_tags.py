from django import template

register = template.Library()

from app.authentication import authentication


@register.simple_tag
def has_permission_on_item(user, item):
    return authentication.has_permission_on_item(user, item)
