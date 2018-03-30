#manually inject users <uid = 1>, <uid = 2>
#user1: create league
curl -X POST -d "startBal=10000&duration=4070989760&leagueName=UNIT TEST LEAGUE&description=unit test" localhost:5000/api/user/1
#user2: join league
curl -X POST -d "lid=1" localhost:5000/api/user/2/joinLeague
#any user: get information of user1
curl -X GET localhost:5000/api/user/1
#ADMIN: 
