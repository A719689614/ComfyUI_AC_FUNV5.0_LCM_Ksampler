from .LCM_SM import *
from .AC_combos import *
from .LCM_SM_AD import *


NODE_CLASS_MAPPINGS = {
    "📊AC_LCM采样器":LCM_KSampler,
    "📟AC_Lora加载器": LoraLoaderWithImages,
    "📺AC_Checkpoint加载器": CheckpointLoaderSimpleWithImages,
    "📈AC_LCM_Adcance":AC_KSampler_Lcm_Advanced,

}

print("AC_FUNV5.0工具加载中......")
print("哔哩哔哩：惠和设计-啊程")