import requests

#r = requests.get('http://127.0.0.1:5000/info')
#print(r.status_code)
#print(r.text)
'''
out_data = {'name': 'Ruotong Li',
            'hdl_value': 150}
r = requests.post('http://127.0.0.1:5000/hdl_check', json=out_data)
print(r.status_code)
print(r.text)

out_data = {'a': 5,
            'b': 12}
r = requests.post('http://127.0.0.1:5000/addition', json=out_data)
print(r.status_code)
print(r.text)
answer = r.json()
'''

r = requests.get('http://127.0.0.1:5000/add/2/3')
print(r.status_code)
print(r.text)