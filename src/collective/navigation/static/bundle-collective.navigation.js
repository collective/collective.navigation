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
