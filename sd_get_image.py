from graphql.worker import RequestModelParams, ResultParams_StableDiffusionV1_4
from lib.txt2img import TxtToImgRequest, txt_to_img


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
