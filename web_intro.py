import requests
'''
r = requests.get('https://api.github.com/repos/ruotongli/BE547/branches')
print(r)
print(type(r))
# print(r.text)
if r.status_code == 200:
    answer = r.json()
    print(type(answer))
    for branch in answer:
        print(branch['name'])
else:
    print('Bad request: {}'.format(r.text))
'''

output_info = {'name': 'Ruotong Li',
               'net_id': 'rl168',
               'e-mail': 'ruotong.li@duke.edu'}
r = requests.post('http://vcm-21170.vm.duke.edu:5000/student', json = output_info)
print(r)
print(r.text)

'''
r = requests.post('http://vcm-21170.vm.duke.edu:5001/add_message', json = output_info)
output_info = {'user': 'echo',
               'message': 'hello'}

r = requests.post('http://vcm-21170.vm.duke.edu:5001/add_message', json = output_info)
print(r)
print(r.text)

rg = requests.get('http://vcm-21170.vm.duke.edu:5001/get_messages/Li')
print(rg.text)
'''