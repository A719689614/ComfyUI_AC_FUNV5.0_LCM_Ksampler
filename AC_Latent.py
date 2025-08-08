from .AC_FUN_CateGory import ac_category
import torch

MAX_RESOLUTION = 8196

list = ['512*512', '576*576', '640*640', '640*480', '480*640','512*768', '768*512','768*768', 
        '896*896','512*960', '512*1024', '1024*512', '768*1280', '1280*768','720*1280', 
        '1280*720', '1024*1536','1536*1024', '1080*1920', '1920*1080', '2048*1536' ,'1536*2048', 
        '3200*2048', '2048*3200','3840*1600', '1600*3840', '3840*2400', '2400*3840', '3480*2600',
        '2600*3480', '4096*3072', '3072*4096', '4515*3386', '5120*3840', '5120*4090','6400*4800'
        ]

# print(list)



# ========================================================
class AC_EmptyLatentImage:
    def __init__(self, device="cpu"):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "Resolution": (list,),
                              
                              "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})}}
    RETURN_TYPES = ("LATENT","STRING")
    RETURN_NAMES = ("LATENT","Help")
    FUNCTION = "generate"

    CATEGORY = ac_category()

    def generate(self, Resolution, batch_size=1):
        str = Resolution
        list = str.split('*')
        width, height = list[0],list[1]
        width, height = int(width),int(height)
        new_str =f"{width},{height}"
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        return ({"samples":latent},new_str )