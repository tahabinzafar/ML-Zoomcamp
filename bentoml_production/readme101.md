
## Deployment

- After installing libraries locally run
```bash
  bentoml build
```
- It will create local bentoml folder containing all dependencies required to run this project

Build docker image
```bash
  bentoml containerize <classifer:tag>
```
- Then you can run the image using
```bash
  docker run <classifier:tag>
```
- I faced unpickling error, had to specify scikit-learn==1.0.2 in bentofile.yaml
