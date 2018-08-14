define('collective.navigation',[
    'jquery',
    'pat-base'
], function($, Base) {

    var Navigation = Base.extend({
        name: 'collective.navigation',
        trigger: '.pat-navigation',
        parser: 'mockup',

        init: function() {
            var href = window.location.href;
            $('a', this.$el).each(function () {
                if (href.indexOf(this.href) !== -1) {
                    var parent = $(this).parent();

                    // check the input-openers within the path
                    var check = parent.find('> input');
                    if (check.length) {
                        check[0].checked = true;
                    }

                    // set "inPath" to all nav items which are within the current path
                    parent.addClass('inPath');

                    // set "current" to the current selected nav item, if it is in the navigation structure.
                    if (href == this.href) {
                        parent.addClass('current');
                    }
                }
            });
        }

    });

    return Navigation;
});

require([
  'jquery',
  'pat-registry',
  // patterns
  'collective.navigation'
], function($, registry) {
  // initialize only if we are in top frame
  if (window.parent === window) {
    $(document).ready(function() {
      if (!registry.initialized) {
        registry.init();
      }
    });
  }
});

define("/home/_thet/data/dev/agitator/collective.navigation/src/collective/navigation/static/bundle-collective.navigation.js", function(){});

