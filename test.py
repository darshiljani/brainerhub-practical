import requests

url = "http://localhost:8000/import/"
file_path = "./details.xlsx"

files = {"file": open(file_path, "rb")}

res = requests.post(url, files=files)
print(res.json())
