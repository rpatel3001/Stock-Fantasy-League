describe('UserListController', function () {

    var $controller;
    beforeEach(inject(function (_$controller_) {

        $controller = _$controller_;
    }));
});
describe("getUserList", function () {
    it('calls on UserListController and sees if the user list is returned. Check by seeing if some predifined users are in the list.', function () {
        var $scope = {};
        var controller = $controller('UserListController', {
            $scope: $scope
        });
        var keysExpected = [];
        var keysRecieved = Object.keys($scope.data.Users[0]);
        expect($scope.data.Users[0].username).toContain("ALEXANDER CHAN");
    });
});
