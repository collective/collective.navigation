define([
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
