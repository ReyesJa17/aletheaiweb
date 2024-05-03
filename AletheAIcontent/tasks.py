from celery import shared_task
import requests

@shared_task
def post_to_social_media(api_url, api_key, message):
    headers = {'Authorization': f'Bearer {api_key}'}
    data = {'message': message}
    response = requests.post(api_url, headers=headers, data=data)
    if response.status_code == 200:
        print("Post successful!")
    else:
        print("Failed to post.")
