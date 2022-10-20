import requests

url = "http://0.0.0.0:9696/predict"

#customer = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
#customer={"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
customer={"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

response = requests.post(url, json=customer).json()
print(response)