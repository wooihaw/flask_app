import requests


url = 'http://localhost:5000/rest_api'
try:
    r1 = requests.post(url, json={'height': 175, 'weight': 80})
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
else:
    if r1.status_code == 200:
        print(r1.json())
    else:
        print('Error!')

h, w = 160, 50
try:
    r2 = requests.get(url + f'?height={h}&weight={w}')
    # Alternative way to set the parameters
    # r2 = requests.get(url, params={'height': h, 'weight': w})
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
else:
    if r2.status_code == 200:
        print(r2.json())
    else:
        print('Error!')
