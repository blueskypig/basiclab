import io
import os

import google.cloud.vision

#Create a Vision client
vision_client=google.cloud.vision.ImageAnnotatorClient()
image_file_name='tmp.jpg'
with io.open(image_file_name,'rb') as image_file:
	content=image_file.read()

image=google.cloud.vision.types.Image(content=content)
response=vision_client.label_detection(image=image)

print('Labels:')
for label in response.label_annotations:
	print(label.description)

#AIzaSyDEalqpIeZ7ICkQcTP8Kp1QOXf8mAMQW6g
