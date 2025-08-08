from .LCM_SM import *
from .AC_combos import *
from .LCM_SM_AD import *
from .AC_LCM_SAMPLER import *
from .AC_Taesd_Decoder import *
from .AC_WEBUI_PROMPT_TRY import *
from .AC_WB_Advance import *
from .AC_Latent import *
from .AC_SC_LATENT import *

NODE_CLASS_MAPPINGS = {
    "AC_LCM采样器":LCM_KSampler,
    "AC_Lora加载器": LoraLoaderWithImages,
    "AC_Checkpoint加载器": CheckpointLoaderSimpleWithImages,
    "AC_LCM_Adcance":AC_KSampler_Lcm_Advanced,
    "AC_LCM_Sampler采样器":AC_SamplerLCM,
    "AC_VAE加载":AC_TAESD_VAELoader,
    "AC_WEBUI格式提示词(测试)": AC_WEBUI_Prompt,
    "AC_Stable Diffusion格式提示词": AdvancedCLIPTextEncode,
    "AC_Stable DiffusionXL格式提示词": AdvancedCLIPTextEncodeSDXL,
    "AC_A格式参数条件": AddCLIPSDXLParams,
    "AC_B格式参数条件": AddCLIPSDXLRParams,
    "AC_EMPT_LATENT":AC_EmptyLatentImage,
    "AC_UPSCALE_LATENT": AC_SC_LATENT,
    # "📁AC_VAE_CK": AC_VAE,

}

# print("AC_FUNV5.0工具加载中......")
# print("Stable DiffusionByAC_FUN")
# print("哔哩哔哩：惠和设计-啊程")
