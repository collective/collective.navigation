# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.i18nmessageid import MessageFactory
from zope.interface import implementer


_ = MessageFactory('collective.navigation')


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'collective.navigation:uninstall',
        ]
