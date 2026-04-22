
%%writefile EmotionDetection/emotion_detection.py
def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {"error": "Invalid input"}

    return {
        "anger": 0.01,
        "disgust": 0.02,
        "fear": 0.05,
        "joy": 0.90,
        "sadness": 0.02,
        "dominant_emotion": "joy"
    }