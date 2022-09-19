def interface():
    print('Blood Calculator')
    print('Options')
    print('9 - Quit')
    keep_running=True
    while keep_running:
        choice = input('Enter choice:')
        if choice =='9':
            return
        elif choice =='1':
            HDL_driver()
        elif choice =='2':
            LDL_driver()
        elif choice =='3':
            Total_driver()

def input_HDL():
    HDL_input = input('Enter the HDL value:')
    return int(HDL_input)

def check_HDL(HDL_input):
    if HDL_input >= 60:
        return 'Normal'
    elif 40<= HDL_input < 60:
        return 'Borderline low'
    else:
        return 'Low'

def HDL_driver():
    hdl_value = input_HDL()
    answer=check_HDL(hdl_value)
    output_HDL_result(hdl_value,answer)

def output_HDL_result(hdl_value,charac):    
    print('The results for an HDL value of {} is {}'.format(hdl_value,charac))

def input_LDL():
    LDL_input = input('Enter the LDL value:')
    return int(LDL_input)

def check_LDL(LDL_input):
    if LDL_input < 130:
        return 'Normal'
    elif 130 <= LDL_input <= 159:
        return 'Borderline high'
    elif 160 <= LDL_input <= 189:
        return 'High'
    else:
        return 'Very high'

def LDL_driver():
    ldl_value = input_LDL()
    answer=check_LDL(ldl_value)
    output_LDL_result(ldl_value,answer)

def output_LDL_result(ldl_value,charac):    
    print('The results for an LDL value of {} is {}'.format(ldl_value,charac))

def check_total(total):
    if total <200:
        return 'Normal'
    elif 200<= total <=239:
        return 'Borderline high'
    else:
        return 'High'

def input_total():
    total_input = input('Enter the total cholesterol:')
    return int(total_input)

def Total_driver():
    total = input_total()
    answer = check_total(total)
    output_total_result(total,answer)

def output_total_result(total,charac):
    print('The results for total cholesterol of {} is {}'.format(total,charac))

if __name__ == '__main__':
    interface()