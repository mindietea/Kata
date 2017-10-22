from flask import jsonify, request
import json
import requests
import semantics

def custom_vision_endpoint(user_image_url):
    payload = {
      #  "Url": user_image_url
        "Url": "http://www.shadestation.co.uk/media/thumbs/800x800/media/product_images/Rayban-Glasses-RX5227-2034afw800fh800.png"
    }
    headers = {
        "Content-Type": "application/json",
        "Prediction-Key": "66aaad81eed9481bba65df01dfe09420"
    }

    url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/91f2d2f7-5c8d-4eb3-a741-a9c75ab6fc41/url"
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response = response.json()
    if response['Predictions'][0]['Probability'] > .70:
        val = response['Predictions'][0]['Tag']
        print(val)
        return semantics.get_recommendations(val)



custom_vision_endpoint("")