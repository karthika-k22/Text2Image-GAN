# Text2Image-GAN
An interactive Text-to-Image Generation Dashboard built in Google Colab using FLUX.1-schnell and Hugging Face's 2026 Inference Router. Includes a custom-styled CSS interface and local image export functionality.

🎨 **Image Creative Studio:**
A professional, interactive dashboard built in Google Colab that leverages state-of-the-art Latent Diffusion Models (LDM) to synthesize high-fidelity images from natural language text prompts.

🚀 **Features**
High-Fidelity Generation: Powered by FLUX.1-schnell via the Hugging Face 2026 Inference Router.

Modern UI: Attractive "Glassmorphism" interface with a Dark Mode aesthetic.

Direct Export: Integrated "Save to Device" button using Base64-encoded binary streams.

Interactive Controls: Dynamic text inputs and real-time generation feedback.

**🛠️ Tech Stack**
Language: Python 3.12

Frameworks: ipywidgets, huggingface_hub

Inference Engine: Hugging Face Inference Router

Environment: Google Colab

**📋 Installation & Setup**
1. Prerequisites
You will need a free Hugging Face API Token.

Go to Hugging Face Settings.

Create a Fine-grained Token with Inference Provider permissions enabled.

2. Google Colab Configuration
Open the .ipynb file in Google Colab.

Click the Key icon (🔑 Secrets) in the left sidebar.

Add a new secret named HF_TOKEN and paste your token.

Toggle Notebook access to ON.

**🧠 Methodology**
This project utilizes a decoupled architecture where the frontend (Colab UI) sends asynchronous requests to a remote GPU-accelerated server. The system bypasses legacy GAN limitations by using Latent Diffusion, which offers superior text-alignment and image quality.

**📝 Result**
The dashboard successfully synthesizes 1024×1024 images in under 30 seconds. 

**🤝 Contributing**
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
