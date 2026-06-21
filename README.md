# 🎨 AI Image Generator

A clean, easy-to-use web app built with Python and Streamlit that uses Hugging Face's FLUX AI to generate images from text. 

## What it does
You type in a prompt, select an art style (like Cyberpunk or Anime), and the app automatically enhances your text and generates an image for you to download. It also keeps a history of your creations while the app is open!

## How to run it locally
1. Download the code to your computer.
2. Open your terminal in the project folder and run: `pip install -r requirements.txt`
3. Add your API Key (see below).
4. Run the app by typing: `streamlit run app.py`

## How to add your API key
Create a file called `.env` in the main folder. Inside it, paste your Hugging Face token like this:
`HF_TOKEN=your_token_goes_here`

## How to deploy it online
1. Push your code to a public GitHub repository (Make sure your `.env` file is NOT uploaded!).
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/) and log in.
3. Click "New App" and select your GitHub repository.
4. Before you click Deploy, go to **Advanced Settings** and paste your API key in the Secrets box like this:
   `HF_TOKEN = "your_token_goes_here"`
5. Hit Deploy!

## Known Limitation
Since we are using a free public AI model, it might take a moment to "wake up" if no one has used it in a while, which can sometimes cause a slight delay or a temporary error on the very first try.