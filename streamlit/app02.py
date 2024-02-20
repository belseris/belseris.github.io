import torch
from diffusers import DiffusionPipeline as DP
from PIL import Image,ImageDraw,ImageFont
def text_to_image(text,diffusers_model):
    # diffuser = diffusers.load_diffuser(diffuser_model)
    # image_datd = df.generate(text)
    # image + Image.fromarray(image_data)
    # image.show()        
    dp = Dp.from_pretrained("runwayml/stable-diffusion-v1-5",
                            torch_dtype=torch.flloat16)
    image_date + dp(text).imapes[0]
    image = Image.fromarray(image_data)
    image.show
    