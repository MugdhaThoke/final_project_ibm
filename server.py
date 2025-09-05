"""Flask server for Emotion Detection application.
This server exposes an endpoint `/emotionDetector` that accepts
text input, processes it with the emotion detection module,
and returns emotion scores and the dominant emotion.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")
@app.route("/emotionDetector")
def emot_detector():
    """Endpoint that analyses emotions from user input text."""
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )
@app.route("/")
def render_index_page():
    """Render the index page with the user input form."""
    return render_template('inde x.html')

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    app.run(host="0.0.0.0", port=8080, debug=True)
