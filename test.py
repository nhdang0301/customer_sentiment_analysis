import requests
# Đường dẫn đến API
url = "https://customer-sentiment.onrender.com/predict"

# Dữ liệu JSON cần gửi
data = {
    "texts": [
        "Tôi rất hạnh phúc khi được tham gia khóa học này.",
        "Tôi không thích cách học trực tuyến này lắm."
    ]
}


# Gửi yêu cầu POST với dữ liệu JSON
response = requests.post(url, json=data)

# In ra kết quả trả về
print(response.json())
