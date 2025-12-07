import os 
from dotenv import load_dotenv
from openai import OpenAI

from utils import image_to_base64

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
    base_url = "https://api.avalai.ir/v1"
)

image_path = r"data\be54b0b4-70c0-470d-b24a-67a7dacbc853-768x768.png"

base64_code = image_to_base64(
    image_path,
    format="PNG"
)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": """
                تمام متنی که در تصویر هست رو به صورت ساختار مارک داون بهم خروجی بده بدون حرف اضافه و فقط متنی که در تصویر هست رو خروجی بده
                """
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{base64_code}"
                }
            },
        ]
    }
]

response = client.chat.completions.create(
    model = "gemma-3-27b-it",
    messages = messages,
)

print(response.choices[0].message.content)