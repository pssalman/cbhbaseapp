(function () {
  'use strict';

  angular
    .module('cbhbaseapp.authentication', [
      'cbhbaseapp.authentication.controllers',
      'cbhbaseapp.authentication.services'
    ]);

  angular
    .module('cbhbaseapp.authentication.controllers', []);

  angular
    .module('cbhbaseapp.authentication.services', ['ngCookies']);
})();
