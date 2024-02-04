from flask import Flask, request, jsonify

import transcribe as ts
import text_analysis as ta

app = Flask(__name__)

@app.route('/process_audio', methods=['POST']) 
def process_audio():
    try:
        audio_file = request.files['audioFile']
        
        # Log the confirmation that the audio file was received
        app.logger.info("Audio file received successfully.")

        # Transcribing the text
        text = ts.t_scribe(audio_file)

        sentiment = ta.get_analysis(text)

        # Return the sentiment as JSON
        return jsonify(sentiment=sentiment)
    
    except Exception as e:
        app.logger.error(f'Error: {str(e)}')
        return jsonify(error=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True, methods=['POST'])

