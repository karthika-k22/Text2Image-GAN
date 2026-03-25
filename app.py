import gradio as gr
from huggingface_hub import InferenceClient
import os

# --- CONFIGURATION ---
# We use os.environ to get the token you pasted into Render's settings earlier
hf_token = os.environ.get("HF_TOKEN")
client = InferenceClient(token=hf_token)

# --- ENGINE ---
def generate_image(prompt):
    if not hf_token:
        return None, "❌ Error: HF_TOKEN environment variable not set in Render!"

    try:
        # Using the exact model from your Colab code
        image = client.text_to_image(
            prompt, 
            model="stabilityai/stable-diffusion-xl-base-1.0"
        )
        return image, "✨ Generation Successful!"
    except Exception as e:
        return None, f"❌ Connection Error: {e}\nNote: The model might be loading (takes ~20s)."

# --- GRADIO UI (The Web Interface) ---
with gr.Blocks(theme=gr.themes.Soft(primary_hue="green")) as demo:
    gr.HTML("<h2>AI Image Dashboard</h2><p>Using Hugging Face Inference Router</p>")
    
    with gr.Row():
        with gr.Column(scale=2):
            text_input = gr.Textbox(
                value='a blue rose in a crystal vase, cinematic lighting, 8k',
                placeholder='Describe your image...',
                label="Prompt"
            )
            gen_button = gr.Button("Generate", variant="primary")
            status_msg = gr.Markdown()
            
        with gr.Column(scale=1):
            image_output = gr.Image(label="Generated Result", type="pil")

    # Connect the button click to our function
    gen_button.click(
        fn=generate_image,
        inputs=text_input,
        outputs=[image_output, status_msg]
    )

# --- RENDER DEPLOYMENT SETTINGS ---
if __name__ == "__main__":
    # Render requires these specific port and host settings
    demo.launch(server_name="0.0.0.0", server_port=10000)
