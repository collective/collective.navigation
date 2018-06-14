# -*- coding: utf-8 -*-
from plone.app.layout.navigation.root import getNavigationRoot
from plone.app.layout.viewlets import common
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.memoize import ram
from plone.tiles import Tile
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility

import plone.api


def _result_cachekey(fun, self):
    cachekey = ' '.join((
        self.navtree_path,
        str(self.navtree_depth),
        plone.api.portal.get_current_language(),
        ' '.join(plone.api.user.get_roles()),
        str(plone.api.portal.get_tool('portal_catalog').getCounter()),
    ))
    return cachekey


class NavigationTile(Tile, common.GlobalSectionsViewlet):

    _navtree = None
    _navtree_path = None
    _navtree_context = None

    @property
    def navtree_path(self):
        if self._navtree_path is None:
            self._navtree_path = getNavigationRoot(self.context)
        return self._navtree_path

    @property
    def navtree_depth(self):
        return 2

    @property
    def enableDesc(self):
        return True

    @property
    def navtree(self):

        if self._navtree is not None:
            return self._navtree

        types = plone.api.portal.get_registry_record('plone.displayed_types')
        lang_current = plone.api.portal.get_current_language()

        query = {
            'path': {'query': self.navtree_path, 'depth': self.navtree_depth},
            'portal_type': {'query': types},
            'exclude_from_nav': False,
            'Language': lang_current,
            'sort_on': 'getObjPositionInParent',
        }
        res = plone.api.content.find(**query)

        ret = {}
        for it in res:
            pathkey = '/'.join(it.getPath().split('/')[:-1])
            entry = {
                'id': it.id,
                'url': it.getURL(),
                'title': it.Title,
                'review_state': it.review_state,
            }
            if pathkey in ret:
                ret[pathkey].append(entry)
            else:
                ret[pathkey] = [entry]

        self._navtree = ret
        return ret

    # Template based recursive tree building
    recurse = ViewPageTemplateFile('navigation_recurse.pt')

    def build_tree(self, path, first_run=True):
        """Non-template based recursive tree building.
        3-4 times faster than template based.
        See figures below.
        """
        normalizer = getUtility(IIDNormalizer)
        out = u''
        for it in self.navtree.get(path, []):
            sub = self.build_tree(path + '/' + it['id'], first_run=False)

            out += u'<li class="{id}{has_sub_class}">'.format(
                id=normalizer.normalize(it['id']),
                has_sub_class=' has_subtree' if sub else '',
            )
            out += u'<a href="{url}" class="state-{review_state}">{title}</a>'.format(  # noqa
                url=it['url'],
                review_state=it['review_state'],
                title=it['title'],
            )
            out += sub
            out += u'</li>'

        if not first_run:
            out = u'<ul>' + out + u'</ul>' if out else ''

        return out

    # @ram.cache(_result_cachekey)
    def __call__(self, *args, **kwargs):
        return super(NavigationTile, self).__call__(*args, **kwargs)


"""
this navigation tile vs webcouturier.dropdownmenu / global_sections viewlet

Typical values:

Navigation tile, non-template based tree building:
cold: 0.22s
warm: 0.02s - 0.05s
cached: 0.01s - 0.03s

Navigation tile, template based
cold: 0.22s
warm: 0.10s - 0.13s
cached: 0.01s - 0.03s

recursive global_sections tile (webcouturier.dropdownmenu):
cold: 7s
warm: 0.5s - 0.8s
"""
