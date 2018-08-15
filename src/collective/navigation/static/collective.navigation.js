define([
    'jquery',
    'pat-base'
], function($, Base) {

    var Navigation = Base.extend({
        name: 'collective.navigation',
        trigger: '.pat-navigation',
        parser: 'mockup',

        init: function() {
            var smallDevice = false
            var href = document.querySelector('head link[rel="canonical"]').href || window.location.href;
            $('a', this.$el).each(function () {
                if (href.indexOf(this.href) !== -1) {
                    var parent = $(this).parent();

                    if (smallDevice) {  // only check checkboxes if it's a small device
                        // check the input-openers within the path
                        var check = parent.find('> input');
                        if (check.length) {
                            check[0].checked = true;
                        }
                    }

                    // set "inPath" to all nav items which are within the current path
                    parent.addClass('inPath');

                    // set "current" to the current selected nav item, if it is in the navigation structure.
                    if (href === this.href) {
                        parent.addClass('current');
                    }
                }
            });
        }


    });

     function myFunction(smallDevice) {
        if (smallDevice.matches) { // If media query matches
            document.body.style.backgroundColor = "yellow";
        } else {
            document.body.style.backgroundColor = "pink";
        }
    }

    var smallDevice = window.matchMedia("(max-width: 767px)")
    myFunction(smallDevice) // Call listener function at run time
    smallDevice.addListener(myFunction) // Attach listener function on state changes

    return Navigation;
});
