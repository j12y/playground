angular.module('app')
.config(function($routeProvider) {
    $routeProvider
    .when('/', { controller: 'PostsCtrl', templateUrl: 'posts.html'})
    .when('/register', { controller: 'RegisterCtrl', templateUrl: 'register.html'})
    .when('/login', { controller: 'LoginCtrl', templateUrl: 'login.html'})

    // $locationProvider.html5Mode(true);
    // Then could remove # from urls, then changing url for express from / to *
});
