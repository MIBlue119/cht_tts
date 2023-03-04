# CHT TTS

Use streamlit app to build a simple tts demo page


## Usage

- Run at local

  - install dependencies with: `pip install -r requirements.txt`
  - apply the cht key: https://iot.cht.com.tw/iot/developer
  - set your api key with: `export CHT_API_KEY="xxxx"`
  - run with `streamlit run app.py`
- Deploy at [streamlit.io](https://streamlit.io/)

  - streamlit is backed up by Snowflake[a data platform]
  - Fork the repository to your github
  - Register to [streamlit.io](https://streamlit.io/) with your github account
  - Click the `New App`  button
  - Select  the forked repository
  - Set the `Advanced Setting`
    - select with `python 3.8`
    - set the API_KEY to the secret
      ```
      CHT_API_KEY = "your_api_key"
      ```
