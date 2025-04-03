# Step 1: Install Required Libraries
# !pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# !pip install diffusers transformers accelerate scipy safetensors

# Step 2: Import Required Libraries
import torch
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt

# Step 3: Load the Stable Diffusion Model
model_id = "runwayml/stable-diffusion-v1-5"  # Pretrained model from Hugging Face
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)  
pipe.to("cuda")  # Move model to GPU

print("✅ Model Loaded Successfully!")

# Step 4: Define Function to Generate Images
def generate_images(prompt, num_images=1, height=512, width=512, seed=42):
    torch.manual_seed(seed)  # Set seed for reproducibility
    images = pipe(prompt, num_images_per_prompt=num_images, height=height, width=width).images
    
    # Display Images
    fig, axes = plt.subplots(1, num_images, figsize=(5*num_images, 5))
    if num_images == 1:
        axes.imshow(images[0])
        axes.axis("off")
    else:
        for i, img in enumerate(images):
            axes[i].imshow(img)
            axes[i].axis("off")
    
    plt.show()
    return images

# Step 5: Generate Image from Text Prompt
prompt = "A futuristic cyberpunk city at night with neon lights"
images = generate_images(prompt, num_images=2, height=512, width=512, seed=123)

print("✅ Image Generation Completed!")
