from porridge import Porridge
import sys


def store(key, secret, password):
    porridge = Porridge(f"{key}:{secret}")
    boiled_password = porridge.boil(password)
    file_obj = open('secret.txt', 'a')
    password = boiled_password
    file_obj.write(password)
    file_obj.close()
    print('Success')


def verify(key, secret, password, boiled_password):
    porridge = Porridge(f"{key}:{secret}")
    old_boiled_password = boiled_password
    if porridge.verify(password, old_boiled_password):
        print('Success!')
    else:
        print('Fail!')


def main():
    if len(sys.argv) < 5 or len(sys.argv) > 5:
        print('Invalid number of arguments')

    elif (sys.argv[2] == "" or sys.argv[3] == "" or sys.argv[4] == ""):
        print('One or more arguments are empty')

    else:
        if sys.argv[1] == 'store':
            key = sys.argv[2]
            secret = sys.argv[3]
            password = sys.argv[4]
            store(key, secret, password)

        elif sys.argv[1] == 'verify':
            key = sys.argv[2]
            secret = sys.argv[3]
            password = sys.argv[4]
            file_obj = open("secret.txt", "r")
            verify(key, secret, password, boiled_password=file_obj.read())


main()