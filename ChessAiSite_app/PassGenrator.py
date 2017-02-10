import random


#      user to activation code
def change_UTA_code(sun):
    sum = 0
    for letter_index in range(len(sun)):
        sum += (letter_index + 1) * (ord(sun[letter_index]))
    SECRET_KEY = ''.join(
        [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(7)])
    SECRET_KEY2 = ''.join(
        [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^*(-_=+)') for i in range(5)])
    current_length = 7 - len(repr(sum))
    result = SECRET_KEY[(7 - current_length + 1):] + "$" + repr(sum) + "=*2" + SECRET_KEY2
    return result


#      activation code to user
def change_ATU_code(sun, code):
    if len(code.strip()) != 15:
        return False

    num = list(code.split("=*2"))[0]
    num2 = list(num.split("$"))[-1]

    sum = 0
    for letter_index in range(len(sun)):
        sum += (letter_index + 1) * (ord(sun[letter_index]))

    if int(sum) == int(num2):
        return True
    else:
        return False


str = input("enter your text: ")
print(change_UTA_code(str))

active = input("input your activation code: ")

if change_ATU_code(str, active):
    print("Dear " + str + "!")
    print("Thank you for registriation")
else:
    print("Purchase the app please!")

finish = input()
