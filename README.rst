=====================
collective.navigation
=====================

DON'T USE THIS PACKAGE, UPGRADE TO PLONE 5.2

This package is now just a proof of concept for the dropdown menus in Plone 5.2
A huge amount of improvements have gone into the actual implemention.


Features
--------

- plone.tiles based navigation
- Focus on speed of execution
- Build-in effecient caching
- ``exclude_from_nav`` indexer
- Renders on the navigation root object and sets ``inPath`` and ``current`` CSS classes in JavaScript, which allows efficient caching.
- Configurable navigation start path
- Configurable navigation depth


Performance comparion
---------------------

The values here were measured on a laptop with a specific setup and are not representational for other setups.

Navigation depth: 3
Navigation structure with 10 menu items and 5 sub- + subsub-menu items.


collective.navigation tile, non-template based tree building
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- cold: 0.22s
- warm: 0.02s - 0.05s
- cached: 0.01s - 0.03s

collective.navigation tile with recursive page template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- cold: 0.22s
- warm: 0.10s - 0.13s
- cached: 0.01s - 0.03s

webcouturier.dropdownmenu with recursive global_sections tile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- cold: 7s
- warm: 0.5s - 0.8s

TODO
----

- JSON data structure for client side rendering.
- Activate cache (had problems with a multi-site lineage setup, where the generated URLs pointed to another site)
- Use options from controlpanel

License
-------

The project is licensed under the GPLv2.
