# 🎨 AI Image Generator

A clean, easy-to-use web app built with Python and Streamlit that uses Hugging Face's FLUX AI to generate high-fidelity images from text prompts.

## What it does
You type in a prompt, select an art style (like Cyberpunk or Anime), and the app automatically enhances your text with descriptive style keywords and generates an image for you to view or download. It also tracks your generation history using a neat, collapsible gallery at the bottom of the page.

---

## Code Architecture & Functions

To keep the project clean, scalable, and easy to maintain, the code is split across three distinct modules:

### 1. Style Engineering (`styles.py`)
This file defines how art styles are mapped to text descriptors, so the user doesn't have to manually type complex visual keywords.
* **`STYLE_MODIFIERS` (Dictionary):** Holds predefined descriptive string tokens (like lighting, resolution, and textures) for 5 distinct art styles: *Cyberpunk, Anime, Cinematic, Oil Painting,* and *Pixel Art*.
* **`apply_style(base_prompt, style_name)`:** * **Input:** The user's raw text prompt and their selected radio button style choice.
  * **Output:** Returns a single combined string, appending the specific art keywords to the user's prompt.

### 2. Backend API Integration (`api.py`)
This file strictly handles connection protocols and network requests to the Hugging Face AI servers.
* **`generate_image(final_prompt)`:**
  * **Input:** The fully styled text string from `styles.py`.
  * **Output:** A viewable Python Imaging Library (`PIL`) Image object.
  * **Logic:** Pulls the secret access token securely using `python-dotenv` (locally) or `st.secrets` (online). It then passes the token and prompt to Hugging Face’s official `InferenceClient` to run the `black-forest-labs/FLUX.1-schnell` model.

### 3. Frontend Web Application (`app.py`)
The main orchestrator of the web app. It builds the interactive visual interface.
* **`st.session_state.history`:** An internal list initialization that stores previously generated images and configurations so they persist during page updates.
* **Streamlit UI Layout:** Captures inputs using `st.text_input` and `st.radio`.
* **Execution Trigger:** When the "Generate Image" button is clicked, it cascades through `apply_style()`, fires `generate_image()`, renders the image using `st.image()`, and structures raw image bytes into an `st.download_button` asset.

---

## How to run it locally

1. **Clone or download** this project folder to your computer.
2. Open your terminal inside the project directory and run:
   ```bash
   pip install -r requirements.txt
