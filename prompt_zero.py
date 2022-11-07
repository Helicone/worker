import base64
from glob import glob
import shutil
from time import sleep
import os
from typing import Callable
from graphql.graphql_wrapper import post_stable_diffusion_result, request_new_stable_diffusion_query
from graphql.worker import PromptRequest, RequestModelParams, ResultParams_StableDiffusionV1_4, SuccessResult
from sgqlc.endpoint.http import HTTPEndpoint


PZ_TEST = os.environ.get("PZ_TEST")

if PZ_TEST.lower() == 'true':
    import shutil

    def get_sd_image(outdir: str, prompt: ResultParams_StableDiffusionV1_4) -> str:
        for i in range(prompt.n_samples,):
            shutil.copyfile(os.path.join('assets/kirby.jpeg'),
                            os.path.join(outdir, "/samples", i))

    def get_image(outdir: str, prompt: RequestModelParams) -> str:
        if (isinstance(prompt, ResultParams_StableDiffusionV1_4)):
            get_sd_image(outdir, prompt)

else:
    from sd_get_image import get_image


URL = os.environ.get("PROMPT_ZERO_URL")
KEY = os.environ.get("API_KEY")


def image_to_binary(path: str) -> str:
    with open(path, mode='rb') as file:
        fileContent = file.read()
        return base64.b64encode(fileContent).decode("utf8")


def proccess_new_job(get_image: Callable[[str, RequestModelParams], str], endpoint: HTTPEndpoint, job: PromptRequest):
    print(f"Got a job! - {job}")
    out_dir = f"outputs/txt2img-results/{job.id}"
    get_image(outdir=out_dir, prompt=job.params)
    images = glob(f"{out_dir}/samples/*")
    binary_images = [image_to_binary(i) for i in images]
    shutil.rmtree(out_dir)
    print("POSTING NOW....")
    op = post_stable_diffusion_result(
        job.id, [{"bytes": b} for b in binary_images])
    data = endpoint(op)
    response: SuccessResult = (op+data).post_job_result
    print(response.message)


def request_and_proccess_job(get_image, endpoint):
    op = request_new_stable_diffusion_query()
    data = endpoint(op)
    job: PromptRequest = (op+data).request_new_job
    if not job:
        print("No job found... sleeping")
        sleep(1)
    else:
        proccess_new_job(get_image, endpoint, job)


endpoint = HTTPEndpoint(URL, {"authorization": KEY})
while True:
    request_and_proccess_job(get_image, endpoint)
