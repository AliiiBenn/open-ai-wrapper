from typing import Any, List, Union
import openai 

from dataclasses import dataclass


@dataclass
class Model:
    id : str
    object : str
    created : int
    owned_by : str
    persmission : List



def list() -> List[Model]:
    basic_models = openai.Model.list()
    basic_models_data : List[dict[str, Union[Any]]] = basic_models["data"]
    
    
    final_models : List[Model] = []
    
    
    for model in basic_models_data:
        final_models.append(
            Model(
                id=model["id"],
                object=model["object"],
                created=model["created"],
                owned_by=model["owned_by"],
                persmission=model["permission"]   
            )
        )
        
    return final_models



def retrieve(model : str) -> Model | None:
    basic_model = openai.Model.retrieve(model)
    final_model = Model(
        id=basic_model["id"],
        object=basic_model["object"],
        created=basic_model["created"],
        owned_by=basic_model["owned_by"],
        persmissions=basic_model["permissions"]   
    )

    return final_model