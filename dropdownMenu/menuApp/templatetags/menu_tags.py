from django import template
from menuApp.models import MenuItem, Menu
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(menu=Menu.objects.filter(name=menu_name)[0].id)
    active = context['active']

    active_item = menu_items.filter(name=active)[0]
    under_active = menu_items.filter(parent=active_item)
    if len(under_active) > 0:
        active_item = under_active[0]

    active_list = above_active(menu_items, active_item)

    return mark_safe(active_list)


def make_li(item):
    return f'<li><a href={item.url}>{item.name}</a></li>'


def make_list(items, string, parent_item):
    l = [make_li(item) if not item == parent_item else f'{make_li(item)}{string}' for item in items]
    l_html = f'<ul>\n{"".join(l)}\n</ul>'
    return l_html


def above_active(items, current, string=''):
    if current is not None:
        ls = items.filter(parent=current.parent)
        string = make_list(ls, string, current)
        if len(ls) > 0:
            current = ls[0].parent
            string = above_active(items, current, string)
    return string
