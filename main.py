import hashlib
image_path = "param.jpg"
with open(image_path,"rb") as image_file:
   image_bytes=image_file.read()
   h=hashlib.sha256(image_bytes).hexdigest()
   print(h)