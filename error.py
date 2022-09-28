def add(a,b):
    answer = a+b
    return answer

def main():
    a = 5
    b = '3'
    try:
        answer = add(a,b)
    except TypeError:
        print('The input values are not int or float, cannot add. Change the type of values.')

if __name__ == '__main__':
    main()