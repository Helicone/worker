import base64
from time import sleep
import requests
import os

from example_helper import Config, build_url, get_job

URL = os.environ.get("PROMPT_ZERO_URL")
KEY = os.environ.get("API_KEY")
HEADERS = Config.HEADERS(KEY)

jobs = None
while True:
    job = get_job(
        build_url(URL, Config.CHECK_JOB_PATH, {
                  "modelType": 'StableDiffusionV1_4'}),
        HEADERS
    )
    if not job:
        sleep(10)
        continue

    sleep(1)
    print("POSTING NOW....")
    with open('kirby.jpeg', mode='rb') as file:
        fileContent = file.read()
        im_b64 = base64.b64encode(fileContent).decode("utf8")
        response = requests.post(
            build_url(URL, Config.PUSH_RESULT_PATH),
            headers=HEADERS,
            json={
                "result": {
                    "images": [
                        im_b64
                    ],
                },
                "prompt_uuid": job['uuid'],
                "user_uuid": job['user_id'],

            }
        )
        print(response)

    sleep(1)
