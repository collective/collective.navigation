# -*- coding: utf-8 -*-
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.theme.interfaces import IDefaultPloneLayer
from collective.navigation import _
from zope import schema
from zope.interface import Interface


class INavigationLayer(IDefaultPloneLayer):
    """Marker interface that defines a browser layer."""


class INavigationConfiguration(Interface):
    """This interface defines the configlet for dropdown menus."""

    navtree_depth = schema.Int(
        title=_(u'label_navtree_depth', default=u'Depth of dropdown menus'),
        description=_(u'help_navtree_depth',
                      default=u'How many levels to list after the top level.'),
        required=True,
        default=3
    )

    enable_caching = schema.Bool(
        title=_(u'label_enable_caching', default=u'Enable caching'),
        description=_(
            u'help_enable_caching',
            default=(u'WARNING! This is an experimental feature. '
                     u'This is using RAM to store cached template for '
                     u'dropdown menus. Technically every user and '
                     u'every visited section gets its own instance '
                     u"in the ram.cache. Don't enable this if you don't "
                     u'know what this is about. Disable this option '
                     u'if you get unexpected behavior of your global tabs.')),
        default=False,
        required=False
    )

    enable_parent_clickable = schema.Bool(
        title=_(u'label_enable_parent_clickable',
                default=u'Enable clicking menu items that have children'),
        description=_(
            u'help_enable_parent_clickable',
            default=(u'With this option enabled, every menu item is '
                     u'clickable. With this option disabled, an item is only '
                     u'clickable when it is not a parent so it has no '
                     u'children.')),
        default=True,
        required=False
    )

    enable_desc = schema.Bool(
        title=_(u'label_enable_desc',
                default=u'Show Description'),
        description=_(
            u'help_desc',
            default=(u'With this option enabled, description is also shown.')),
        default=False,
        required=False
    )

    enable_images = schema.Bool(
        title=_(u'label_enable_img',
                default=u'Show Images'),
        description=_(
            u'help_img',
            default=(u'With this option enabled, images are shown.')),
        default=False,
        required=False
    )

    img_size = schema.Choice(
        title=_(u'label_size', default=u'Size'),
        description=_(u'description_size', default=u'The size of the image'),
        default='icon',
        vocabulary='plone.app.vocabularies.ImagesScales',
    )
