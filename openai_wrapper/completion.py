from typing import Self, Protocol
import openai

from enum import Enum

from dataclasses import dataclass


@dataclass
class ChatCompletionResponseChoicesMessage:
    role : str 
    content : str
    
    
@dataclass 
class ChatCompletionResponseChoices:
    index : int
    message : ChatCompletionResponseChoicesMessage
    finish_reason : str
    
    
@dataclass 
class ChatCompletionResponseUsage:
    prompt_tokens : int
    completion_tokens : int
    total_tokens : int


@dataclass
class ChatCompletionResponse:
    id : str 
    object : str
    model : str
    choices : ChatCompletionResponseChoices
    usage : ChatCompletionResponseUsage



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

    
class ChatCompletionMessage(Protocol):
    message : dict[str, str]
    
    def __init__(self, *, content : str) -> None:
        ...
        
    
    def __build(self) -> dict[str, str]:
        ...
    
    
class UserCompletionMessage(ChatCompletionMessage):
    def __init__(self, *, content : str) -> None:
        self.message = self.__build(content=content)
    
    def __build(self, *, content : str) -> dict[str, str]:
        return {"role": Roles.USER.value, "content": content}
    

class SystemCompletionMessage(ChatCompletionMessage):
    def __init__(self, *, content : str) -> None:
        self.message = self.__build(content=content)
    
    
    def __build(self, *, content : str) -> dict[str, str]:
        return {"role": Roles.SYSTEM.value, "content": content}
    


class ChatCompletion:
    def __init__(self, model : Models) -> None:
        self.model = model.value
        self.messages : list[dict[str, str]] = []
        
        self.temperature = 1
        self.n = 1
        self.max_tokens = None
        
        
    def __add_message(self, content : dict[str, str]) -> Self:
        self.messages.append(content)

        return self
    
    def __add_messages(self, *contents : dict[str, str]) -> Self:
        self.messages.extend(contents)
        
        return self
    
    
    def __set_temperature(self, temperature : float) -> Self:
        MIN_TEMPERATURE = 0
        MAX_TEMPERATURE = 2
        
        if not MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE:
            raise ValueError("temperature must be between 0 and 2")
        
        self.temperature = temperature
        
        return self
    
    def __set_n(self, n : int) -> Self:
        self.n = n
        
        return self
    
    def __set_max_tokens(self, max_tokens : int) -> Self:
        self.max_tokens = max_tokens
        
        return self    
    
    
    def generate(self) -> ChatCompletionResponse:
        params = {
            "model": self.model,
            "messages": self.messages,
            "temperature": self.temperature,
            "n": self.n,
        }
        
        if self.max_tokens is not None:
            params["max_tokens"] = self.max_tokens
            
        
        response = openai.ChatCompletion.create(**params)
        
        final_response = ChatCompletionResponse(
            id = response['id'],
            object = response['object'],
            model = response['model'],
            choices = ChatCompletionResponseChoices(
                index = response['choices'][0]['index'],
                message = ChatCompletionResponseChoicesMessage(
                    role = response['choices'][0]['message']['role'],
                    content = response['choices'][0]['message']['content']   
                ),
                finish_reason = response['choices'][0]['finish_reason']
            ),
            usage = ChatCompletionResponseUsage(
                prompt_tokens = response["usage"]["prompt_tokens"],
                completion_tokens = response["usage"]["completion_tokens"],
                total_tokens = response["usage"]["total_tokens"]   
            )
        )
        
        
        return final_response
    
    
    
    @classmethod
    def create(
        cls,
        model : Models,
        messages : list[ChatCompletionMessage],
        temperature : float = 1.0,
        n : int = 1,        
    ) -> ChatCompletionResponse:
        chat_completion = ChatCompletion(model = model)
        
        chat_completion.__set_temperature(temperature)
        chat_completion.__set_n(n)
        
        for message in messages:
            chat_completion.__add_message(message.message)
            
        return chat_completion.generate()
    
        
    




if __name__ == "__main__":
    pass