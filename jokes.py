import requests

def joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        json_data = requests.get(url).json()
        return [json_data["setup"], json_data["punchline"]]
    except:
        return ["Sorry, couldn't fetch a joke right now.", ""]
