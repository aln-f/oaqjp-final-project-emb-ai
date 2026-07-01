'''Flask application for Emotion Detection.'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emot_detector():
    '''Run emotion detection on text (received from the HTML interface)
    and return 5 core emotions, their confidence scores, and the
    dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    if res['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    text = (
        "For the given statement, the system response is " + 
        f"'anger': {res['anger']}, 'disgust': {res['disgust']}, " +
        f"'fear': {res['fear']}, 'joy': {res['joy']} and " +
        f"'sadness': {res['sadness']}. " +
        f"The dominant emotion is {res['dominant_emotion']}."
    )
    return text

@app.route('/')
def index():
    '''Render the main application page.'''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
