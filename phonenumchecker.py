import requests 
import pandas as pd

number = +917708525127

url = f"https://api.veriphone.io/v2/verify?phone={number}&key=5B922C23E0A141EABF3B702645EA4DFF"   #key unknownmode mail

res = requests.get(url)

print(res.json())

file = pd.read_json()
