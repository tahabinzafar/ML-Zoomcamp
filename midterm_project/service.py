import numpy as np
from pydantic import BaseModel
import bentoml
from bentoml.io import JSON


class ChurnApplication(BaseModel):

    
    satisfaction_level: float
    last_evaluation: float
    number_project: int 
    average_montly_hours: int
    time_spend_company: int
    Work_accident: int
    promotion_last_5years: int
    dept: str
    salary: str
    satisfaction_category: str
    employee_work_load: str


model_ref = bentoml.sklearn.get("employee_churn_model:latest")
dv = model_ref.custom_objects['dictVectorizer']
model_runner = model_ref.to_runner()

svc = bentoml.Service("employee_churn_classifier", runners=[model_runner])


@svc.api(input=JSON(pydantic_model=ChurnApplication), output=JSON())

#now we receive ChurnApplication in classify

async def classify(churn_application):
#def classify(churn_application):

    application_data=churn_application.dict()
    vector = dv.transform(application_data)
    prediction = await model_runner.predict_proba.async_run(vector)
    #prediction = model_runner.predict.run(vector)
    result=prediction[:,1]
    
    if result >= 0.5:

        return {
            "Churn": "Very Likely to Churn (High Risk)",
            "result": result
        }
    elif result >= 0.25:
        return {
            "status": "Less Risk of Churn (Cautious)",
            "result": result
        }
    else:
        return {
            "status": "Not at Risk",
            "result": result
        }