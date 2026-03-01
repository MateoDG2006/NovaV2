import json
import logging

import requests
from pydantic import BaseModel


# Modelo para la solicitud
class Message(BaseModel):
    content: str

# Modelo para la respuesta
class ResponseModel(BaseModel):
    message: str
    model: str

class Model:
    def __init__(self, name: str, version: str, model_base_url: str):
        self.name = name
        self.model_base_url = model_base_url
        self.version = version

    def __str__(self):
        return f"{self.name} v{self.version}"
    
    def chat(self, message: Message) -> ResponseModel:
        """
        Envía un mensaje a un modelo y retorna la respuesta completa
        """
        logging.debug(f"chat() called with message: {message.content}")
        try:
            response = requests.post(
                f"{self.model_base_url}/api/generate",
                json={
                    "model": self.name,
                    "prompt": message.content,
                    "stream": False
                }
            )
            logging.debug(f"POST {self.model_base_url}/api/generate status={response.status_code}")
            response.raise_for_status()
            
            result = response.json()
            return ResponseModel(
                message=result.get("response", ""),
                model=self.name
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"chat() request failed: {e}")
            return ResponseModel(
                message=f"Error al conectar con el modelo: {str(e)}",
                model=self.name
            )

    async def chat_stream(self, message: Message):
        """
        Envía un mensaje a un modelo y retorna la respuesta en streaming
        """
        def generate():
            try:
                response = requests.post(
                    f"{self.model_base_url}/api/generate",
                    json={
                        "model": self.name,
                        "prompt": message.content,
                        "stream": True
                    },
                    stream=True
                )
                response.raise_for_status()
                
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line)
                        yield chunk.get("response", "")
                        
            except Exception as e:
                yield f"Error: {str(e)}"
        
        return generate()