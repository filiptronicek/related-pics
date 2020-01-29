from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import json
import requests

random_pic_url = "https://picsum.photos/1920/1080"

# Add your Computer Vision subscription key to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()
# Add your Computer Vision endpoint to your environment variables.
if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
else:
    print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
remote_image_url = input("Your image URL: [defaults to "+random_pic_url+"]")
if remote_image_url == "":
    remote_image_url = random_pic_url

percisionLvl = input("How percise should the recognition be (1-5 recommended) [default 3]")
if percisionLvl == "":
    percisionLvl = 3

print("\n\n===== Top #{} Image tags =====".format(percisionLvl))
# Call API with remote image
tags_result_remote = computervision_client.tag_image(remote_image_url)

description_results = computervision_client.describe_image(remote_image_url )
# Print results with confidence score

print("Searching for the tags:")  
if (len(tags_result_remote.tags) == 0):
    print("No tags detected.")
else:
    pixabayUrl = "https://pixabay.com/api/?key="+ os.environ['PIXABAY_API_KEY'] +"&q="

    for i,tag in enumerate(tags_result_remote.tags):
        if i < int(percisionLvl):    
            print("#{} [{:.2f}]%".format(tag.name, tag.confidence * 100))   
            if i > 0: pixabayUrl += "+" + tag.name
            else: pixabayUrl += tag.name
    pixabayUrl += "&image_type=photo&pretty=true"
# Get the captions (descriptions) from the response, with confidence level
print("\n\n===== Image description =====")
if (len(description_results.captions) == 0):
    print("No description detected.")
else:
    for caption in description_results.captions:
        print("That's {}. (I'm {:.2f}% sure)".format(caption.text, caption.confidence * 100))

responce = requests.get(pixabayUrl)

print("\n\n===== Results from PixaBay: [https://pixabay.com] =====\n")
print(responce)

jsonedResponce = json.loads(responce.text)

#print(jsonedResponce["hits"][0]["largeImageURL"])

for i,hit in enumerate(jsonedResponce["hits"]):
   print(jsonedResponce["hits"][i]["largeImageURL"])
