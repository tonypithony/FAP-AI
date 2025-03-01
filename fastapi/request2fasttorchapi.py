# Чтобы отправить изображение в формате Base64 с помощью библиотеки requests в Python, вам нужно сначала преобразовать изображение в строку Base64, а затем отправить его в POST-запросе. Вот пример, как это сделать:

# Преобразуйте изображение в строку Base64.
# Отправьте POST-запрос с этой строкой.

import requests
import base64

# Функция для преобразования изображения в строку Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Путь к вашему изображению
image_path = "ai.png"

# Преобразуем изображение в Base64
image_base64 = image_to_base64(image_path)

# URL вашего FastAPI сервиса
url = "http://192.168.100.90:6660/predict/"

# Отправляем POST-запрос
response = requests.post(url, json={"image": image_base64})

# Выводим статус-код и текст ответа
print("Status Code:", response.status_code)
print("Response Text:", response.text, '\n')

# Если статус-код 200, то пробуем декодировать JSON
if response.status_code == 200:
    decoded_text = response.json()
    # Выводим результат
    print(decoded_text['predicted_class_name'])
else:
    print("Error: Unable to decode JSON response.")

# "cap.jpg"

# Status Code: 200
# Response Text: {"predicted_class_index":724,"predicted_class_name":"pirate, pirate ship"} 

# pirate, pirate ship 

# jersey, T-shirt, tee shirt < linus.jpg
# water jug < linux.png
# comic book < ai.png
# king snake, kingsnake < slang.png
