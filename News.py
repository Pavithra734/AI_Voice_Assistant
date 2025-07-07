import requests

Key = "12bc430f6cee44528705af6172c5659b"

def news():
    api_address = f"http://newsapi.org/v2/top-headlines?country=us&apikey={Key}"
    arr = []
    try:
        json_data = requests.get(api_address).json()
        for i in range(3):
            headline = f"Number {i + 1}: {json_data['articles'][i]['title']}."
            arr.append(headline)
    except:
        arr.append("Unable to fetch news at the moment.")
    return arr
