from flask import Flask, request, jsonify
from transformers import pipeline

# Tạo pipeline để phân loại cảm xúc sử dụng mô hình trực tiếp từ Hugging Face
sentiment_pipeline = pipeline(
    "text-classification", model="5CD-AI/Vietnamese-Sentiment-visobert")

# Tạo Flask app
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    texts = data.get('texts', [])  # Lấy danh sách các câu văn bản từ JSON

    # Sử dụng pipeline để phân tích cảm xúc cho từng câu trong danh sách
    results = []
    for text in texts:
        prediction = sentiment_pipeline(text)
        results.append(prediction[0])
    return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
