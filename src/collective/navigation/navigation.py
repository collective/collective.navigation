# -*- coding: utf-8 -*-
from datetime import datetime
from plone.memoize import ram
from plone.tiles import Tile
from zope.component.hooks import getSite

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


class NavigationTile(Tile):

    _navtree = None
    _navtree_path = None
    _navtree_context = None

    @property
    def navtree_context(self):
        if self._navtree_context is None:
            self._navtree_context = getSite()
        return self._navtree_context

    @property
    def navtree_path(self):
        if self._navtree_path is None:
            self._navtree_path = '/'.join(
                self.navtree_context.getPhysicalPath()
            )
        return self._navtree_path

    @navtree_path.setter
    def navtree_path(self, value):
        self.navtree_path = value

    @property
    def navtree_depth(self):
        return 3

    @property
    def navtree(self):

        if self._navtree is not None:
            return self._navtree

        dt1 = datetime.now()
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

        print('navtree: %s' % (datetime.now() - dt1).total_seconds())
        return ret

    def build_tree(self, path):

        out = u''
        for it in self.navtree.get(path, []):
            out += u'<li class="{id} state-{review_state}">'.format(
                id=it['id'],
                review_state=it['review_state']
            )
            out += u'<a href="{url}">{title}</a>'.format(
                url=it['url'],
                title=it['title']
            )
            out += self.build_tree(path + '/' + it['id'])
            out += u'</li>'

        out = u'<ul>' + out + u'</ul>' if out else ''
        return out

    @ram.cache(_result_cachekey)
    def result(self):
        return self.build_tree(self.navtree_path)


"""
this navigation tile vs webcouturier.dropdownmenu / global_sections viewlet

Typical values:

navigation tile, cold: 0.22s
navigation tile, warm: 0.02s - 0.05s
navigation tile, cached: 0.01s

global_section tile, cold: 7s
global_section tile, warm: 0.5s - 0.8s

"""