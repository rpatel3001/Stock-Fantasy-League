var stk = angular.module('Stock Fantasy League', ["ngRoute"]);
stk.config(function ($routeProvider, $locationProvider, $rootScope) {
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
        templateUrl: 'league_list.html',
        controller: 'LeagueListController'
    }).when("/league/:lid", {
        templateUrl: 'league_parts.html'
        /*,
                controller: 'LeagueController'*/
    }).when("/league/:lid/player/:pid", {
        templateUrl: 'player_parts.html'
/*,
                controller: 'LeagueController'*/
    }).when("/about-us", {
        templateUrl: 'about_us.html'
        /*,
                controller: 'DashboardController'*/
    }).when("/vip", {
        templateUrl: 'vip.html'
        /*,
                controller: 'UserListController'*/
    });
    //$locationProvider.html5Mode(true);
});
stk.service('SharedData',function(){
    
})
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
    $http(req).then(function (response) {
        $scope.data = JSON.parse(response.data);
        $scope.league = $scope.data.Leagues[0]; //wrapped json
    }, function (response) {
        console.log('Failing getting league info!');
    });
}]);
stk.controller('UserController', ['$scope', '$http', '$routeParams', function ($scope, $http, $routeParams) {
    $scope.uid = $routeParams.uid;
    $scope.signedinuid = uid;
    $scope.startBal = null;
    $scope.duration = null;
    $scope.leaguename = null;
    $scope.description = null;
    $scope.data = {};
    $scope.leaguesView = false;
    var req = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + $scope.uid
    };
    $http(req).then(function (response) {
        $scope.user = response.data; //unwrapped json
        $scope.getUserLeagues();
    }, function (response) {
        console.log('Failing getting league info!');
    });
    $scope.createLeague = function () {
        if ($scope.signedinuid == $scope.uid) {
            var req = {
                method: 'POST',
                url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + $scope.uid,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data: $.param({
                    startBal: $scope.startBal,
                    duration: new Date($scope.duration).getTime(),
                    leagueName: $scope.leaguename,
                    description: $scope.description
                })
            };
            $http(req).then(function (response) {
                console.log(response.data); //unwrapped json
                $scope.startBal = null;
                $scope.duration = null;
                $scope.leaguename = null;
                $scope.description = null;
                $scope.getUserLeagues();
            }, function (response) {
                console.log('Failing getting league info!');
            });
        };
    };
    $scope.getUserLeagues = function () {
        if ($scope.user.lid != null) {
            var req = {
                method: 'GET',
                url: 'http://stock-fantasy-league.herokuapp.com/api/league/multiple',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                params: {
                    lidarray: $scope.user.lid.join(',')
                }
            };
            $http(req).then(function (response) {
                $scope.data.Leagues = response.data;
                $scope.user.leagues = response.data //unwrapped json
            }, function (response) {
                console.log('Failing getting league info!');
            });
        }
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

stk.controller('PlayerController', function ($scope, $http, $route) {
    $scope.lid = $routeParams.lid;
    $scope.pid = $routeParams.pid;


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
        $scope.organizedData = createGroupings($scope.data.Users, 3);
    }, function loginFailure(response) {
        console.log('Failing getting users info!');
    });
});
stk.controller('LeagueListController', function ($scope, $http, $rootScope) {
    $scope.leaguesView = true;
    $scope.uid = $rootScope.uid; //need to make an official watch in another controller
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
    $scope.joinLeague = function (selected_lid) {
        if (uid > 0) {
            var req = {
                method: 'POST',
                url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + uid + '/joinLeague',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data: $.param({
                    lid: selected_lid
                })
            };
            $http(req).then(function (response) {
                console.log(response.pid); //unwrapped json
            }, function (response) {
                console.log('Failing to join league!');
            });
        }
    };
});

var createGroupings = function (original, numCols) {
    var rows = [];
    for (i = 0; i < original.length; i += numCols) {
        rows.push(original.slice(i, i + numCols));
    }
    return rows;
};
