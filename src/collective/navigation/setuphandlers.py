# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api
import logging

logger = logging.getLogger('collective.navigation')


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'excellent.site:uninstall',
        ]


def post_install(context):
    """Post install script"""

    wanted_indexes = (
        ('exclude_from_nav', 'BooleanIndex'),
    )
    add_catalog_indexes(context, logger=logger, wanted=wanted_indexes)


def add_catalog_indexes(context, logger=None, wanted=None):
    """Method to add our wanted indexes to the portal_catalog.
    """
    catalog = api.portal.get_tool('portal_catalog')
    indexes = catalog.indexes()
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info('Added %s for field %s.', meta_type, name)
    if len(indexables) > 0:
        logger.info('Indexing new indexes %s.', ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
