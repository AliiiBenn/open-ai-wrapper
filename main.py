import dotenv, os
import openai

from openai_wrapper import UserCompletionMessage, Roles, Models





def main() -> None:
    dotenv.load_dotenv()
    
    API_KEY = os.getenv("OPENAI_API_KEY")
    
    if API_KEY is None:
        raise ValueError("OPENAI_API_KEY is not set")
    
    openai.api_key = API_KEY
    
    message = UserCompletionMessage.build(content="Hello, how are you?")
    
    response = openai.ChatCompletion.create(
        model=Models.GPT_3_5_TURBO_0613.value,
        messages=[message]
    )

    print(response["choices"][0]["message"]["content"])


if __name__ == "__main__":
    main()

