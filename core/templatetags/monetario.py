from django import template
from core.currency import format_brl

register = template.Library()
register.filter("brl", format_brl)
