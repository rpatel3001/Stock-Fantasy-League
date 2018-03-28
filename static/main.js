var stk = angular.module('Stock Fantasy League', ["ngRoute"]);
stk.config(function ($routeProvider) {
    $routeProvider.when("/", {
        templateUrl: "homepage_parts.html"
    }).when("/users", {
        templateUrl: 'user_list.html',
        controller: 'UserListController',
    }).when("/user/:uid", {
        templateUrl: 'user_info.html',
        controller: 'UserInfoController'
    }).when("/leagues", {
        templateUrl: 'league_list.html',
        controller: 'LeagueListController'
    }).when("/dashboard", {
        templateUrl: 'dashboard_parts.html',
        controller: 'DashboardController'
    });
});
stk.controller('LoginController', ['$scope', function ($scope) {
    $scope.showLogIn = false;
    $scope.message = 'Sign In';
    //x button
}]);

stk.controller('LeagueController', function ($scope, $http) {
    $scope.league = {
        leagueName: "Test",
        leagueCreator: "Oz Bejerano",
        numberMembers: 10,
        marketCap: 1973824.76,
        players: [
            {
                username: "Oz",
                description: "I'm Oz",
                holdings: 10982.67
            },
            {
                username: "Oz2",
                description: "I'm Oz",
                holdings: 109328.67
            },
            {
                username: "Oz",
                description: "I'm 3Oz",
                holdings: 1032398.67
            }
        ]
    };
});
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
            href: '#!users'
        }, {
            name: 'Leagues',
            command: 'ViewLeagues',
            href: '#!leagues'
        }]
    };
}]);

stk.controller('PageManagerController', ['$scope', '$rootScope', '$location', function ($scope, $rootScope, $location) {
    $scope.title = "Stock Fanatasy League";
    /*$scope.activepage = {
        homepage: {
            link: 'homepage_parts.html',
            visible: true
        },
        leagues: {
            link: 'league_parts.html',
            visible: false
        },
        users: {
            link: 'user_parts.html',
            visible: false
        },
        dashboard: {
            link: 'dashboard_parts.html',
            visible: false
        }
    };*/
    /*$scope.$on('ViewUsers', function viewUsers() {
        $scope.activePage.homepage.visible = false;
        $scope.activePage.users.visible = true;
        $scope.activePage.leagues.visible = false;
        $scope.activePage.dashboard.visible = false;
        $location.path("/users");
    });
    $scope.$on('ViewDashboard', function viewDashboard() {
        $scope.activePage.homepage.visible = false;
        $scope.activePage.dashboard.visible = true;
        $scope.activePage.users.visible = true;
        $scope.activePage.leagues.visible = false;
        $location.path("/dashboard");
    });
    $scope.$on('ViewLeagues', function viewLeagues() {
        $scope.activePage.homepage.visible = false;
        $scope.activePage.users.visible = false;
        $scope.activePage.leagues.visible = true;
        $scope.activePage.dashboard.visible = false;
        $location.path("/leagues");
    });
    $scope.$on('ViewHomePage', function viewHomePage() {
        $scope.activePage.homepage.visible = true;
        $scope.activePage.users.visible = false;
        $scope.activePage.leagues.visible = false;
        $scope.activePage.dashboard.visible = false;
        $location.path("/");
    });*/
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
        console.log('Failing getting user info!');
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
        console.log('Failing getting user info!');
    });
});
