import sgqlc.types


worker = sgqlc.types.Schema()


########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

ID = sgqlc.types.ID

Int = sgqlc.types.Int


class ModelType(sgqlc.types.Enum):
    __schema__ = worker
    __choices__ = ('Custom', 'StableDiffusionV1_4', 'UnknownAudioV0')


class OrderByDirection(sgqlc.types.Enum):
    __schema__ = worker
    __choices__ = ('Asc', 'Dsc')


class Params_StableDiffusionV1_4_Action(sgqlc.types.Enum):
    __schema__ = worker
    __choices__ = ('img2img', 'inPaint', 'txt2img')


class Params_StableDiffusionV1_4_Sampler(sgqlc.types.Enum):
    __schema__ = worker
    __choices__ = ('ddim', 'k_dpm_2', 'k_dpm_2_ancestral',
                   'k_euler', 'k_euler_ancestral', 'k_huen', 'k_lms', 'plms')


class PromptRequestStatus(sgqlc.types.Enum):
    __schema__ = worker
    __choices__ = ('Completed', 'Failed', 'NotStarted', 'Started')


class PromptsOrderBy(sgqlc.types.Enum):
    __schema__ = worker
    __choices__ = ('CreatedAt', 'Id', 'Status')


String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################
class Asset(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('url', 'bytes')
    url = sgqlc.types.Field(String, graphql_name='url')
    bytes = sgqlc.types.Field(String, graphql_name='bytes')


class AudioAsset(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('bytes',)
    bytes = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='bytes')


class Custom(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('josnb',)
    josnb = sgqlc.types.Field(String, graphql_name='josnb')


class ImageAsset(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('bytes',)
    bytes = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='bytes')


class JobResult(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('id', 'stable_diffusion_v1_4', 'unknown_audio_v0')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    stable_diffusion_v1_4 = sgqlc.types.Field(
        'JobResultStableDiffusionV1_4', graphql_name='stableDiffusionV1_4')
    unknown_audio_v0 = sgqlc.types.Field(
        'JobResultUnknownAudioV0', graphql_name='unknownAudioV0')


class JobResultStableDiffusionV1_4(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('images',)
    images = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null(ImageAsset))), graphql_name='images')


class JobResultUnknownAudioV0(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('audios',)
    audios = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null(AudioAsset))), graphql_name='audios')


