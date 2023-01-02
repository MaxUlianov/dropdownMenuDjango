from django.shortcuts import render


def page(request, menus=None, active=None, *args, **kwargs):
    # query = request.get('menus')
    query = menus
    list = request.GET.get('list_menu')

    return render(request, 'page.html', {'query': query, 'active': active, 'list': list})
