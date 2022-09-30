from dataclasses import dataclass
from glob import glob
from lib.txt2img import txt_to_img, TxtToImgRequest
import shutil


import base64
from time import sleep
import requests
import os
import urllib
from typing import Optional

URL = os.environ.get("PROMPT_ZERO_URL")
KEY = os.environ.get("API_KEY")

HEADERS = {
    'bhunkio_auth': KEY
}

CHECK_JOB_PATH = "/api/worker/jobs"
PUSH_RESULT_PATH = "/api/worker/results"


def build_url(base_url, path, args_dict={}):
    url_parts = list(urllib.parse.urlparse(base_url))
    url_parts[2] = path
    url_parts[4] = urllib.parse.urlencode(args_dict)
    return urllib.parse.urlunparse(url_parts)


def get_image(outdir: str, prompt: str) -> str:
    request = TxtToImgRequest(
        prompt=prompt,
        n_samples=1,
        n_iter=1,
        plms=True,
        precision="full",
        outdir=outdir,
        skip_grid=True
    )
    print(txt_to_img(request))


@dataclass
class PromptQueue:
    uuid: str
    user_id: str
    prompt: str
    result_id: str
    status: int
    current_worker: str
    created_at: str
    job_started_time: str
    model_type: str
    request_input_params: str
    model_action: str
    name: Optional[str]


def image_to_binary(path: str) -> str:
    with open(path, mode='rb') as file:
        fileContent = file.read()
        return base64.b64encode(fileContent).decode("utf8")


def do_job(prompt_request: PromptQueue):
    out_dir = f"outputs/txt2img-results/{prompt_request.uuid}"
    get_image(outdir=out_dir, prompt=prompt_request.prompt)
    images = glob(f"{out_dir}/samples/*")
    binary_images = [image_to_binary(i) for i in images]

    shutil.rmtree(out_dir)

    return {
        "result": {"images": binary_images},
        "prompt_uuid": prompt_request.uuid,
        "user_uuid": prompt_request.user_id,
    }


def main():
    jobs = None
    while True:
        print("getting jobs..")
        job_request = requests.get(
            build_url(URL, CHECK_JOB_PATH, {
                      "modelType": 'StableDiffusionV1_4'}),
            headers=HEADERS,
        )
        if job_request and job_request.json().get('uuid') != None:
            print(f"Got a job! - {job_request.json()}")
            result = do_job(PromptQueue(**job_request.json()))
            response = requests.post(
                build_url(URL, PUSH_RESULT_PATH),
                headers=HEADERS,
                json=result
            )
            print(f"finished job! Response: {response}")
        else:
            print(f"no response {job_request.text}")
            sleep(5)
            continue


if __name__ == "__main__":
    main()
