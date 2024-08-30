import requests

def emotion_detector(text_to_analyze):
  """
  Detects the emotion of the given text using the Watson NLP Emotion Predict function.

  Args:
      text_to_analyze: The text to be analyzed for emotion.

  Returns:
      The emotion detected in the text, as a string.
  """
  url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
  headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  data = { "raw_document": { "text": text_to_analyze } }

  response = requests.post(url, headers=headers, json=data)
  response.raise_for_status()  # Raise an exception for error status codes

  return response.json()['emotionPredictions'][0]['emotion']['document']['emotion']


# Test the function
text = "I am feeling happy today"
emotion = emotion_detector(text)
print(emotion)  # Output: {'joy': 0.9999999403953552, 'sadness': 1.0000001424921397e-07, 'fear': 1.0000001424921397e-07, 'disgust': 1.0000001424921397e-07, 'anger': 1.0000001424921397e-07}
