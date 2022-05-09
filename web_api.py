import requests
import json

api_key = 'b0382a9da8d31051dd5eecdc220673dc'
city = input("ჩაწერე ქალაქი: ")
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units-metric'

r = requests.get(url)
result_json = r.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=4)
print(res_structured)

m = res['main']
temp = m['temp']
humidity = m['humidity']
pressure = m['pressure']

print('ტემპერატურა: ', temp)
print('ტენიანობა: ', humidity, '%')
print('წნევა: ', pressure)