import requests
import json
import pandas as pd

key = "34a712a1eab141619467f97f4b4e126c"
url = "https://api.spoonacular.com/food/products/search?query=yogurt&apiKey="
url += key

response = requests.get(url)

if(response.ok):
    # For successful API call, response code will be 200 (OK)

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(response.content)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    """
    for key in jData:
        print(key)
        print()
    """
else:
  # If response code is not ok (200), prt the resulting http error code with description
    response.raise_for_status()

response_df = pd.read_json(response.content)
print(response_df.head())
print(response_df.shape)

for i in response_df['products']:
    print(i)
    print()