import os
from .models import *
from datetime import datetime
from datetime import timedelta
from django.core.mail import send_mail
from django.http import *
from django.shortcuts import *
from django.shortcuts import *
from random import *

# defining state globaly
# ['Rook', 'Knight', 'Bishop', S~shah:='King','Queen', 'Bishop', 'Knight', 'Rook']

statebase = [
    ["0" ,"-a", "-b", "-c", "-d", "-e", "-f", "-g", "-h"],
    ["8" ,"R", "K", "B", "Q", "S", "B", "K", "R"],
    ["7" ,"P", "P", "P", "P", "P", "P", "P", "P"],
    ["6" ,".", ".", ".", ".", ".", ".", ".", "."],
    ["5" ,".", ".", ".", ".", ".", ".", ".", "."],
    ["4" ,".", ".", ".", ".", ".", ".", ".", "."],
    ["3" ,".", ".", ".", ".", ".", ".", ".", "."],
    ["2" ,"p", "p", "p", "p", "p", "p", "p", "p"],
    ["1" ,"r", "k", "b", "q", "s", "b", "k", "r"]
]
# global USERNAME

# state = [
#     ["0" ,"-a", "-b", "-c", "-d", "-e", "-f", "-g", "-h"],
#     ["8" ,"R", "K", "B", "Q", "S", "B", "K", "R"],
#     ["7" ,"P", "P", "P", "P", "P", "P", "P", "P"],
#     ["6" ,".", ".", ".", ".", ".", ".", ".", "."],
#     ["5" ,".", ".", ".", ".", ".", ".", ".", "."],
#     ["4" ,".", ".", ".", ".", ".", ".", ".", "."],
#     ["3" ,".", ".", ".", ".", ".", ".", ".", "."],
#     ["2" ,"p", "p", "p", "p", "p", "p", "p", "p"],
#     ["1" ,"r", "k", "b", "q", "s", "b", "k", "r"]
# ]
# global state

def translate(matrix):
    dic_value = {"R": "bR.png", "r": "wR.png", "K": "bK.png", "k": "wK.png", "Q": "bQ.png", "q": "wQ.png","B": "bB.png",
    "b": "wB.png", "S": "bS.png", "s": "wS.png", "P": "bP.png", "p": "wP.png", ".": "em.png","-a": "a.png",
    "-b": "b.png", "-c": "c.png", "-d": "d.png", "-e": "e.png", "-f": "f.png", "-g": "g.png","-h": "h.png", "0":"chess.png", "1": "1.png", 
    "2": "2.png", "3": "3.png", "4": "4.png", "5": "5.png", "6": "6.png","7": "7.png", "8": "8.png"}

    for row_index in range(9):
        for column_index in range(9):
            matrix[row_index][column_index] = dic_value[matrix[row_index][column_index]]
    return matrix

def undo_translation(matrix):
    dic_value_reverse={"bR.png":"R", "wR.png":"r", "bK.png":"K", "wK.png":"k", "bQ.png":"Q", "wQ.png":"q","bB.png":"B",
    "wB.png":"b",  "bS.png":"S",  "wS.png":"s","bP.png":"P",  "wP.png":"p",  "em.png":".", "a.png":"-a",
    "b.png":"-b",  "c.png":"-c",  "d.png":"-d",  "e.png":"-e", "f.png":"-f",  "g.png":"-g", "h.png":"-h", "1.png":"1",
    "2.png":"2", "3.png":"3",  "4.png":"4",  "5.png":"5",  "6.png":"6","7.png":"7", "8.png":"8","chess.png":"0"}

    for row_index in range(9):
        for column_index in range(9):
            state[row_index][column_index] = dic_value_reverse[state[row_index][column_index]]
    return state


def matrix_to_string(matrix):
    string = ''
    for row_index in range(9):
        for column_index in range(9):
            string += matrix[row_index][column_index]
            if column_index != 8:
                string += ","
        string += "%"
    return string

def string_to_matrix(string):
    matrix =[[0 for i in range(9)]for j in range(9)]
    list_temp_str = string.strip().split("%")
    for row_index in range(len(list_temp_str)-1):
        list_row_matrix =list_temp_str[row_index].split(",")
        for column_index in range(len(list_row_matrix)):
            matrix[row_index][column_index] = list_row_matrix[column_index]
    return matrix

def move_decoding(string):
    dic_position_value = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
    j = dic_position_value[string[0]]
    i = 9 - int(string[1])
    return (i,j)


def home(request):
    return render(request, "ChessAiSite_app/home.html")


def login(request):
    return render(request, "ChessAiSite_app/login.html")


def signup(request):
    return render(request, "ChessAiSite_app/signup.html")


# def change_UTA_code(sun):
#     sum = 0
#     for letter_index in range(len(sun)):
#         sum += (letter_index + 1) * (ord(sun[letter_index]))
#     SECRET_KEY = ''.join(
#         [SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(7)])
#     SECRET_KEY2 = ''.join(
#         [SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^*(-_=+)') for i in range(5)])
#     current_length = 7 - len(repr(sum))
#     result = SECRET_KEY[(7 - current_length + 1):] + "$" + repr(sum) + "=*2" + SECRET_KEY2
#     print result


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


