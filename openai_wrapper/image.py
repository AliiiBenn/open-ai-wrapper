from typing import Optional, Self
import openai 

from enum import Enum
from dataclasses import dataclass


@dataclass
class ImageResponseData:
    url : str 


@dataclass
class ImageResponse:
    created : int 
    data : list[ImageResponseData]


class Size(Enum):
    TINY = "256x256"
    MIDDLE = "512x512"
    LARGE = "1024x1024"
    
    
class Format(Enum):
    URL = "url"   
    B64_JSON = "b64_json"


class Image:
    def __init__(self,
                 prompt : str,
                 n : Optional[int] = 1,
                 size : Optional[Size] = Size.LARGE,
                 response_format : Optional[Format] = Format.URL,
                 user : Optional[str] = "") -> None:
        
        
        self.__prompt = prompt
        self.__n = n
        self.__size = size.value
        self.__response_format = response_format.value
        self.__user = user
        
        
    def __repr__(self) -> str:
        return f"<Image prompt={self.__prompt} n={self.__n} size={self.__size} response_format={self.__response_format} user={self.__user}>"        
        

    def __generate(self) -> ImageResponse:
        response = openai.Image.create(
            prompt = self.__prompt,
            n = self.__n,
            size = self.__size,
            response_format = self.__response_format,
            user = self.__user
        )
        
        return ImageResponse(
            created = response["created"],
            data = [
                ImageResponseData(
                    url = response["data"][i]["url"]
                ) for i in range(len(response["data"]))
            ]
        )
                
    
    
    @classmethod
    def create(cls, 
               prompt : str,
               n : Optional[int] = 1,
               size : Optional[Size] = Size.LARGE,
               response_format : Optional[Format] = Format.URL,
               user : Optional[str] = "") -> ImageResponse:
        
        return cls(
            prompt = prompt,
            n = n,
            size = size,
            response_format = response_format,
            user = user
        ).__generate()
        