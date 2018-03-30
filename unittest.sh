#manually inject users <uid = 1>, <uid = 2>
#newuser: create user
curl -X POST -d "email=sample@sample.com&username=sampleUsername&imageurl=https://orig00.deviantart.net/68a0/f/2013/309/6/a/profile_picture_by_fruit_juice_dog-d6t7bul.png&description=sample description" localhost:5000/api/user
#user1: create league
curl -X POST -d "startBal=10000&duration=4070989760&leagueName=UNIT TEST LEAGUE&description=unit test" localhost:5000/api/user/1
#user2: join league
curl -X POST -d "lid=1" localhost:5000/api/user/2/joinLeague
#any user: get information of user1
curl -X GET localhost:5000/api/user/1



#system: update user:
curl -X POST -d "update=%7B%22pid%22%3A1%2C%22uid%22%3A2%2C%22lid%22%3A1%2C%22holdings%22%3A%7B%22holdings%22%3A%5B%5D%7D%2C%22notifications%22%3Anull%2C%22availbalance%22%3A20000%2C%22pendingorders%22%3Anull%2C%22translog%22%3A%7B%22translog%22%3A%5B%5D%7D%7D" localhost:5000/api/player/1/update

#ADMIN: get information of all users
curl -X GET localhost:5000/api/user
#player: get data for stock given ticker
curl -X GET "localhost:5000/api/stock_data?cmd=getStockData&sym=goog"

