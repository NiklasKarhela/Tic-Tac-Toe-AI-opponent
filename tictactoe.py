import math
matrix =[["","",""], ["","",""], ["","",""]]
positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
letters = ["A", "B", "C"]
def print_matrix():
    for lis in matrix:
        print(lis)

def check_taken(choise):
    choise = list(choise)

    for idx, letter in enumerate(letters):
        if choise[0] == letter:
            if matrix[idx][int(choise[1])-1] == "":
                return 0
    return 1

def check_win():
    #vågräta linjer
    for n in range(3):
        if all(element == matrix[n][0] for element in matrix[n]):
            if matrix[n][0] == "X":
                return -1
            elif matrix[n][0] == "O":
                return 1
                
    #vågräta linjer
    for n in range(3):
        if matrix[0][n] == matrix[1][n] and matrix[2][n] == matrix[0][n]:
            if matrix[0][n] == "X":
                return -1
            elif matrix[n][0] == "O":
                return 1
    
    #korsvis linjerna
    if matrix[0][0] == matrix[1][1] and matrix[0][0]==matrix[2][2]:
        if matrix[0][0] == "X":
            return -1
        elif matrix[n][0] == "O":
            return 1
                
    if matrix[0][2] == matrix[1][1] and matrix[0][2]==matrix[2][0]:
        if matrix[0][2] == "X":
            return -1
        elif matrix[n][0] == "O":
            return 1
    
    # Tittar om spelet har blivit jämt
    if "" not in matrix:
        return 0
        
def player_move(rounds):
    choise = input("Välj ruta (bokstav sedan nummer): ")

    if choise in positions:  #tittar om inputten är i rätt form (t.ex A1)
        if check_taken(choise) == 0:  #tittar om valda rutan är ledig
        
        
            #Denna for loop sätter in spelarens märke på givna position.
            for idx, pos in enumerate(positions):
                if pos == choise:
                    choise = list(choise)
                    
                    for letter in letters:
                        
                        if choise[0] == letter:
                            if idx<=2:
                                matrix[0].insert(int(choise[1])-1, "X")
                                matrix[0].pop(int(choise[1]))
                            elif idx<=5 and idx>2:
                                matrix[1].insert(int(choise[1])-1, "X")
                                matrix[1].pop(int(choise[1]))
                            else:
                                matrix[2].insert(int(choise[1])-1, "X")
                                matrix[2].pop(int(choise[1]))
            if rounds >= 3:
                check_win()
        else:
            print("Denna rutan är tagen! ")
            player_move(rounds)
    else:
        print("Fel input (A1, A2, A3, B1, B2, B3, C1, C2 och C3 godkäns)")
        player_move(rounds)

def bot_move(rounds):
    best_score = -math.inf

    for x in range(3):
        for z in range(3):
            if matrix[x][z] == "": #Tittar om det rutan är ledig (forloopina före går genom alla positioner)

                matrix[x].insert(z, "O") #sätter in O på ett ställe som är ledigt och spelar genom spelet
                matrix[x].pop(z+1) 
                score = minimax(True, 0, best_score)
                matrix[x].insert(z, "") #efter "lek" spelet ändrar den tillbaka rutan till den orginella
                matrix[x].pop(z+1)

                if score > best_score:
                    best_score = score
                    best_move = letters[x] + str(z+1)
    best_move = list(best_move)
    for idx, letter in enumerate(letters):
        if letter == best_move[0]:
            matrix[idx].insert(int(int(best_move[1])-1), "O")
            matrix[idx].pop(int(best_move[1]))

    #tittar om bot-niklas van
    if rounds >= 3:
        winner = check_win()
        if winner == 1:
            print_matrix()
            print("BOT-Niklas van")
            exit()
        elif winner == -1:
            print_matrix()
            print("Spelaren van")
            exit()
        elif winner == 0 :
            print_matrix()
            print("Det blev jämt")
            exit()
            

def minimax(is_maximizing, depth, best_score):
    #Titta om BOT niklas van
    check_win()
    score = check_win()
    if score != None:
        return score

    if is_maximizing == True:
        for x in range(3):
            for z in range(3):
                if matrix[x][z] == "": #Tittar om det rutan är ledig

                    matrix[x].insert(z, "O") #sätter in O på ett ställe som är ledigt och spelar genom spelet
                    matrix[x].pop(z+1) 
                    score = minimax(False, depth +1, best_score)
                    matrix[x].insert(z, "") #efter "lek" spelet ändrar den tillbaka rutan till den orginella
                    matrix[x].pop(z+1)

                    if score > best_score:
                        return score
    else:
        for x in range(3):
            for z in range(3):
                if matrix[x][z] == "": #Tittar om det rutan är ledig

                    matrix[x].insert(z, "X") #sätter in O på ett ställe som är ledigt och spelar genom spelet
                    matrix[x].pop(z+1) 
                    score = minimax(True, depth +1, best_score)
                    matrix[x].insert(z, "") #efter "lek" spelet ändrar den tillbaka rutan till den orginella
                    matrix[x].pop(z+1)
                    if score > best_score:
                        return score

rounds = 0
while rounds <= 9:
    rounds+=1
    print_matrix()
    player_move(rounds)
    bot_move(rounds)
    
