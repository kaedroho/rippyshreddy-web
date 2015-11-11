from django.db import models

from wagtail.wagtailcore.models import Page


class MapPage(Page):
    parent_page_types = ['MapHomePage']


class MapHomePage(Page):
    subpage_types = ['MapPage']
