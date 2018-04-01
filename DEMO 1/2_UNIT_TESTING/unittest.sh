#create users <uid = 1>, <uid = 2>
#newuser: create user
curl -X POST -d "email=sample1@sample1.com&username=sampleUsername1&imageurl=https://orig00.deviantart.net/68a0/f/2013/309/6/a/profile_picture_by_fruit_juice_dog-d6t7bul.png&description=sampledescription1&token=123" localhost:5000/api/user
curl -X POST -d "email=sample2@sample2.com&username=sampleUsername2&imageurl=https://orig00.deviantart.net/68a0/f/2013/309/6/a/profile_picture_by_fruit_juice_dog-d6t7bul.png&description=sampledescription2&token=321" localhost:5000/api/user
#user1: create league
curl -X POST -d "startBal=10000&duration=4070989760&leagueName=UNIT TEST LEAGUE&description=unit test" localhost:5000/api/user/1

#user2: join league
curl -X POST -d "lid=1" localhost:5000/api/user/2/joinLeague

#any user: get information of user1
curl -X GET localhost:5000/api/user/1

echo "About to update user! Updating in 2 seconds."
sleep 2s
#system: update player 1:
#example: changes balance to 50k
# {"pid":1,"uid":1,"lid":1,"holdings":{"holdings":[]},"notifications":null,"availbalance":50000,"pendingorders":null,"translog":{"translog":[]}}
curl -X POST -d "update=%7B%22pid%22%3A1%2C%22uid%22%3A1%2C%22lid%22%3A1%2C%22holdings%22%3A%7B%22holdings%22%3A%5B%5D%7D%2C%22notifications%22%3Anull%2C%22availbalance%22%3A50000%2C%22pendingorders%22%3Anull%2C%22translog%22%3A%7B%22translog%22%3A%5B%5D%7D%7D" localhost:5000/api/player/1/update

#system: update user 1:
#example: change VIP status
# {"uid": 1, "lid": [1], "pid": [1], "friends": null, "email": "sample1@sample1.com", "messages": null, "notifications": null, "username": "sampleUsername1", "imageurl": "https://orig00.deviantart.net/68a0/f/2013/309/6/a/profile_picture_by_fruit_juice_dog-d6t7bul.png", "vip": true, "token": "123", "description": null, "joinday": 1522421487}
curl -X POST -d "update=%7B%22uid%22%3A%201%2C%20%22lid%22%3A%20%5B1%5D%2C%20%22pid%22%3A%20%5B1%5D%2C%20%22friends%22%3A%20null%2C%20%22email%22%3A%20%22sample1%40sample1.com%22%2C%20%22messages%22%3A%20null%2C%20%22notifications%22%3A%20null%2C%20%22username%22%3A%20%22sampleUsername1%22%2C%20%22imageurl%22%3A%20%22https%3A%2F%2Forig00.deviantart.net%2F68a0%2Ff%2F2013%2F309%2F6%2Fa%2Fprofile_picture_by_fruit_juice_dog-d6t7bul.png%22%2C%20%22vip%22%3A%20true%2C%20%22token%22%3A%20%22123%22%2C%20%22description%22%3A%20null%2C%20%22joinday%22%3A%201522421487%7D" localhost:5000/api/user/1/update

#ADMIN: get information of all users
curl -X GET localhost:5000/api/user
#player: get data for stock given ticker
curl -X GET "localhost:5000/api/stock_data?cmd=getStockData&sym=goog"

