import streamlit as st
import numpy as np

st.title(":tv: Media Tester")
st.write("Testing all media elements in one place.")

st.write("**Image - static image should appear:**")
image_nums = np.random.randint(255, size=(144, 144), dtype=np.uint8)
st.image(image_nums, caption='Example image caption')


st.write("**Audio - empty audio should appear:**")
audio_video_data = np.random.uniform(-1, 1, 44100)
st.audio(audio_video_data, sample_rate=44100)


st.write("**Video - empty video should appear:**")
st.video(audio_video_data)