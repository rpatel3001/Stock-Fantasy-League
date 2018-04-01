var uid = -1;
$http = angular.injector(["ng"]).get("$http");
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
    }).when("/tutorial", {
        templateUrl: 'tutorial.html'
    }).when("/privacy", {
        templateUrl: 'privacy.html'
    }).when("/terms", {
        templateUrl: 'terms.html'
    }).when("/integration_testing", {
        templateUrl: 'integration_testing.html'
    });
});
/*stk.service('SharedData', function () {

})*/
stk.controller('LeagueController', ['$scope', '$http', '$routeParams', function ($scope, $http, $routeParams) {
    if ($routeParams.lid != undefined) {
        $scope.lid = $routeParams.lid;
    } else {
        $scope.lid = 1;
    }
    var req = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/league/' + $scope.lid
    };
    var reqPlayers = {
        method: 'GET',
        url: '/api/league/' + $scope.lid + '/everything'
    };
    $scope.data = null;
    $http(req).then(function (response) {
        $scope.league = JSON.parse(response.data).Leagues[0]; //wrapped json
        $http(reqPlayers).then(function (response) {
            $scope.players = response.data;
        }, function (repsonse) {
            console.log(response);
        })
    }, function (response) {
        console.log('Failing getting league info!');
    });
}]);
stk.controller('UserController', ['$scope', '$http', '$rootScope', '$routeParams', '$route', function ($scope, $http, $rootScope, $routeParams, $route) {
    if ($scope.paramuid == undefined) {
        $scope.paramuid = 1;
    } else {
        $scope.paramuid = $routeParams.uid;
    }
    $scope.startBal = null;
    $scope.intStartBal = 10000;
    $scope.duration = null;
    $scope.intDuration = new Date("01/01/2030");
    $scope.leaguename = null;
    $scope.intGenerateRandomLeagueName = function () {
        return 'Test League - ' + Math.floor(1e12 * Math.random());
    }
    $scope.intLeaguename = $scope.intGenerateRandomLeagueName();
    $scope.description = null;
    $scope.intDescription = "Description for Integration Test League: " + $scope.intLeaguename + ".";
    $scope.leaguesView = false;
    $scope.navbarHeader = "Leagues";
    var req = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + $scope.paramuid
    };
    $http(req).then(function (response) {
        $scope.user = response.data;
        //unwrappedjson
        $scope.navbarHeader = "Leagues with " + $scope.user.username;
        $scope.getUserLeagues();
        $scope.updateUser();
    }, function (response) {
        console.log('Failing getting league info!');
    });
    $scope.createLeague = function () {
        if ($scope.paramuid == $scope.uid) { // could use user.uid as well
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
                $scope.user.lid.push(response.data[response.data.length - 1].lid);
                $route.reload();
            }, function (response) {
                console.log('Failing getting league info!');
            });
        };
    };
    $scope.intTestCreateLeague = function () {
        if ($scope.uid > 0) { // test check not as accurate 
            var req = {
                method: 'POST',
                url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + $scope.uid,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data: $.param({
                    startBal: $scope.intStartBal,
                    duration: $scope.intDuration.getTime(),
                    leagueName: $scope.intLeaguename,
                    description: $scope.intDescription
                })
            };
            $http(req).then(function (response) {
                console.log(response.data); //unwrapped json
                $scope.intStartBal = null;
                $scope.intDuration = null;
                $scope.intLeaguename = $scope.intGenerateRandomLeagueName();
                $scope.intDescription = null;
                $scope.user.lid.push(response.data[response.data.length - 1].lid);
                $route.reload();
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
                $scope.leagues = response.data;
                //$scope.user.leagues = response.data; //unwrapped json
            }, function (response) {
                console.log('Failing getting league info!');
            });
        }
    };
    $scope.updateUser = function () {
        var reqUpdatePlayer = {
            method: 'POST',
            url: 'http://stock-fantasy-league.herokuapp.com/api/user/' +
                $scope.user.uid + '/update',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data: $.param({
                'update': JSON.stringify($scope.user)
            })
        };
        $http(reqUpdatePlayer).then(function (response) {
            return response.data;
        }, function (response) {
            return null;
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

stk.controller('PlayerController', ['$scope', '$http', '$routeParams', '$route', function ($scope, $http, $routeParams, $route) {
    if ($routeParams.lid == undefined && $routeParams.uid == undefined) {
        $scope.lid = 1;
        $scope.pid = 16;
    } else {
        $scope.lid = $routeParams.lid;
        $scope.pid = $routeParams.pid;
    }
    $scope.player = null;
    $scope.league = null;
    $scope.intNumStocks = 1000;
    $scope.intGetPriceTicker = 'AAPL';
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
        url: 'http://stock-fantasy-league.herokuapp.com/api/stock_data/top/7000'
    };
    $http(reqLeague).then(function (response) {
        $scope.league = JSON.parse(response.data).Leagues[0];
        //wrapped json
        $http(reqPlayer).then(function (response) {
            $scope.player = response.data[0];
            if ($scope.player.holdings == null) {
                $scope.player.holdings = []
            }
            if ($scope.player.availbalance == null) {
                $scope.player.availbalance = $scope.league.startbal;
            }
            if ($scope.player.translog == null) {
                $scope.player.translog = []
            }
            //update sholding with server
            //$scope.updatePlayer();

            $http(reqStocks).then(function (response) {
                $scope.topStocks = response.data.stocks;
            });
            $scope.intGetStocks($scope.intNumStocks);
            $scope.intGetPrice($scope.intGetPriceTicker);
        }, function (response) {
            console.log('Failing getting league info!');
        });
    }, function (response) {
        console.log('Failing getting league info!');
    });
    $scope.intGetStocks = function (intNumStocks) {
        $scope.intDisplayStocks = [];
        var reqStocks = {
            method: 'GET',
            url: 'http://stock-fantasy-league.herokuapp.com/api/stock_data/top/' + intNumStocks
        };
        $http(reqStocks).then(function (response) {
            $scope.intDisplayStocks = response.data.stocks;
        });
    }
    $scope.updatePlayer = function () {
        var reqUpdatePlayer = {
            method: 'POST',
            url: 'http://stock-fantasy-league.herokuapp.com/api/player/' +
                $scope.pid + '/update',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data: $.param({
                'update': JSON.stringify($scope.player)
            })
        };
        $http(reqUpdatePlayer).then(function (response) {

        }, function (response) {

        });
    };
    $scope.openChangeHoldings = function (stock, tType) {
        $scope.transactionType = tType;
        $scope.selectedStock = stock;
        $scope.selectedTicker = stock.symbol;
        $scope.selectedName = stock.name;
        $scope.numSharesSelected = 0;
        var reqPrice = {
            type: 'GET',
            url: 'http://stock-fantasy-league.herokuapp.com/api/stock_data',
            params: {
                'cmd': 'getStockData',
                'sym': $scope.selectedTicker
            }
        };
        new TradingView.widget({
            "width": 400,
            "height": 250,
            "symbol": $scope.selectedTicker,
            "interval": "D",
            "timezone": "Etc/UTC",
            "theme": "Light",
            "style": "1",
            "locale": "en",
            "toolbar_bg": "#f1f3f6",
            "enable_publishing": false,
            "allow_symbol_change": true,
            "container_id": "tradingview_cd18d"
        });
        $http(reqPrice).then(function (response) {
            $scope.selectedTicker = stock.symbol;
            $scope.selectedName = stock.name;
            $scope.selectedStockPrice = response.data.stockdata[0].price;
            $('#holdingsModal').modal('show');
        }, function (response) {});
    }
    $scope.modifyHoldings = function (stock, transactionType, numShares, price, testingStatus) {
        var index = $scope.player.holdings.findIndex(function (element) {
            return element.symbol == stock.symbol;
        });
        if (index >= 0 && !transactionType.localeCompare('Buy')) {
            if ($scope.player.availbalance < price * numShares) {
                numShares = Math.floor($scope.player.availbalance / price)
            }
            $scope.player.holdings[index].numberShares += numShares;
            $scope.player.availbalance -= price * numShares;
        } else if (index >= 0 && !transactionType.localeCompare('Sell')) {
            if ($scope.player.holdings[index].numberShares < numShares) {
                numShares = $scope.player.holdings[index].numberShares;
            }
            if ($scope.player.holdings[index].numberShares == numShares) {
                $scope.player.holdings.splice(index, 1);
            } else {
                $scope.player.holdings[index].numberShares -= numShares;
            }
            $scope.player.availbalance += price * numShares;
        } else if (index == -1 && !transactionType.localeCompare('Buy')) {
            if ($scope.player.availbalance < price * numShares) {
                numShares = Math.floor($scope.player.availbalance / price)
            }
            $scope.player.holdings.push({
                'symbol': stock.symbol,
                'name': stock.name,
                'numberShares': numShares
            });
            $scope.player.availbalance -= price * numShares;
        }
        $scope.updatePlayer();
        $('#myModal').modal('hide');
        $('body').removeClass('modal-open');
        $('.modal-backdrop').remove();
        if (!testingStatus)
            $route.reload();
    };
    $scope.integrationTesting = function (intTranType) {
        /* $scope.player.holdings = [{
             "symbol": "ABEV",
             "name": "Ambev S.A.",
             "numberShares": 10
             }, {
             "symbol": "GOOG",
             "name": "Alphabet Inc.",
             "numberShares": 2
             }];
         $scope.updatePlayer();
         */
        var intStock = {
            "symbol": "GOOG",
            "name": "Alphabet Inc.",
            "price": 1100
        };
        var intTestPrice = null;
        var reqPrice = {
            type: 'GET',
            url: 'http://stock-fantasy-league.herokuapp.com/api/stock_data',
            params: {
                'cmd': 'getStockData',
                'sym': 'AAPL'
            }
        };
        $http(reqPrice).then(function (response) {

            intTestPrice = response.data.stockdata[0].price;

        }, function (response) {});
        $scope.modifyHoldings(intStock, intTranType, 4, intTestPrice, false);
        /*setTimeout(function () {
            $scope.modifyHoldings(intStock, 'Sell', 4, intTestPrice, false);
        }, 10000);*/
    };
    $scope.intGetPrice = function (symArr) {
        var reqPrice = {
            type: 'GET',
            url: 'http://stock-fantasy-league.herokuapp.com/api/stock_data',
            params: {
                'cmd': 'getStockData',
                'sym': symArr
            }
        }
        $http(reqPrice).then(function (response) {
            $scope.intStockPrice = response.data.stockdata;
        }, function () {});
    };
}]);
stk.controller('NavbarController', ['$scope', function ($scope, $rootScope) {
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
        }, {
            name: 'Tutorial',
            command: 'ViewTutorial',
            href: '#!/tutorial'
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
        $scope.leagues = JSON.parse(response.data).Leagues;
    }, function loginFailure(response) {
        console.log('Failing getting leagues info!');
    });
    $scope.joinLeague = function (selected_lid) {
        if ($scope.uid > 0) {
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
                    $scope.leagues = JSON.parse(response.data).Leagues;
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

var updateUser = function (uid, user) {
    var reqUpdatePlayer = {
        method: 'POST',
        url: 'http://stock-fantasy-league.herokuapp.com/api/user/' +
            uid + '/update',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: $.param({
            'update': JSON.stringify(uid)
        })
    };
    $http(reqUpdatePlayer).then(function (response) {
        return response.data;
    }, function (response) {
        return null;
    });
};

var updatePlayer = function (pid, player) {
    var reqUpdatePlayer = {
        method: 'POST',
        url: 'http://stock-fantasy-league.herokuapp.com/api/player/' +
            pid + '/update',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: $.param({
            'update': JSON.stringify(player)
        })
    };
    $http(reqUpdatePlayer).then(function (response) {
        return response.data;
    }, function (response) {
        return null;
    });
};
/*function getPrice(symArr) {
    var reqPrice = {
        type: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/stock_data/',
        params: {
            'cmd': 'getStockData',
            'sym': symArr
        }
    }
    $http(reqPrice).then(function (response) {
        return response.data.stockdata;
    }, function () {
        return null;
    });
}*/
