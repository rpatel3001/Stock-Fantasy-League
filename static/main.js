var uid = -1;
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
/*stk.service('SharedData', function () {

})*/

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
stk.controller('UserController', ['$scope', '$http', '$rootScope', '$routeParams', function ($scope, $http, $rootScope, $routeParams) {
    $scope.paramuid = $routeParams.uid;
    $scope.uid = uid;
    $scope.startBal = null;
    $scope.duration = null;
    $scope.leaguename = null;
    $scope.description = null;
    $scope.data = {};
    $scope.leaguesView = false;
    $scope.navbarHeader = "Leagues";
    var req = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + $scope.paramuid
    };
    $http(req).then(function (response) {
        $scope.user = response.data; //unwrapped json
        $scope.navbarHeader = "Leagues with " + $scope.user.username;
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

stk.controller('PlayerController', function ($scope, $http, $routeParams) {
    $scope.lid = $routeParams.lid;
    $scope.pid = $routeParams.pid;
    $scope.player = null;
    $scope.league = null;
    var reqLeague = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/league/' + $scope.lid
    };
    var reqPlayer = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/player/' + $scope.pid
    };
    var reqStocks = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/stock_data/top/1000'
    };
    $http(reqLeague).then(function (response) {
        $scope.league = JSON.parse(response.data).Leagues[0];
        //wrapped json
        $http(reqPlayer).then(function (response) {
            $scope.player = response.data[0];
            if ($scope.player.holdings == null) {
                $scope.player.holdings = {
                    'holdings': []
                }
            }
            if ($scope.player.availbalance == null) {
                $scope.player.availbalance = $scope.league.startbal;
            }
            if ($scope.player.translog == null) {
                $scope.player.translog = {
                    'translog': []
                };
            }
            //update sholding with server
            $http(reqStocks).then(function (response) {
                $scope.topStocks = response.data.stocks;
            })
        }, function (response) {
            console.log('Failing getting league info!');
        });
    }, function (response) {
        console.log('Failing getting league info!');
    });


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

    function onSignIn(googleUser) {
        var profile = googleUser.getBasicProfile();
        var id_token = googleUser.getAuthResponse().id_token;
        var req = {
            method: 'POST',
            url: 'http://stock-fantasy-league.herokuapp.com/api/user',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data: $.param({
                email: profile.getEmail(),
                username: profile.getName(),
                imageurl: profile.getImageUrl(),
                token: id_token
            })
        }
        $http(req).then(function loginSuccess(response) {
            uid = response.data.uid;
            var scope = angular.element(document).scope();
            scope.$apply(function () {
                scope.uid = uid;
            });
            var scope2 = angular.element($("#mainNavbar")).scope();
            scope2.$apply(function () {
                scope2.uid = uid;
                scope2.signedIn = true;
                scope2.username = profile.getName();
                scope2.imageurl = profile.getImageUrl();
            });
        }, function loginFailure(response) {
            console.log('Failing to log in!');
        });
    }
    window.onSignIn = onSignIn;
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
stk.controller('LeagueListController', function ($scope, $http, $rootScope, $location) {
    $scope.leaguesView = true; //need to make an official watch in another controller
    $scope.navbarHeader = "Leagues";
    var reqLeagues = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/league'
    };
    $scope.data = null;
    $http(reqLeagues).then(function loginSuccess(response) {
        $scope.data = JSON.parse(response.data);
    }, function loginFailure(response) {
        console.log('Failing getting leagues info!');
    });
    $scope.joinLeague = function (selected_lid) {
        if (uid > 0) {
            var reqJoinLeague = {
                method: 'POST',
                url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + uid + '/joinLeague',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data: $.param({
                    lid: selected_lid
                })
            };
            $http(reqJoinLeague).then(function (response) {
                //need to update this to change button and reload leagues
                $http(reqLeagues).then(function loginSuccess(response) {
                    $scope.data = JSON.parse(response.data);
                }, function loginFailure(response) {
                    console.log('Failing getting leagues info!');
                });
                $location.path("/league/" + selected_lid + "/player/" + response.data[response.data.length - 1].pid)
                //console.log(response.pid); //unwrapped json
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

function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    var scope = angular.element($("#mainNavbar")).scope();
    auth2.signOut().then(function () {
        uid = -1;
        scope.$apply(function () {
            scope.uid = -1;
            scope.username = '';
            scope.imageurl = '';
            scope.signedIn = false;
        });
        console.log('User signed out.');
    });
}
