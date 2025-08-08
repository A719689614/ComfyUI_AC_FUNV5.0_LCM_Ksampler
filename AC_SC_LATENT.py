from .AC_FUN_CateGory import ac_category
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))


import comfy.diffusers_load
import comfy.samplers
import comfy.sample
import comfy.sd
import comfy.utils

import comfy.clip_vision

import comfy.model_management
from comfy.cli_args import args


import folder_paths
def before_node_execution():
    comfy.model_management.throw_exception_if_processing_interrupted()

def interrupt_processing(value=True):
    comfy.model_management.interrupt_current_processing(value)


class AC_SC_LATENT:
    upscale_methods = ["nearest-exact", "bilinear", "area", "bicubic", "bislerp"]
    crop_methods = ["disabled", "center"]
    resolution = ['512*512', '576*576', '640*640', '640*480', '480*640','512*768', '768*512','768*768', 
        '896*896','512*960', '512*1024', '1024*512', '768*1152', '1152*768','720*1280', 
        '1280*720', '768*1152', '1152*768','1536*1024', '1024*1536', '1080*1920','1280*1920',
          '1920*1280', '1920*1080', '2048*1536' ,'1536*2048', 
        '3200*2048', '2048*3200','3840*1600', '1600*3840', '3840*2400', '2400*3840', '3480*2600',
        '2600*3480', '4096*3072', '3072*4096', '4515*3386', '5120*3840', '5120*4090','6400*4800']

    @classmethod
    def INPUT_TYPES(cls):
        return {"required":
                {
                 "Samples": ("LATENT",), 
                 "upscale_method": (cls.upscale_methods,),
                 "Resolution": (cls.resolution,),
                 "crop": (cls.crop_methods,),
                 "tips":("STRING",{"default":"AC_SC_LA","multiline":False})
                }
                }
        
    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("LATENT",)
    CATEGORY = ac_category()
    FUNCTION = "ac_sc_latent"

    def ac_sc_latent(self,Samples,upscale_method,Resolution,crop,tips=None):

        s = Samples.copy()
        str = Resolution.split('*')
        width, height = str[0],str[1]
        width, height = int(width),int(height)
        s["samples"] = comfy.utils.common_upscale(Samples["samples"], width // 8, height // 8, upscale_method, crop)
        return (s,)



# class AC_VAE:
    
#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required":{
#             "samples": ("LATENT", ), 
#             "vae_check": {"vae_name":(folder_paths.get_filename_list("vae"),)},
#             "tips": ("STRING",{"default":"AC_FUN VAE自适应","multiline":False})
#             }
#         }
    
#     RETURN_TYPES = ("IMAGE",)
#     FUNCTION = "ac_vae"
#     CATEGORY = ac_category()
    
#     #TODO:
#     def ac_vae(self,vae_check,samples,tips=None):
#         vae_path = folder_paths.get_full_path("vae", vae_check)
#         vae = comfy.sd.VAE(ckpt_path=vae_path)
#         return (vae.decode(samples["samples"]), )