import requests

response =requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
print(response.json()[0]["setup"])
print(response.json()[0]["punchline"])