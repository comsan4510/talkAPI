import requests as rq

url = "https://api.a3rt.recruit.co.jp/image_search/v1/search_by_text"
apikey = "DZZZU0zjzio0m4RTrfvzJq9wPfdKGIJk"
query = "りんご"

param = {
 "apikey" : apikey,
 "query" : query
}


res = rq.get(url,params=param)

print(res.json()['result']['txt'][0])