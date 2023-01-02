from django.db import models


class Menu(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, null=False, blank=False)
    name = models.CharField(verbose_name='MenuName', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(verbose_name='MenuItemName', max_length=50, blank=False, null=False)
    url = models.URLField(max_length=50, verbose_name='MenuItemUrl', blank=False, null=False)
    parent = models.ForeignKey('self', verbose_name='MenuItemParent', null=True, blank=True,
                               on_delete=models.DO_NOTHING)
    menu = models.ForeignKey(Menu, blank=False, null=True, verbose_name='BelongsToMenu', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