def info_signup(request):
    player = User.objects.filter(username=request.POST['username'])
    # if user wan't assign to another user before
    if not player:
        usernamen = request.POST['username']
        passwordn = request.POST['password']
        emailn = request.POST['email']
        sum = 0
        for letter_index in range(len(usernamen)):
            sum += (letter_index + 1) * (ord(usernamen[letter_index]))
        SECRET_KEY = ''.join([SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(7)])
        SECRET_KEY2 = ''.join([SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^*(-_=+)') for i in range(5)])
        current_length = 7 - len(repr(sum))
        result = SECRET_KEY[(7 - current_length + 1):] + "$" + repr(sum) + "=*2" + SECRET_KEY2
        activationcoden = result
        user = User(username=usernamen, email=emailn, password=passwordn, activationcode=activationcoden, gameboard=matrix_to_string(statebase))
        user.save()
        send_mail(
            'ChessAi Suport',
            'Dear ' + usernamen + " Your Activation code is :  " + str(activationcoden),
            'proje.term1.5@gmail.com',
            [user.email],
            fail_silently=False,
        )
        return render(request, "ChessAiSite_app/info_signup.html", {'user': user})
    else:
        error = "This username was token before, please try some thing diffrent"
        return render(request, "ChessAiSite_app/signup.html", {'error': error})


def info_login(request):
    usernamen = request.POST['username']
    passwordn = request.POST['password']
    
    # user1 = User.objects.filter(username=USERNAME)
    # return HttpResponse(repr(user1)+repr(user1.username)+repr(user1.password))
    
    user1 = User.objects.filter(username=usernamen)
    if user1:
        user1 = User.objects.get(username=usernamen)
        if user1.password == passwordn:
            if user1.isActive == 0:
                return render(request, "ChessAiSite_app/info_signup.html", {'error': "you account isnt active!"})
            else:
                return render(request, 'ChessAiSite_app/game.html', {'state':translate(statebase), 'user':user1})
        else:
            error = "Password is incorrect pleas try again !"
            return render(request, "ChessAiSite_app/login.html", {'error': error})
    else:
        error = "The Username dosen't exist in data base !"
        return render(request, "ChessAiSite_app/login.html", {'error': error})


def active(request):
    user = User.objects.get(username=request.POST['username'])
    activationcoden = request.POST['activationcode']
    if change_ATU_code(user.username, activationcoden):
        if user.activationcode == activationcoden:
            user1 = user
            user.delete()
            user1.isActive = 1
            user1.save()
            return render(request, "ChessAiSite_app/active.html", {"user": user1})
        else:
            error = "You have entered Code wrongly"
            return render(request, "ChessAiSite_app/info_signup.html", {'error': error})
    else:
        error = "Code is not valid"
        return render(request, "ChessAiSite_app/info_signup.html", {'error': error})


# def game(request):
    # if request.session.has_key('user_id'):
    #     user_id=request.session['user_id']
    #     # user = User.objects.get(id = user_id)
    #     user = User.objects.get(pk=user_id)
    #   s  state = user.gameboard
    #     state = translate(state)
    # else:
    #     state = translate(statebase)
    # global USERNAME
    # state = translate(statebase)
    # return render(request, "ChessAiSite_app/game.html", {'state': state, 'user' : user})

def move(request):
    # movement = request.POST['move']
    # id_move = movement.strip().split(":")
    # moves = id_move[1].split(",")
    # current_position = move_decoding(moves[0])
    # next_position = move_decoding(moves[1])
    # # user = User.objects.get(id=int(id_move[0]))
    # user = User.objects.get(pk=int(id_move[0]))
    # user_state = string_to_matrix(user.gameboard)
    # user_state[next_position[0]][next_position[1]] = user_state[current_position[0]][current_position[1]]
    # user_state[current_position[0]][current_position[1]] = "."
    # user.gameboard = matrix_to_string(user_statse)
    # # state = user_state
    # request.session['user_id'] = user.id
    # user.save()

    # global USERNAME
    # USERNAME = request.POST['username']
    # return HttpResponse(repr(USERNAME)+repr(request.POST['username']))
    return
    user = User.objects.get(username=request.POST['username'])
    movement = request.POST['move']
    # return HttpResponse(repr(user.username)+repr(movement))
    moves = movement.split(",")
    current_position = move_decoding(moves[0])
    next_position = move_decoding(moves[1])
    user_state = string_to_matrix(user.gameboard)
    user_state[next_position[0]][next_position[1]] = user_state[current_position[0]][current_position[1]]
    # return HttpResponse(repr(USERNAME)+repr(user_state))
    user_state[current_position[0]][current_position[1]] = "."
    user.gameboard = matrix_to_string(user_state)
    # request.session['user_username'] = user.username
    state = translate(string_to_matrix(user.gameboard))
    user.save()
    return render(request, "ChessAiSite_app/game.html", {'state': state})

    # return game(request)
    

 # User.objects.get(id=request.POST['id'])
   # def move(request):
   #      movements = request.POST['movements']
   #      move_list = list(map(str,movements.split(",")))
   #      move_current = move_list[0]
   #      move_next = move_list[1]
        
        # changing move_current & move_next {a5 to [1][5]}
        # geting state:matrix
        # checking movement posibility of moving
        # returning sate:matrix to game function
        # adding AI



    # User.objects.get(id=request.POST['id'])
        # pass 





 # player = User.objects.filter(username=request.POST['username'])
