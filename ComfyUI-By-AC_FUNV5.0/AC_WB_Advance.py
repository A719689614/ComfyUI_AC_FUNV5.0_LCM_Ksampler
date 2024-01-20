from .AC_Encode import advanced_encode, advanced_encode_XL
MAX_RESOLUTION=8199
from .AC_FUN_CateGory import ac_category




AC_list = ["Stable diffusion", "ComfyUI", "Compel", "Comfy++" ,"Down_Weight"]
class AdvancedCLIPTextEncode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "text": ("STRING", {"multiline": True}),
            "clip": ("CLIP", ),
            "token_normalization": (["none", "mean", "length", "length+mean"],),
            "weight_interpretation": (AC_list,),
            "tips":("STRING", {"multiline": False,"default":"把CLIP权重调整为stable diffusion的权重值"}),
 
            }}
    
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = ac_category()

    def encode(self, clip, text, token_normalization, weight_interpretation, affect_pooled='disable',tips=None):
        embeddings_final, pooled = advanced_encode(clip, text, token_normalization, weight_interpretation, w_max=1.0, apply_to_pooled=affect_pooled=='enable')
        return ([[embeddings_final, {"pooled_output": pooled}]], )

class AddCLIPSDXLParams:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "conditioning": ("CONDITIONING", ),
            "width": ("INT", {"default": 1024.0, "min": 0, "max": MAX_RESOLUTION}),
            "height": ("INT", {"default": 1024.0, "min": 0, "max": MAX_RESOLUTION}),
            "crop_w": ("INT", {"default": 0, "min": 0, "max": MAX_RESOLUTION}),
            "crop_h": ("INT", {"default": 0, "min": 0, "max": MAX_RESOLUTION}),
            "target_width": ("INT", {"default": 1024.0, "min": 0, "max": MAX_RESOLUTION}),
            "target_height": ("INT", {"default": 1024.0, "min": 0, "max": MAX_RESOLUTION}),
            }}
    
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = ac_category()

    def encode(self, conditioning, width, height, crop_w, crop_h, target_width, target_height):
        c = []
        for t in conditioning:
            n = [t[0], t[1].copy()]
            n[1]['width'] = width
            n[1]['height'] = height
            n[1]['crop_w'] = crop_w
            n[1]['crop_h'] = crop_h
            n[1]['target_width'] = target_width
            n[1]['target_height'] = target_height
            c.append(n)
        return (c,)
    
class AddCLIPSDXLRParams:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "conditioning": ("CONDITIONING", ),
            "width": ("INT", {"default": 1024.0, "min": 0, "max": MAX_RESOLUTION}),
            "height": ("INT", {"default": 1024.0, "min": 0, "max": MAX_RESOLUTION}),
            "ascore": ("FLOAT", {"default": 6.0, "min": 0.0, "max": 1000.0, "step": 0.01}),
            }}
    
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = ac_category()

    def encode(self, conditioning, width, height, ascore):
        c = []
        for t in conditioning:
            n = [t[0], t[1].copy()]
            n[1]['width'] = width
            n[1]['height'] = height
            n[1]['aesthetic_score'] = ascore
            c.append(n)
        return (c,)
        

class AdvancedCLIPTextEncodeSDXL:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "text_l": ("STRING", {"multiline": True}),
            "text_g": ("STRING", {"multiline": True}),
            "clip": ("CLIP", ),
            "token_normalization": (["none", "mean", "length", "length+mean"],),
            "weight_interpretation": (AC_list,),
            #"affect_pooled": (["disable", "enable"],),
            "balance": ("FLOAT", {"default": .5, "min": 0.0, "max": 1.0, "step": 0.01}),
            "tips":("STRING", {"multiline": False,"default":"把CLIP权重调整为stable diffusion的权重值"}),
            }}
    
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = ac_category()

    def encode(self, clip, text_l, text_g, token_normalization, weight_interpretation, balance, affect_pooled='disable',tips=None):
        embeddings_final, pooled = advanced_encode_XL(clip, text_l, text_g, token_normalization, weight_interpretation, w_max=1.0, clip_balance=balance, apply_to_pooled=affect_pooled == "enable")
        return ([[embeddings_final, {"pooled_output": pooled}]], )
        
    
