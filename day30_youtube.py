import streamlit as st


# Sidebar
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}

with st.sidebar:
    st.header('Settings')
    selected_img_dict = st.selectbox(
        'Select image quality',
        ['Max', 'High', 'Medium', 'Standard']
    )

img_quality = img_dict[selected_img_dict]

# Main
st.title(':frame_with_picture: yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
    st.write('This app retrieves the thumbnail image from a YouTube video.')

youtube_url = st.text_input(
    'Paste YouTube URL',
    'https://youtu.be/JwSS70SZdyM'
)

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid

# サムネイルの表示
if youtube_url != '':

    ytid = get_ytid(youtube_url)
    yt_img = f'https://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
    st.image(yt_img)
    st.write('YouTube video thumbnail image URL:', yt_img)
