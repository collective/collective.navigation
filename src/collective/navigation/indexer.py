# -*- coding: utf-8 -*-
from plone.indexer.decorator import indexer
from zope.interface import Interface


@indexer(Interface)
def exclude_from_nav_indexer(obj):
    ret = bool(getattr(obj, 'exclude_from_nav', False))
    return ret
