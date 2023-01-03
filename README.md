## Dropdown menu

Django app среализацией древовидного меню:
* меню и элементы добавляются / редактируются через Django admin
* на странице отрисовавается через template tag:
  
    {% load menu_tags %}
    {% draw_menu 'name_of_menu' %}
  
* активный элемент (выделенный в списке) определяется по url:

> URL: '<host-url>/menu/<имя-активного-элемента-в-меню>'
 
* элементы над выделенным и первый уровень под выделенным разворачиваются
* элементы содержат URL, при нажатии на элемент происходит переход (URL добавляется в Django admin)

Директория template tag:

> dropdownMenu/menuApp/templatetags/menu_tags.py