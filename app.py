import io
import streamlit as st
from api import generate_image
from styles import STYLE_MODIFIERS, apply_style

# Set up the look of the web page
st.set_page_config(page_title="AI Image Generator", page_icon="🎨", layout="centered")

st.title("🎨 AI Image Generator")
st.write("Type what you want to see, pick a style, and let the AI do the rest!")

# Create a memory for the app so it doesn't forget old images when it refreshes
if "history" not in st.session_state:
    st.session_state.history = []

# Create our input boxes
st.subheader("Your Canvas")
user_prompt = st.text_input("What should we draw?", placeholder="e.g., A cat riding a skateboard")
selected_style = st.radio("Pick an Art Style:", list(STYLE_MODIFIERS.keys()), horizontal=True)

# The big generate button
if st.button("Generate Image", type="primary"):
    if user_prompt == "":
        st.warning("Please type something to draw first!")
    else:
        # 1. Add the style keywords to the prompt
        ready_prompt = apply_style(user_prompt, selected_style)
        
        # 2. Show a loading spinner while we wait
        with st.spinner("Painting your picture..."):
            try:
                # 3. Get the image from our API file
                image = generate_image(ready_prompt)
                
                # 4. Show it on the screen
                st.image(image, caption=f"{user_prompt} ({selected_style})", use_container_width=True)
                
                # 5. Get the image ready for downloading
                img_bytes = io.BytesIO()
                image.save(img_bytes, format='PNG')
                
                st.download_button(
                    label="📥 Download your image",
                    data=img_bytes.getvalue(),
                    file_name="my_ai_art.png",
                    mime="image/png"
                )
                
                # 6. Save this to our history list
                st.session_state.history.insert(0, {
                    "prompt": user_prompt,
                    "style": selected_style,
                    "image": image
                })
                
            except Exception as e:
                st.error(f"Uh oh! {e}")

# Show the history gallery at the bottom
if st.session_state.history:
    st.markdown("---")
    st.subheader("📜 Past Creations")
    
    for item in st.session_state.history:
        # Create a clickable dropdown for past images
        with st.expander(f"{item['prompt']} - {item['style']}"):
            st.image(item['image'], use_container_width=True)