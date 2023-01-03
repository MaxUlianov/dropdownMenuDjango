from django.shortcuts import render


def page(request, active=None, *args, **kwargs):

    return render(request, 'page.html', {'active': active})
