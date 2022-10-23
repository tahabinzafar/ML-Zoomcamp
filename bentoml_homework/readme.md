
## Deployment

- Run service.py

```bash
  bentoml serve service.py:svc --production --reload
 ```
- Then run locustfile.py

```bash
  locust -H http://localhost:3000
 ```
 - Switch between model1 and model2 tags by changing in service.py
  
  
