## Midterm Project

Project contains EDA and model implementation of HR data of an organization. Main goal is to study the churn behaviour and make a predictive model that generates churn probabilities of any employee record sent to it in format discussed in "test_sample.ipynb" notebook. 

### For EDA; notebook.ipynb

- Please go through the analysis in the notebook to understand the data through visual and numerical data analysis

### Run train.py script (IMPORTANT!!)

- Run train.py script, it will save the model locally in your home directory
"Model(tag="employee_churn_model:gvpuglsym6okp7ir", path="/home/user/bentoml/models/employee_churn_model/gvpuglsym6okp7ir/")"
(Please note that tag specified with model name would be different everytime, hence we have used "employee_churn_model:latest" to get latest tag in service.py)


### Run web service locally

- Activate the virtual environment in project directory, using
```bash
  pipenv shell
```
- Then run following command in project directory
```bash
  bentoml serve service.py:svc --production --reload
```
- Make sure to pass input in format mentioned in "test_sample.ipynb" notebook or else an error would be generated

### Run web service using a container

- Activate the virtual environment in project directory, using
```bash
  pipenv shell
```
- After all libraries installed run
```bash
  bentoml build
```
- It will create local bentoml folder containing all dependencies needed to create docker image

- Build docker image
```bash
  bentoml containerize employee_churn_classifer:tag
```
- Then you can run the image using
```bash
  docker run -it --rm -p 3000:3000 employee_churn_classifier:tag serve --production
```
- Run following command to see description about image created. Size of image is around 884MB
```bash
  docker images
```
- Make sure to pass input in format mentioned in "test_sample.ipynb" notebook or else an error would be generated


### Important Note 

- I faced unpickling error, had to specify scikit-learn==1.0.2 in bentofile.yaml


### Screenshots

Not Churn

[![not-churn.png](https://i.postimg.cc/9FdvGgzd/not-churn.png)](https://postimg.cc/VdNGwRqv)

Churn

[![churn.png](https://i.postimg.cc/x17yqnYt/churn.png)](https://postimg.cc/jDHJFVD7)






