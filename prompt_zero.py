import base64
from glob import glob
import shutil
from time import sleep
import os
from graphql.graphql_wrapper import post_stable_diffusion_result, request_new_stable_diffusion_query
from graphql.worker import PromptRequest, RequestModelParams, ResultParams_StableDiffusionV1_4, SuccessResult
from lib.txt2img import TxtToImgRequest, txt_to_img
from sgqlc.endpoint.http import HTTPEndpoint


URL = os.environ.get("PROMPT_ZERO_URL")
KEY = os.environ.get("API_KEY")


def get_sd_image(outdir: str, prompt: ResultParams_StableDiffusionV1_4) -> str:
    request = TxtToImgRequest(
        prompt=prompt.prompt,
        n_samples=prompt.n_samples,
        n_iter=1,
        plms=True,
        precision="full",
        outdir=outdir,
        skip_grid=True
    )
    print(txt_to_img(request))


def get_image(outdir: str, prompt: RequestModelParams) -> str:
    if (isinstance(prompt, ResultParams_StableDiffusionV1_4)):
        get_sd_image(outdir, prompt)


def image_to_binary(path: str) -> str:
    with open(path, mode='rb') as file:
        fileContent = file.read()
        return base64.b64encode(fileContent).decode("utf8")


endpoint = HTTPEndpoint(URL, {"authorization": KEY})
while True:
    op = request_new_stable_diffusion_query()
    data = endpoint(op)
    job: PromptRequest = (op+data).request_new_job
    if not job:
        print("No job found... sleeping")
        sleep(1)
    else:
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
