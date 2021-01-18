import requests
import json
import sys
from pyzbar.pyzbar import decode
from PIL import Image
from ..models import barcodeResult

def readBarcode(img):
  result = decode(Image.open(img))
  data = result[0].data
  data_conv = data.decode("utf-8") 
  print("str:",data_conv)
  return data_conv

def getAllBarcodes():
  barcods_objs = barcodeResult.objects.all()
  codes = set((obj.barcode for obj in barcods_objs))
  return codes

def retrieveCode(name):
  code = barcodeResult.objects.filter(barcode=name)[0]
  return code.data

def barcodeSearch(user_code):
    cachedCodes = getAllBarcodes() # Type = python set
    if user_code not in cachedCodes:
      return None
    else:
      codeData = retrieveCode(user_code)
    return codeData


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
  return response.json()