class JobType(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('stable_diffusion_v1_4', 'unknown_audio_v0', 'custom')
    stable_diffusion_v1_4 = sgqlc.types.Field(
        'JobTypeStableDiffusionV1_4', graphql_name='stableDiffusionV1_4')
    unknown_audio_v0 = sgqlc.types.Field(
        'JobTypeUnknownAudioV0', graphql_name='unknownAudioV0')
    custom = sgqlc.types.Field(Custom, graphql_name='custom')


class JobTypeStableDiffusionV1_4(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('action',)
    action = sgqlc.types.Field(sgqlc.types.non_null(
        Params_StableDiffusionV1_4_Action), graphql_name='action')


class JobTypeUnknownAudioV0(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('action',)
    action = sgqlc.types.Field(String, graphql_name='action')


class Params_Custom(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('jsonb',)
    jsonb = sgqlc.types.Field(String, graphql_name='jsonb')


class Params_StableDiffusionV1_4(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('action', 'prompt', 'width', 'height', 'cfg_scale',
                       'steps', 'n_samples', 'sampler', 'seed', 'input_image')
    action = sgqlc.types.Field(sgqlc.types.non_null(
        Params_StableDiffusionV1_4_Action), graphql_name='action')
    prompt = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='prompt')
    width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='width')
    height = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='height')
    cfg_scale = sgqlc.types.Field(Int, graphql_name='cfgScale')
    steps = sgqlc.types.Field(Int, graphql_name='steps')
    n_samples = sgqlc.types.Field(Int, graphql_name='nSamples')
    sampler = sgqlc.types.Field(
        Params_StableDiffusionV1_4_Sampler, graphql_name='sampler')
    seed = sgqlc.types.Field(Int, graphql_name='seed')
    input_image = sgqlc.types.Field(Asset, graphql_name='inputImage')


class Params_UnknownAudioV0(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('prompt', 'dim_steps', 'n_samples')
    prompt = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='prompt')
    dim_steps = sgqlc.types.Field(Int, graphql_name='dimSteps')
    n_samples = sgqlc.types.Field(Int, graphql_name='nSamples')


class PromptRequestBody(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('stable_diffusion_v1_4', 'unknown_audio_v0', 'custom')
    stable_diffusion_v1_4 = sgqlc.types.Field(
        Params_StableDiffusionV1_4, graphql_name='stableDiffusionV1_4')
    unknown_audio_v0 = sgqlc.types.Field(
        Params_UnknownAudioV0, graphql_name='unknownAudioV0')
    custom = sgqlc.types.Field(Params_Custom, graphql_name='custom')


class RequestedPromptsOrderBy(sgqlc.types.Input):
    __schema__ = worker
    __field_names__ = ('order_by', 'direction')
    order_by = sgqlc.types.Field(PromptsOrderBy, graphql_name='orderBy')
    direction = sgqlc.types.Field(OrderByDirection, graphql_name='direction')


########################################################################
# Output Objects and Interfaces
########################################################################
class ApiKey(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('id', 'associated_user')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    associated_user = sgqlc.types.Field(
        sgqlc.types.non_null('User'), graphql_name='associatedUser')


class Audio(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('url',)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class Image(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('url',)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class Mutation(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('request_new_job', 'post_job_result')
    request_new_job = sgqlc.types.Field('PromptRequest', graphql_name='requestNewJob', args=sgqlc.types.ArgDict((
        ('job_type', sgqlc.types.Arg(JobType, graphql_name='jobType', default=None)),
    ))
    )
    post_job_result = sgqlc.types.Field('SuccessResult', graphql_name='postJobResult', args=sgqlc.types.ArgDict((
        ('job_type', sgqlc.types.Arg(JobResult, graphql_name='jobType', default=None)),
    ))
    )


class PromptRequest(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('_user_id', 'id', 'prompt', 'params',
                       'result', 'user', 'model_type', 'status', 'created_at')
    _user_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='_userId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    prompt = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='prompt')
    params = sgqlc.types.Field('RequestModelParams', graphql_name='params')
    result = sgqlc.types.Field('PromptResult', graphql_name='result')
    user = sgqlc.types.Field('User', graphql_name='user')
    model_type = sgqlc.types.Field(
        sgqlc.types.non_null(ModelType), graphql_name='modelType')
    status = sgqlc.types.Field(sgqlc.types.non_null(
        PromptRequestStatus), graphql_name='status')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')


class Query(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('jobs', 'user')
    jobs = sgqlc.types.Field(sgqlc.types.list_of(
        PromptRequest), graphql_name='jobs')
    user = sgqlc.types.Field('User', graphql_name='user')


class ResultAsset(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('url',)
    url = sgqlc.types.Field(String, graphql_name='url')


class ResultParams_Custom(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('jsonb',)
    jsonb = sgqlc.types.Field(String, graphql_name='jsonb')


class ResultParams_StableDiffusionV1_4(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('action', 'prompt', 'width', 'height', 'cfg_scale',
                       'steps', 'n_samples', 'sampler', 'seed', 'input_image')
    action = sgqlc.types.Field(sgqlc.types.non_null(
        Params_StableDiffusionV1_4_Action), graphql_name='action')
    prompt = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='prompt')
    width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='width')
    height = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='height')
    cfg_scale = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='cfgScale')
    steps = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='steps')
    n_samples = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='nSamples')
    sampler = sgqlc.types.Field(sgqlc.types.non_null(
        Params_StableDiffusionV1_4_Sampler), graphql_name='sampler')
    seed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='seed')
    input_image = sgqlc.types.Field(ResultAsset, graphql_name='inputImage')


class ResultParams_UnknownAudioV0(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('n_samples',)
    n_samples = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='nSamples')


class Result_StableDiffusionV1_4(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('id', 'images', 'request')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    images = sgqlc.types.Field(sgqlc.types.non_null(
        sgqlc.types.list_of(sgqlc.types.non_null(Image))), graphql_name='images')
    request = sgqlc.types.Field(sgqlc.types.non_null(
        PromptRequest), graphql_name='request')


class Result_UnknownAudioV0(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('id', 'audio_files', 'request')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    audio_files = sgqlc.types.Field(sgqlc.types.non_null(
        sgqlc.types.list_of(sgqlc.types.non_null(Audio))), graphql_name='audioFiles')
    request = sgqlc.types.Field(sgqlc.types.non_null(
        PromptRequest), graphql_name='request')


class SuccessResult(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('message',)
    message = sgqlc.types.Field(String, graphql_name='message')


class User(sgqlc.types.Type):
    __schema__ = worker
    __field_names__ = ('id', 'api_keys', 'requested_prompts')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    api_keys = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(ApiKey)), graphql_name='apiKeys')
    requested_prompts = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(PromptRequest)), graphql_name='requestedPrompts')


########################################################################
# Unions
########################################################################
class PromptResult(sgqlc.types.Union):
    __schema__ = worker
    __types__ = (Result_UnknownAudioV0, Result_StableDiffusionV1_4)


class RequestModelParams(sgqlc.types.Union):
    __schema__ = worker
    __types__ = (ResultParams_StableDiffusionV1_4,
                 ResultParams_UnknownAudioV0, ResultParams_Custom)


########################################################################
# Schema Entry Points
########################################################################
worker.query_type = Query
worker.mutation_type = Mutation
worker.subscription_type = None
