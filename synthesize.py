"""
Use cht's taiwanese tts engine to generate taiwanese tts
api: https://iot.cht.com.tw/iot/developer 

"""
import urllib
import urllib.request
import io
from pydub import AudioSegment

def get_speaker(gender="female"):
    support_speaker = {
        "female": "lsj",
        "male": "tc"
    }
    return support_speaker[gender]

def generate_taiwanese_tts(text,speaker_gender, X_API_KEY):
    """Generate taiwanese tts"""
    # Convert text to url encoding
    text_encoded = urllib.parse.quote(text)
    speaker = get_speaker(speaker_gender)
    url = f"https://iot.cht.com.tw/apis/CHTIoT/tts/v1/ch/synthesisRaw?inputText={text_encoded}&speaker={speaker}"
    headers = {"X-API-KEY": X_API_KEY}
    # Send request
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    # Write response to file in memory
    audio = io.BytesIO(response.read())

    # Convert audio to mp3 format
    sound = AudioSegment.from_file(audio, format="wav")
    output_audio = io.BytesIO()
    sound.export(output_audio, format="mp3")
    output_audio.seek(0)

    return output_audio