var stk = angular.module('Stock Fantasy League', ["ngRoute"]);
stk.config(function ($routeProvider, $locationProvider) {
    $routeProvider.when("/", {
        templateUrl: "homepage_parts.html"
    }).when("/user", {
        templateUrl: 'user_list.html'
        /*,
                controller: 'UserListController'*/
    }).when("/user/:uid", {
        templateUrl: 'user_parts.html'
        /*,
                controller: 'UserInfoController'*/
    }).when("/league", {
        templateUrl: 'league_list.html'
        /*,
                controller: 'LeagueListController'*/
    }).when("/league/:lid", {
        templateUrl: 'league_parts.html'
        /*,
                controller: 'LeagueController'*/
    }).when("/dashboard", {
        templateUrl: 'dashboard_parts.html'
        /*,
                controller: 'DashboardController'*/
    });
    //$locationProvider.html5Mode(true);
});
stk.controller('LoginController', ['$scope', function ($scope) {
    $scope.showLogIn = false;
    $scope.message = 'Sign In';
    //x button
}]);

stk.controller('LeagueController', ['$scope', '$http', '$routeParams', function ($scope, $http, $routeParams) {
    $scope.lid = $routeParams.lid;
    var req = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/league/' + $scope.lid
    };
    $scope.data = null;
    $http(req).then(function loginSuccess(response) {
        $scope.data = JSON.parse(response.data);
        $scope.league = $scope.data.Leagues[0]; //wrpped json
    }, function loginFailure(response) {
        console.log('Failing getting league info!');
    });
}]);
stk.controller('UserController', ['$scope', '$http', '$routeParams', function ($scope, $http, $routeParams) {
    $scope.uid = $routeParams.uid;
    var req = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + $scope.uid
    };
    $scope.data = null;
    $http(req).then(function loginSuccess(response) {
        $scope.user = response.data; //unwrapped json
        $scope.createLeague();
    }, function loginFailure(response) {
        console.log('Failing getting league info!');
    });
    $scope.createLeague = function () {
        var req = {
            method: 'POST',
            url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + $scope.uid,
            data: $.param({
                startBal: 10000,
                duration: Date.now(),
                leagueName: "angulartestLeague1",
                description: "test"
            })
        };
        $http(req).then(function loginSuccess(response) {
            console.log(response.data); //unwrapped json
        }, function loginFailure(response) {
            console.log('Failing getting league info!');
        });
    };
}]);
stk.controller('DashboardController', function ($scope, $http) {
    /*$http.get('http://stock-fantasy-league.herokuapp.com/api/user').then(function (response) {
        $scope.user = response.data;
    });*/
    $scope.user = {
        "uid": 1,
        "lids": [1, 2314, 234],
        "pid": null,
        "friends": null,
        "email": "x@x.com",
        "messages": null,
        "notifications": null,
        "username": "brian",
        "password": "pass",
        "description": 'test',
        joinDate: '12/27/16'
    }; // change pids and lids to leagues and users
});

stk.controller('PlayerController', function ($scope, $http) {
    $scope.player = {
        league: {
            leagueName: 'test',
            description: 'test league',
            img: 'url'
        },
        ranking: 10,
        holdingsValue: 4321.65,
        holdings: [
            {
                stockTicker: "AAPL",
                name: "Apple, Inc.",
                numberShares: 10,
                sharePrice: 197.65
            },
            {
                stockTicker: "GOOG",
                name: "Alphabet, Inc.",
                numberShares: 10,
                sharePrice: 1097.65
            }
            , {
                stockTicker: "AMZN",
                name: "Amazon, Inc.",
                numberShares: 10,
                sharePrice: 1597.65
            }
            ]

    };
});
stk.controller('NavbarController', ['$scope', function ($scope) {
    $scope.signedIn = false;
    $scope.username = '';
    $scope.imageurl = '';
    $scope.navItems = {
        links: [{
            name: 'Users',
            command: 'ViewUsers',
            href: '#!/user'
        }, {
            name: 'Leagues',
            command: 'ViewLeagues',
            href: '#!/league'
        }]
    };
}]);

stk.controller('PageManagerController', ['$scope', '$rootScope', '$location', function ($scope, $rootScope, $location) {
    $scope.title = "Stock Fanatasy League";
}]);
stk.controller('UserListController', function ($scope, $http) {
    var req = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/user'
    };
    $scope.data = null;
    $http(req).then(function loginSuccess(response) {
        $scope.data = JSON.parse(response.data);
    }, function loginFailure(response) {
        console.log('Failing getting users info!');
    });
});
stk.controller('LeagueListController', function ($scope, $http) {
    var req = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/league'
    };
    $scope.data = null;
    $http(req).then(function loginSuccess(response) {
        $scope.data = JSON.parse(response.data);
    }, function loginFailure(response) {
        console.log('Failing getting leagues info!');
    });
});
