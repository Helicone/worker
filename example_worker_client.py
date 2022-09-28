import base64
from time import sleep
import os
from sgqlc.endpoint.http import HTTPEndpoint
from lib.graphql_wrapper import post_stable_diffusion_result, request_new_stable_diffusion_query
from worker import PromptRequest, SuccessResult


URL = os.environ.get("PROMPT_ZERO_URL")
KEY = os.environ.get("API_KEY")


endpoint = HTTPEndpoint(URL, {"authorization": KEY})
while True:
    op = request_new_stable_diffusion_query()
    data = endpoint(op)
    job: PromptRequest = (op+data).request_new_job
    if not job:
        sleep(10)
        continue

    sleep(1)
    print("POSTING NOW....")
    with open('kirby.jpeg', mode='rb') as file:
        fileContent = file.read()
        im_b64 = base64.b64encode(fileContent).decode("utf8")
        op = post_stable_diffusion_result(
            job.id, [{"bytes": im_b64}, {"bytes": im_b64}])
        data = endpoint(op)
        response: SuccessResult = (op+data).post_job_result
        print(response.message)

    sleep(1)
