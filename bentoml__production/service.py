import numpy as np
from pydantic import BaseModel
import bentoml
from bentoml.io import JSON

class CreditApplication(BaseModel):
    seniority: int
    home: str
    time: int
    age: int
    marital: str
    records: str
    job: str
    expenses: int
    income: float
    assets: float
    debt: float
    amount: int
    price: int

model_ref = bentoml.xgboost.get("credit_risk_model:latest")
dv = model_ref.custom_objects['dictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service("credit_risk_classifier", runners=[model_runner])


@svc.api(input=JSON(pydantic_model=CreditApplication), output=JSON())

#now we receive CreditApplication in classify

async def classify(credit_application):
#def classify(credit_application):

    application_data=credit_application.dict()
    vector = dv.transform(application_data)
    prediction = await model_runner.predict.async_run(vector)
    #prediction = model_runner.predict.run(vector)
    result = prediction[0]

    if result > 0.5:

        return {
            "status": "DECLINED",
            "result": result
        }
    elif result > 0.25:
        return {
            "status": "MAYBE",
            "result": result
        }
    else:
        return {
            "status": "APPROVED",
            "result": result
        }