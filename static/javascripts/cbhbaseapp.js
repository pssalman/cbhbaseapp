angular
  .module('cbhbaseapp', [
      'cbhbaseapp.config',
      'cbhbaseapp.routes',
      'cbhbaseapp.authentication',
      'cbhbaseapp.layout',
      'cbhbaseapp.departments',
      'cbhbaseapp.utils'
  ]);

angular
  .module('cbhbaseapp.config', []);

angular
  .module('cbhbaseapp.routes', ['ngRoute']);

angular
  .module('cbhbaseapp')
  .run(run);

run.$inject = ['$http'];

/**
* @name run
* @desc Update xsrf $http headers to align with Django's defaults
*/
function run($http) {
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
}
