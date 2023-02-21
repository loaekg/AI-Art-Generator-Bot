import webbrowser
import tweepy
from base64 import b64decode
import openai
import time
import json
import re

#Twitter
api_key= "D5L AL API TA3K"
api_secret= "D5L AL API TA3K"
bearer_token= r"D5L AL TOKEN TA3K"
access_token= "D5L AL TOKEN TA3K"
access_token_secret= "D5L AL TOKEN TA3K"




client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)
client_id = client.get_me().data.id



openai.api_key='D5L AL API TA3K'

def generatedImage(prompt, image_count):
    images = []
    response = openai.Image.create(
        prompt=prompt,
        n=image_count,
        size= '1024x1024',
        response_format='b64_json'
        )
    for image in response['data']:
        images.append(image.b64_json)

    prefix = 'Img'
    for index,image in enumerate(images):
        with open(f'{prefix}_{index}.jpg','wb') as file:
            file.write(b64decode(image))
            


#ID
client_id = client.get_me().data.id




def removeM(tweet):
    a1=tweet.text
    a2= a1.lower().replace("D5L UR BOT USER", '')
    return a2




    

# 7ay 3shan albot yrd 3la a5r tweets o ma yrd akthr mn mra
start_id = 1
initialisation_resp = client.get_users_mentions(client_id)
if initialisation_resp.data != None:
    start_id = initialisation_resp.data[0].id
response = client.get_users_mentions(client_id, since_id=start_id)





while True:
    response = client.get_users_mentions(client_id, since_id=start_id)
    
    if response.data != None:
        
        for tweet in response.data: 
                       
            try:
                start_id= tweet.id
                pic=generatedImage(removeM(tweet), image_count=1)
                media = api.media_upload(filename='Img_0.jpg')
                print(removeM(tweet))

                api.update_status(status='الصوره جاهزة!', in_reply_to_status_id=tweet.id, media_ids=[media.media_id], auto_populate_reply_metadata=True)
            except Exception as error:
                print(error)
            

    time.sleep(5)





