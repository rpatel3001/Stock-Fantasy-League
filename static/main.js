var stk = angular.module('Stock Fantasy League', []);

stk.controller('LoginController', ['$scope', function ($scope) {
    $scope.showLogIn = false;
    $scope.message = 'Sign In';
    //x button
}]);

stk.controller('LeagueController', function ($scope) {
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
stk.controller('UserController', function ($scope, $http) {
    $http.get('http://stock-fantasy-league.herokuapp.com/api/user').then(function (response) {
        $scope.user = response.data;
    });
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
            name: 'Leagues',
            href: '/test'
        }, {
            name: 'Players',
            href: './l'
        }],
    };
}]);
