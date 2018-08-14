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
                    $(this).parent().addClass('inPath');
                    if (href == this.href) {
                        $(this).parent().addClass('current');
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

