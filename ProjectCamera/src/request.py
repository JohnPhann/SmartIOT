import requests


def upload_request(image_name):
    url = "https://notify-api.line.me/api/notify"
    access_token = 'J9FCLPNWqhBlwbQ5nNu37OkSnZCDnhmZtQMhuzc3xDB'
    headers = {'Authorization': 'Bearer ' + access_token}
    
    message = 'Warning!!!! Some object detected'
    image = image_name  # png or jpg
    payload = {'message': message}
    files = {'imageFile': open(image, 'rb')}
    r = requests.post(url, headers=headers, params=payload, files=files, )
    print("Line Notification Warning")
