def create_patient_entry(patient_name,patient_id,patient_age):
    patient_name = patient_name.split(' ')
    new_patient = {'First Name': patient_name[0], 'Last Name':patient_name[1],
    'ID': patient_id, 'Age': patient_age,'Tests': []}
    return new_patient

def main():
    db = {}
    db[1] = create_patient_entry('Ann Ables',1,30)
    db[2] = create_patient_entry('Bob Boyles',2,34)
    db[3] = create_patient_entry('Chris Chou',3,25)
    show_line(db)
    addition(db,1,'HDL',100)
    show_line(db)
    print('Patient {} is a {}'.format(get_full_name(db[2]),adult_or_minor(db[2])))
    #print(search(db,1))

    #room_list=['Room 1','Room 2','Room 3']

    #for i, patient in enumerate(db):
        #print('Name = [], Room = []'.format(patient[0],room_list[i]))

    #for patient,room in zip(db,room_list):
        #print('Name = [], Room = []'.format(patient[0],room)

def get_full_name(patient):
    full_name = '{} {}'.format(patient['First Name'],patient['Last Name'])
    return full_name

def show_line(db):
    for patient in db:
        print(patient)
        print('Name: {} , Patient ID: {} , Age: {}'.format(get_full_name(db[patient]),db[patient]['ID'],db[patient]['Age']))

def search(db,patient_id):
    patient = db[patient_id]
    return patient

def adult_or_minor(patient):
    if patient['Age']>=18:
        return 'Adult'
    else:
        return 'Minor'

def addition(db,patient_id,test_name,test_value):
    patient = search(db,1)
    t = (test_name,test_value)
    patient['Tests'].append(t)


    
if __name__=='__main__':
    main()
