
## Deployment

- After installing libraries locally run
```bash
  bentoml build
```
- It will create local bentoml folder containing all dependencies required to create docker image

Build docker image
```bash
  bentoml containerize credit_risk_classifer:tag
```
- Then you can run the image using
```bash
  docker run -it --rm -p 3000:3000 credit_risk_classifier:tag serve --production
```
- I faced unpickling error, had to specify scikit-learn==1.0.2 in bentofile.yaml

### Validating Performance

- Run locustfile.py using 
```bash
  locust -H http://localhost:3000
```
- Test your model's performance by generating webtraffic using locust web ui
