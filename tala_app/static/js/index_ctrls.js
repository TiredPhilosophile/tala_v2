		var app = angular.module('myApp', ['ui.router'])

		app.config(function($interpolateProvider) {
		  	$interpolateProvider.startSymbol('[[').endSymbol(']]')
		})

		app.config( ['$anchorScrollProvider', 
			function($anchorScrollProvider) {
					$anchorScrollProvider.disableAutoScrolling();
			}]
		);

		/* ---------- Routing ---------- */

		app.config(function($stateProvider, $urlRouterProvider) {
			
			$urlRouterProvider.otherwise('/home')
			
			$stateProvider
				
				.state('home', {
					url: '/home',
					templateUrl: 'page/home.html',
				})
			
				.state('search', {
					url: '/search',
					templateUrl: 'page/search.html',
				})
			
				.state('testing', {
					url: '/testing',
					templateUrl: 'page/testing.html',
				})
			
					.state('testing.nest1', {
						url: '/nest1',
						templateUrl: 'page/nest1.html',
						controller: function($scope) {
							$scope.bird = "bluejay";
						},
						
					});
			
							 
		}); // ./routing
		
		/* ---------- Controllers ---------- */

		app.controller('myCtrl', function($scope) {
		    $scope.names = [
		        {name:'Jani',country:'Norway'},
		        {name:'Hege',country:'Sweden'},
		        {name:'Kai',country:'Denmark'}
		    ]
		    $scope.firstName = 'James'
		    $scope.lastName  = 'Bond'
		    $scope.myVar = false
		    $scope.toggle = function() {
		        $scope.myVar = !$scope.myVar; // sets myVar to opposite of itself
		    }
		    $scope.fullName = function() {
		    	return $scope.firstName + " " + $scope.lastName 
		    }
		});

		app.controller('pullCtrl', function($scope, $http) {
			// link is provided directly from the DOM
			// the get_data(link) function is called.
			$scope.get_data = function(link) {
		    $http.get(link).success(function(response) { 
		    	// returns array of users
		    	$scope.page_data = response.page_data;
		    	$scope.userprofile = response.userprofile;
		    });
		  }

		});

		app.controller('validateCtrl', function($scope) {
		    $scope.user = 'John Doe';
		    $scope.email = 'john.doe@gmail.com';
		});

		app.controller('formCtrl', function($scope, $http) {
				$scope.something = 'a thing';
				$scope.formData = {};

		// process the form
		$scope.processForm = function() {

			var csrftoken = $.cookie('csrftoken'); // get csrf token
			console.log(csrftoken)

			// although this is a nice way of doing it, you might just want $.ajaxSubmit or something as that works
			// well already with django submit.

			/* $.ajaxSubmit(url)
				.success(function() {
					// do stuff
				})
				.fail(function(response) {
					$scope.error = response
				})
			*/

		  $http({
		  method  : 'POST',
		  url     : 'api/process_form',
		  data    : $.param($scope.formData),  // pass in data as strings
		  headers : { 'Content-Type': 'application/x-www-form-urlencoded' } 
		 })
		  .success(function(data) {
		    console.log(data);

		    if (!data.success) {
		      // if not successful, bind errors to error variables
		      $scope.errorName = data.errors.name;
		      $scope.errorSuperhero = data.errors.superheroAlias;
		    } else {
		      // if successful, bind success message to message
		      $scope.message = data.message;
		    }
		  });
		};

		}) // ./validateCtrl

		// learn more about forms here: https://scotch.io/tutorials/angularjs-form-validation
		
		
		
		
		
		