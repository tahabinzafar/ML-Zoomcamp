## Midterm Project

Project contains EDA and model implementation of HR data of an organization. Main goal is to study the churn behaviour and make a predictive model that generates churn probabilities of any employee record sent to it in format discussed in "test_sample.ipynb" notebook. 

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

- - After installing libraries locally run
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
- I faced unpickling error, had to specify scikit-learn==1.0.2 in bentofile.yaml

- Make sure to pass input in format mentioned in "test_sample.ipynb" notebook or else an error would be generated



