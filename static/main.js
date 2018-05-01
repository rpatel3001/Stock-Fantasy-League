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
    }).when("/league/:lid/gameshow/:pid", {
        templateUrl: 'gameshow.html'
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
stk.controller('LessonController', ['$scope', '$route', '$location', '$http', function ($scope, $route, $location, $http) {
    $scope.curquestion = 0;
    $scope.lesson = null;
    $scope.include_file = 'index.html';
    var reqLesson = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/lesson/1'
    };
    $http(reqLesson).then(function (response) {
        $scope.lesson = response.data;
        $scope.numEvent = $scope.lesson.length;
        console.log($scope.lesson[$scope.curquestion].topic);
    }, function (response) {
        console.log("error");
    });
    $scope.nextQuestion = function () {
        if ($scope.curquestion < ($scope.numEvent - 1)) {
            $scope.curquestion++;
        }
    }
    $scope.prevQuestion = function () {
        if ($scope.curquestion > 0) {
            $scope.curquestion--;
        }
    }
}]);
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
        url: 'http://stock-fantasy-league.herokuapp.com/api/league/' + $scope.lid + '/everything'
    };
    $scope.data = null;
    $http(req).then(function (response) {
        $scope.league = response.data[0];
        $http(reqPlayers).then(function (response) {
            $scope.players = response.data;
            if ($scope.lid > 6) {
                var reqOwner = {
                    method: 'GET',
                    url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + $scope.league.owneruid
                };
                $http(reqOwner).then(function (response) {
                    $scope.owner = response.data;
                }, function (response) {
                    console.log('Failing getting Owner info!');
                });
            }
        }, function (repsonse) {
            console.log(response);
        });
    }, function (response) {
        console.log('Failing getting league info!');
    });
}]);
stk.controller('GameShowController', ['$scope', '$timeout', '$interval', '$http', '$routeParams', function ($scope, $timeout, $interval, $http, $routeParams) {
        if ($routeParams.lid != undefined && $routeParams.pid != undefined) {
            $scope.lid = $routeParams.lid;
            $scope.pid = $routeParams.pid;
        } else {
            //$scope.lid = 1;
        }
        var reqLeague = {
            method: 'GET',
            url: 'http://stock-fantasy-league.herokuapp.com/api/league/' + $scope.lid
        };
        var req = {
            method: 'GET',
            url: 'http://stock-fantasy-league.herokuapp.com/api/league/' + $scope.lid + '/startquiz/' + $scope.pid
        };
        var reqServerTime = {
            method: 'GET',
            url: 'http://stock-fantasy-league.herokuapp.com/api/servertime'
        };
        var avail_time = 20,
            resp_time = 15;
        $scope.data = null;
        $scope.quizLive = false;
        $scope.nonLiveText = "🌟 Get ready for the Gameshow! 🌟";
        $scope.qindex = -1;
        $scope.numcorrect = 0;
        $scope.disbutton = "";
        $scope.seconds_left = avail_time;
        $scope.start_seconds = avail_time;
        $scope.counter_promise = null;
        $scope.showing_answer = false;
        $scope.selected_index = -1;
        var testingSetTime = {
            method: 'POST',
            url: 'http://stock-fantasy-league.herokuapp.com/api/setquiztime'
        };
        $http(reqLeague).then(function (response) {
            $scope.league = response.data[0];
            $scope.starttime = $scope.league.quiztime;
            $http(req).then(function (response) {
                $scope.questions = response.data; //check
                $scope.numquestions = $scope.questions.length;
                console.log("G+" + $scope.numquestions);
                //$scope.numquestions; //TO REVERT
                $scope.question = $scope.questions[$scope.qindex];
                $http(reqServerTime).then(function (response) {
                    $scope.servertime = response.data;
                    //$scope.starttime = Math.floor((new Date()).getTime() / 1000) + 3;
                    if (($scope.initdelay = $scope.starttime - $scope.servertime) > 0) {
                        $scope.seconds_left = $scope.initdelay;
                        $scope.start_seconds = $scope.initdelay;
                        $interval($scope.countdown, 1000, $scope.initdelay, true);
                        $timeout($scope.nextQuestion, $scope.initdelay * 1000);
                    } else {
                        $scope.quizLive = false;
                        $scope.nonLiveText = "Either the you joined the Gameshow too late or there is no quiz at the current time!";
                        return;
                    }
                }, function (repsonse) {
                    console.log(response);
                })
            }, function (response) {
                console.log('Failing getting league info!');
            });
        });
        // $scope.starttime = Math.round(new Date().getTime() + 10);
        /*$scope.startGameshow = function () {
            $interval($scope.countdown, 1000, avail_time, true);
            $timeout($scope.showAnswer, avail_time * 1000);
        }*/
        $scope.nextQuestion = function () {
            $scope.quizLive = true;
            $scope.disbutton = false;
            $scope.selected_index = -1;
            ++$scope.qindex;
            if ($scope.qindex > ($scope.numquestions - 1)) {
                //NEED TO FINISH
                console.log("completed");
                $scope.endGameshow();
            } else {
                $scope.showing_answer = false;
                $scope.seconds_left = avail_time;
                $scope.start_seconds = avail_time;
                $interval($scope.countdown, 1000, avail_time, true);
                $timeout($scope.showAnswer, avail_time * 1000);
            }
        }
        $scope.showAnswer = function () {
            if ($scope.selected_index == $scope.questions[$scope.qindex].answer_index) {
                //console.log("correctAnswer");
                $scope.numcorrect += 1;
            }
            $scope.showing_answer = true;
            $scope.seconds_left = resp_time;
            $scope.start_seconds = resp_time;
            $interval($scope.countdown, 1000, resp_time, true);
            $timeout($scope.nextQuestion, resp_time * 1000);
        }
        $scope.selectAnswer = function (index) {
            $scope.disbutton = true;
            $scope.selected_index = index;
        };
        $scope.countdown = function () {
            $scope.seconds_left -= 1;
            var ratio = ($scope.start_seconds - $scope.seconds_left) / $scope.start_seconds;
            $scope.progressbar = {
                'width': (($scope.start_seconds - $scope.seconds_left) / $scope.start_seconds) * 100 + "%"
            }
            if (ratio > .75) {
                $scope.progressbarclass = "bg-danger";
                $scope.timer = "text-danger";
            } else if (ratio > .5) {
                $scope.progressbarclass = "bg-warning";
                $scope.timer = "text-warning";
            } else {
                $scope.progressbarclass = "bg-success";
                $scope.timer = "";
            }
        }

        $scope.buttonclass = function (index) {
            if ($scope.showing_answer && index == $scope.questions[$scope.qindex].answer_index) {
                return "btn-success  disabled";
            } else if ($scope.showing_answer && index == $scope.selected_index) {
                return "btn-danger  disabled";
            } else if ($scope.showing_answer) {
                return "btn-secondary  disabled";
            } else if ($scope.disbutton && index == $scope.selected_index) {
                return "btn-primary disabled";
            } else if ($scope.disbutton) {
                return "btn-outline-primary disabled";
            } else {
                return "btn-outline-primary";
            }
        };
        $scope.endGameshow = function () {
            $scope.quizLive = false;
            $scope.showing_answer = false;
            var ratio = $scope.numcorrect / $scope.numquestions;
            if (ratio > .75) {
                $scope.nonLiveText = "🌟 Good job! You got " + $scope.numcorrect + " questions correct out of " + $scope.numquestions + ". Thank you for participating in the quiz! 🌟";
            } else if (ratio > .5) {
                $scope.nonLiveText = "⭐ You got " + $scope.numcorrect + " questions correct out of " + $scope.numquestions + ". Thank you for participating in the quiz! ⭐";
            } else {
                $scope.nonLiveText = "Better luck next time! You got " + $scope.numcorrect + " questions correct out of " + $scope.numquestions + ". Thank you for participating in the quiz!"
            }

            var sendScore = {
                method: 'PATCH',
                url: 'http://stock-fantasy-league.herokuapp.com/api/player/' + $scope.pid + '/correct/' + $scope.numcorrect + '/add'
            };
            $http(sendScore).then(function (response) {
                console.log("Ranking is recalculated at the end of the day.");
            });

        }
    }
]);
stk.controller('UserController', ['$scope', '$http', '$rootScope', '$routeParams', '$route', function ($scope, $http, $rootScope, $routeParams, $route) {
    if ($routeParams.uid == undefined) {
        $scope.paramuid = 1;
    } else {
        $scope.paramuid = $routeParams.uid;
    }
    $scope.inLeagueList = false;
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
        console.log('Failing getting User info!');
    });
    $scope.openCreateLeagueModal = function () {
        $('#createLeagueModal').modal('show');
    }
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
                if ($scope.user.lid == null)
                    $scope.user.lid = [];
                $scope.user.lid.push(response.data[response.data.length - 1].lid);
                $('#createLeagueModal').modal('hide');
                $('body').removeClass('modal-open');
                $('.modal-backdrop').remove();
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
    $scope.deleteLeague = function (lid) {
        var reqDeleteLeague = {
            method: 'DELETE',
            url: 'http://stock-fantasy-league.herokuapp.com/api/league/' +
                lid + '/delete'
        };
        $http(reqDeleteLeague).then(function (response) {
            $route.reload();
        }, function (response) {
            console.log("Error deleting League");
        });
    };
    $scope.leaveLeague = function (uid, pid) {
        var reqLeaveLeague = {
            method: 'PATCH',
            url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + uid + '/player/' + pid + '/leave'
        };
        $http(reqLeaveLeague).then(function (response) {
            $route.reload();
        }, function (response) {
            console.log("Error leaving League");
        });
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
            $scope.league = response.data[0];
            //wrapped json
            $http(reqPlayer).then(function (response) {
                    $scope.player = response.data[0];
                    if (!($scope.player.holdings instanceof Array)) {
                        $scope.player.holdings = []
                    }
                    if ($scope.player.availbalance == null) {
                        $scope.player.availbalance = $scope.league.startbal;
                    }
                    if (!($scope.player.translog instanceof Array)) {
                        $scope.player.translog = [];
                    }
                    //update sholding with server
                    //$scope.updatePlayer();
                    var reqUser = {
                        method: 'GET',
                        url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + $scope.player.uid
                    };
                    $http(reqUser).then(function (response) {
                        $scope.user = response.data;
                    });
                    $http(reqStocks).then(function (response) {
                        $scope.topStocks = response.data.stocks;
                    });
                    $scope.intGetStocks($scope.intNumStocks);
                    $scope.intGetPrice($scope.intGetPriceTicker);
                },
                function (response) {
                    console.log('Failing getting league info!');
                });
        },
        function (response) {
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
        $('#holdingsModal').modal('hide');
        $('body').removeClass('modal-open');
        $('.modal-backdrop').remove();
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
stk.filter('stockSearch', function () {
    return function (input, searchstatus) {
        console.log(searchstatus);
        if (searchname === undefined || (searchname.name == "" && searchname.symbol == "")) {
            console.log(index + index < 100 ? true : false);
            return index < 100 ? input : false;
        } else {
            return input;
        }
    }

});
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
        }, {
                name: 'Lesson',
                command: 'ViewLesson',
                href: '/lessons.html'
        }
               ]
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
stk.controller('LeagueListController', ['$scope', '$http', '$rootScope', '$location', '$route', function ($scope, $http, $rootScope, $location, $route) {
    $scope.leaguesView = true; //need to make an official watch in another controller
    $scope.inLeagueList = true;
    $scope.navbarHeader = "Leagues";
    var reqLeagues = {
        method: 'GET',
        url: 'http://stock-fantasy-league.herokuapp.com/api/league'
    };
    $scope.data = null;
    $scope.startBal = null;
    $scope.intStartBal = 10000;
    $scope.duration = null;
    $scope.intDuration = new Date("01/01/2030");
    $scope.leaguename = null;
    $http(reqLeagues).then(function loginSuccess(response) {
        $scope.leagues = response.data;
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
                $location.path("/league/" + selected_lid + "/player/" + response.data[response.data.length - 1].pid);
                //console.log(response.pid); //unwrapped json
            }, function (response) {
                console.log('Failing to join league!');
            });
        }
    };
    $scope.deleteLeague = function (lid) {
        var reqDeleteLeague = {
            method: 'DELETE',
            url: 'http://stock-fantasy-league.herokuapp.com/api/league/' +
                lid + '/delete'
        };
        $http(reqDeleteLeague).then(function (response) {
            $route.reload();
        }, function (response) {
            console.log("Error deleting League");
        });
    };
    $scope.leaveLeague = function (uid, pid) {
        var reqLeaveLeague = {
            method: 'PATCH',
            url: 'http://stock-fantasy-league.herokuapp.com/api/user/' + uid + '/player/' + pid + '/leave'
        };
        $http(reqLeaveLeague).then(function (response) {
            $route.reload();
        }, function (response) {
            console.log("Error leaving League");
        });
    };
    $scope.openCreateLeagueModal = function () {
        $('#createLeagueModal').modal('show');
    }
    $scope.createLeague = function () {
        if ($scope.uid > 0) { // could use user.uid as well
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
                /* $scope.user.lid.push(response.data[response.data.length - 1].lid);*/
                $('#createLeagueModal').modal('hide');
                $('body').removeClass('modal-open');
                $('.modal-backdrop').remove();
                $location.path("/league/" + response.data[response.data.length - 1].lid);
            }, function (response) {
                console.log('Failing getting league info!');
            });
        };
    };
}]);

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
