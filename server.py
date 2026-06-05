from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emot_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    text = (
        "For the given statement, the system response is " + 
        f"'anger': {res['anger']}, 'disgust': {res['disgust']}, " +
        f"'fear': {res['fear']}, 'joy': {res['joy']} and " +
        f"'sadness': {res['sadness']}. The dominant emotion is {res['dominant_emotion']}."
    )
    return text

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
