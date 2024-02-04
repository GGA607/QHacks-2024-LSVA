from flask import Flask, request

import transcribe as ts
import text_analysis as ta

app = Flask(__name__)

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    try:
        audio_file = request.files['audioFile']
        #transcribing the text
        text = ts.t_scribe(audio_file)

        sentiment = ta.get_analysis(text)

        return sentiment
    
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)