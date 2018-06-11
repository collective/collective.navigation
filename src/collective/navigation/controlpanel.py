# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from Products.CMFPlone import PloneMessageFactory as _
from collective.navigation.interfaces import INavigationConfiguration


class NavigationControlPanelForm(RegistryEditForm):

    id = 'NavigationControlPanel'
    schema = INavigationConfiguration
    schema_prefix = (
        'collective.navigation.interfaces.INavigationConfiguration'
    )

    label = _(
        u'A dropdown menu configuration.',
        default=u'A dropdown menu configuration.'
    )
    description = _(
        u'Settings to configure dropdown menus for global navigation.',
        default=u'Settings to configure dropdown menus for global navigation.'
    )


class NavigationControlPanel(ControlPanelFormWrapper):
    form = NavigationControlPanelForm

