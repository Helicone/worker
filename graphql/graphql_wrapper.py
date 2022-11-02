from sgqlc.operation import Operation
from .worker import Mutation, PromptRequest, SuccessResult, worker as schema

from python_graphql_client import GraphqlClient


def request_new_stable_diffusion_query() -> Mutation:
    op: Mutation = Operation(schema.Mutation)

    job: PromptRequest = op.request_new_job(
        job_type={
            "stableDiffusionV1_4": {
                "action": "txt2img"
            }
        }
    )
    job.created_at()
    job.id()
    job.params()
    return op


def post_stable_diffusion_result(prompt_uuid, images) -> Mutation:
    op: Mutation = Operation(schema.Mutation)
    result: SuccessResult = op.post_job_result(
        job_type={
            "id": prompt_uuid,
            "stableDiffusionV1_4": {
                "images": images
            }
        }
    )
    result.message()
    return op


def request_new_unknown_audio_query() -> Mutation:
    op: Mutation = Operation(schema.Mutation)

    job: PromptRequest = op.request_new_job(
        job_type={
            "unknownAudioV0": {
                "action": ""
            }
        }
    )
    job.created_at()
    job.id()
    job.params()
    return op


def post_unknown_audio_result(prompt_uuid, audios) -> Mutation:
    op: Mutation = Operation(schema.Mutation)
    result: SuccessResult = op.post_job_result(
        job_type={
            "id": prompt_uuid,
            "unknownAudioV0": {
                "audios": audios
            }
        }
    )
    result.message()
    return op
