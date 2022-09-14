def create_patient_entry(patient_name,patient_id,patient_age):
    new_patient = [patient_name,patient_id,patient_age,[]]
    return new_patient

def main():
    db = []
    db.append(create_patient_entry('Ann Ables',1,30))
    db.append(create_patient_entry('Bob Boyles',2,34))
    db.append(create_patient_entry('Chris Chou',3,25))
    # show_line(db)
    # search(db,2)
    addition(db,1,'HDL',100)
    print(search(db,1))

    room_list=['Room 1','Room 2','Room 3']

    for i, patient in enumerate(db):
        print('Name = [], Room = []'.format(patient[0],room_list[i]))

    for patient,room in zip(db,room_list):
        print('Name = [], Room = []'.format(patient[0],room)
    
def show_line(db):
    for patient in db:
        print('Name: {} , Patient ID: {} , Age: {}'.format(patient[0],patient[1],patient[2]))

def search(db,patient_id):
    for patient in db:
        if patient_id == patient[1]:
            return patient
    return False

def addition(db,patient_id,test_name,test_value):
    patient = search(db,1)
    t = (test_name,test_value)
    patient[3].append(t)


    
if __name__=='__main__':
    main()
