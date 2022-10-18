import requests


rg = requests.get('http://vcm-7631.vm.duke.edu:5002/get_patients/rl168')
print(rg.text)

rb1 = requests.get('http://vcm-7631.vm.duke.edu:5002/get_blood_type/M1')
rb2 = requests.get('http://vcm-7631.vm.duke.edu:5002/get_blood_type/F4')
print(rb1.text)
print(rb2.text)

output_info = {'Name': 'rl168',
               'Match': 'No'}
r = requests.post('http://vcm-7631.vm.duke.edu:5002/match_check', json = output_info)
print(r.text)

