from pyzbar.pyzbar import decode
from PIL import Image
import sys
result = decode(Image.open('pic2.jpg'))

print(result)
data = result[0].data

print()
print(type(data))
print(data)
data_conv = int.from_bytes(data, byteorder=sys.byteorder)
print(data_conv)
data_conv = data.decode("utf-8") 
print("str:",data_conv)

print()
for i in result[0]:
	print(i)

