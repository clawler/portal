/**
 *
 */
export function ddGoogleDriveListing() {
    'ngInject';
    return {
      restrict: 'E',
      transclude: true,
      replace: true,
      template: require('../html/directives/dd-googledrive-listing.html'),
      scope: {
        browser: '=',
        onBrowse: '&',
        onSelect: '&',
        onDetail: '&'
      }
    };
  }
