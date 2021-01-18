import requests
import json
import sys
from pyzbar.pyzbar import decode
from PIL import Image


def readBarcode(img):
  result = decode(Image.open('pic2.jpg'))
  data_conv = data.decode("utf-8") 
  print("str:",data_conv)
  return data_conv




def callUPCAPI(barcode):

  key = "vomzm65m1mrs95n8gwivnuz9xvpj8c"
  url = "https://api.barcodelookup.com/v2/products?barcode="
  url += barcode
  url += "&formatted=y&key="
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
  return response