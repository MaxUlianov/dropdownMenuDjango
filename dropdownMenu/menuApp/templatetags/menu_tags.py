from django import template
from menuApp.models import MenuItem, Menu
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(menu=Menu.objects.filter(name=menu_name)[0].id)
    # active = context['active']

    menu = [f'<li><a href={item.url}>{item.name}</a></li>' for item in menu_items]
    print(menu)
    menu_html = f'<ul>\n{"".join(menu)}\n</ul>'
    return mark_safe(menu_html)
