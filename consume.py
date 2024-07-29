import requests

#The Random-Word API (Heroku App)
url = "https://random-word-api.herokuapp.com/word"
word_quantity = 5

def fetchWord():
    response = requests.get(F"{url}?number={word_quantity}")
    if response.status_code == 200:
        data = response.json()
        # print(data)
        return data
    else:
        print("failed to retrieve data:", response.status_code)

