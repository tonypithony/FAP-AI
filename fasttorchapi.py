# pip install torch torchvision
# pip install fastapi uvicorn requests

# https://www.restack.io/p/fastapi-answer-pytorch-integration

from fastapi import FastAPI, HTTPException
import torch
from torchvision import models, transforms
from PIL import Image
import io
import base64
from fastapi.responses import JSONResponse
import uvicorn
import asyncio

app = FastAPI()

# Загрузка предобученной модели
model = models.resnet50(pretrained=True)
model.eval()

# Определение преобразования для предварительной обработки входного изображения
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Список меток классов ImageNet
with open('imagenet-classes.txt','r') as f:
    imagenet_classes = f.read().splitlines()

# print(imagenet_classes[:5])

@app.post("/predict/")
async def predict(image: dict):
    try:
        # Получаем строку Base64 из запроса
        image_data = image['image']
        
        # Декодируем строку Base64
        image_bytes = base64.b64decode(image_data)
        
        # Открываем изображение
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image_tensor = preprocess(image).unsqueeze(0)
        
        with torch.no_grad():
            output = model(image_tensor)
        
        # Получаем индекс предсказанного класса
        predicted_class_index = output.argmax(dim=1).item()
        
        # Получаем имя класса из списка
        predicted_class_name = imagenet_classes[predicted_class_index]
        
        # Возвращаем предсказанный класс в формате JSON
        return JSONResponse(content={
                                    "predicted_class_index": predicted_class_index, 
                                    "predicted_class_name": predicted_class_name
                                    })
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("fasttorchapi:app", host="0.0.0.0", port=6660, reload=True)

# Объяснение кода:
# Функция image_to_base64: Эта функция открывает изображение в бинарном режиме, считывает его содержимое и кодирует в строку Base64.
# Путь к изображению: Укажите путь к изображению, которое вы хотите отправить.
# Отправка POST-запроса: Используйте requests.post для отправки POST-запроса на ваш FastAPI сервер. В данном случае мы передаем JSON-объект, содержащий строку Base64.
# Вывод ответа: После отправки запроса выводим ответ от сервера.