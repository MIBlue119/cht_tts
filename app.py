import os
from datetime import datetime
import base64
from pydub import AudioSegment
from synthesize import generate_taiwanese_tts
import streamlit as st

CHT_API_KEY = os.getenv("CHT_API_KEY")
if CHT_API_KEY is None:
    # Use streamlit secrets to set CHT_API_KEY
    CHT_API_KEY = st.secrets["CHT_API_KEY"]
def get_audio_download_link(audio_bytes_io):
    """Generates a link allowing the audio to be downloaded
	    in:  audio_bytes  io
	    out: href string
	"""
    audio_str = base64.b64encode(audio_bytes_io.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{audio_str}">Download result</a>'
    return href

def app():
    st.title("Traditional Chinese TTS")
    st.write("基於中華電信的中文TTS服務")

    # Get user input
    text = st.text_area("Enter text:")
    gender = st.selectbox("Select voice gender:", options=["female", "male"])
    X_API_KEY = CHT_API_KEY

    st.session_state["sythesized_result"]=None
    path="tmp"
    if "Synthesize Success" not in st.session_state:
        st.session_state["Synthesize Success"] = False    
    if os.path.exists(path) == False:
        os.mkdir(path)        


    # Generate TTS audio
    if st.button("Generate audio"):
        # Use the timestamp as the file name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_path_mp3 = f"output_{timestamp}.mp3"
        st.session_state["sythesized_audio_name"]=os.path.join(path, output_path_mp3)        

        if os.path.exists(st.session_state["sythesized_audio_name"]) == False:
            progress_text = "Operation in progress... Please wait."
            progress_bar = st.progress(0)
            sythesizing=st.markdown("Sythesizing...")
            message = st.markdown(" ")

            audio_data = generate_taiwanese_tts(text, gender, X_API_KEY)
            # Export audio to mp3 with pydub
            sound = AudioSegment.from_file(audio_data, format="mp3")
            sound.export(st.session_state["sythesized_audio_name"], format="mp3")
            progress_bar.progress(100)
            sythesizing.markdown("Sythesizing...Done")
            message.markdown(" ")

            st.audio(audio_data.getvalue(), format="audio/mp3")
        
        with open(st.session_state["sythesized_audio_name"],"rb") as f:
            st.session_state["sythesized_result"]=f.read()
        st.session_state["Synthesize Success"]=True



    # delete the file
    if st.session_state["Synthesize Success"]==True:
        try:
            os.remove(st.session_state["sythesized_audio_name"])
            for file in os.listdir(path):
                os.remove(os.path.join(path, file))
        except:
            pass 

    if st.session_state["Synthesize Success"]==True and st.session_state["sythesized_result"] is not None:
        download_button=st.download_button(
        label="Download",
        data=st.session_state["sythesized_result"],
        file_name=output_path_mp3,
        ) 
        

if __name__ == '__main__':
    app()
