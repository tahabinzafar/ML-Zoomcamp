# Midterm Project

Project contains EDA and model implementation of HR data of an organization. Main goal is to study the churn behaviour and make a predictive model that generates churn probabilities of any employee record sent to it in format discussed in "test_sample.ipynb" notebook.

## For EDA; notebook.ipynb

- Please go through the analysis in the notebook.ipynb to understand the data through visual and numerical data analysis.

## Run train.py script (IMPORTANT!!)

- Run train.py script, it will save the model locally, you will get the output of last cell as follows;

"Model(tag="employee_churn_model:gvpuglsym6okp7ir", path="/home/user/bentoml/models/employee_churn_model/gvpuglsym6okp7ir/")"

(Note that tag specified with model name would be different everytime, hence we have used "employee_churn_model:latest" to get latest tag in service.py)


## Run web service locally

- Activate the virtual environment in project directory, using
```bash
  pipenv shell
```
- Then run following command in project directory
```bash
  bentoml serve service.py:svc --production --reload
```
- Make sure to pass input in format mentioned in "test_sample.ipynb" notebook or else an error would be generated, example;

```bash
{
  "satisfaction_level": 0.38, #float (0-1)
  "last_evaluation": 0.53, #float (0-1)
  "number_project": 2, #int (trained on 2-7 projects)
  "average_montly_hours": 143, #int (trained on 96 - 310 hours)
  "time_spend_company": 3, #int (trained on 2 to 10 years)
  "Work_accident": 0, #int (trained on 0:no or 1:yes)
  "promotion_last_5years": 0, #int (trained on 0:no or 1:yes)
  "dept": "sales", #str (Please see test_samples for range of departments initials)
  "salary": "low", #str (low,medium or high)
  "satisfaction_category": "low", #str (set it to "low" if satisfaction level < 0.5, or "high" if > = 0.5)
  "employee_work_load": "unburdened" #str ("unburdened": projects = 2, "ideal": projects=3,4 or 5, "overburdened": projects=6,7 or more)
}
```
More details about range of values and data types of each input field is discussed briefly in the "test_sample.ipynb" notebook. Please refer to it for more clarity

## Run web service using Docker

- Activate the virtual environment in project directory, using
```bash
  pipenv shell
```
- After creating environment, we will create local bentoml folder containing all dependencies needed to create a docker image
```bash
  bentoml build
```
(Note down the "< tag >" specified to the image as you would need that to containerize your service)
  
- Build docker image
```bash
  bentoml containerize employee_churn_classifer:<tag>
```
- Then you can run the image using
```bash
  docker run -it --rm -p 3000:3000 employee_churn_classifier:<tag> serve --production
```
- Run following command to see description about image created. Size of image in my environment is 884MB
```bash
  docker images
```
- Make sure to pass input in format mentioned in "test_sample.ipynb" notebook or else an error would be generated


## Important Note 

- I faced unpickling error, had to specify scikit-learn==1.0.2 in bentofile.yaml


## Screenshots

### Not Churn output

[![not-churn.png](https://i.postimg.cc/9FdvGgzd/not-churn.png)](https://postimg.cc/VdNGwRqv)

### Churn output

[![churn.png](https://i.postimg.cc/x17yqnYt/churn.png)](https://postimg.cc/jDHJFVD7)






