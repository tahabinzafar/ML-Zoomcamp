import numpy as np
from pydantic import BaseModel
import bentoml
from bentoml.io import JSON
from bentoml.io import NumpyNdarray

#I have saved tags as model1 and model2 respectively
model_ref = bentoml.sklearn.get("mlzoomcamp_homework:model1")
#model_ref = bentoml.sklearn.get("mlzoomcamp_homework:model1")
model_runner = model_ref.to_runner()

svc = bentoml.Service("mlzoomcamp_classifier", runners = [model_runner])


@svc.api(input=NumpyNdarray(), output=JSON())

#now we receive CreditApplication in classify

async def classify(vector):
#def classify(credit_application):

    prediction = await model_runner.predict.async_run(vector)
    #prediction = model_runner.predict.run(vector)
    result = prediction[0]

    if result > 0.5:

        return {
            "status": "DECLINED",
            "result": result
        }

    else:
        return {
            "status": "APPROVED",
            "result": result
        }
