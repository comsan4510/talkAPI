import requests

#送信先url
url = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk"
def send_talkapi(msg='Hello'):

    #送信データ
    payload = {
        "apikey" : "DZZao0hq1RccvBgUMYWUrtUsTXFoD9fF",
        "query" : msg
    }
        
    response = requests.post(url,data=payload)
    message = response.json()
    return message['results'][0]['reply']
