import requests

# Đường dẫn đến API
url = "http://localhost:5000/predict"

# Dữ liệu JSON cần gửi
data = {
    "text": "Sản phẩm rất tuyệt vời!"
}

# Gửi yêu cầu POST với dữ liệu JSON
response = requests.post(url, json=data)

# In ra kết quả trả về
print(response.json())
