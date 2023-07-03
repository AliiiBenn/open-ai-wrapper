"""  

OpenAI API Wrapper

------------------

Very simple wrapper for the OpenAI API.



"""


__title__ = 'openai_wrapper'
__author__ = "AliBen"
__version__ = "0.0.1"

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import openai 




from openai_wrapper.api_ressources import (
    ChatCompletion,
    Models,
    UserCompletionMessage,
    SystemCompletionMessage
)

__all__ = [
    "ChatCompletion",
    "Models",
    "UserCompletionMessage",
    "SystemCompletionMessage"
]