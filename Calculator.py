print('Select Operation')
print('1. Add')
print('2. Substract')
print('3. Multiply')
print('4. Divide')

def add(x, y):
    return x + y
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y


while True:
    choice = input('Enter Operation (1/2/3/4): ')

    if choice in ('1', '2', '3', '4'):
        num1 = float(input('Enter The First Number : '))
        num2 = float(input('Enter The Second Number : '))

        if choice == '1':
            print('{} + {} = {}'.format(num1, num2, add(num1, num2)))
            print()
        elif choice == '2':
            print('{} - {} = {}'.format(num1, num2, substract(num1, num2)))
            print()
        elif choice == '3':
            print('{} x {} = {}'.format(num1, num2, multiply(num1, num2)))
            print()
        elif choice == '4':
            print('{} / {} = {}'.format(num1, num2, divide(num1, num2)))
            print()
        break
    else:
        print('Invalid Input')
