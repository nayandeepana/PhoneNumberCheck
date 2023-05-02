import requests
number=input('Enter your Number : ')
url = f"https://api.apilayer.com/number_verification/validate?number=91{number}"

payload = {}
headers= {
  "apikey": "e7sMm91j1dnoWldntUQPMcylQD4MOKP6"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)