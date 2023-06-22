from dataclasses import dataclass
import stat
import openai

from enum import Enum, auto
from abc import ABC, abstractmethod



class Models(Enum):
    GPT_4 = "gpt-4"
    GPT_4_0613 = "gpt-4-0613"
    GPT_4_32K = "gpt-4-32k"
    GPT_4_32K_0613 = "gpt-4-32k-0613"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_0613 = "gpt-3.5-turbo-0613"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"
    GPT_3_5_TURBO_16K_0613 = "gpt-3.5-turbo-16k-0613"


class Roles(Enum):
    SYSTEM = "system"
    USER = "user"

    
class ChatCompletionMessage(ABC):
    @staticmethod
    @abstractmethod
    def build(*, content : str) -> dict[str, str]:
        pass
    
    
class UserCompletionMessage(ChatCompletionMessage):
    @staticmethod
    def build(*, content : str) -> dict[str, str]:
        return {"role": Roles.USER.value, "content": content}
    

class SystemCompletionMessage(ChatCompletionMessage):
    @staticmethod
    def build(*, content : str) -> dict[str, str]:
        return {"role": Roles.SYSTEM.value, "content": content}
    

class ChatCompletion:
    def __init__(self,
                 model : Models,
                 messages : list[ChatCompletionMessage],
                 temperature : float = 1
                 ):
        
        self.model = model
        self.messages = messages
        self.temperature = temperature


if __name__ == "__main__":
    pass