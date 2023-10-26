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
            if matrix[idx][int(choise[1])] != "":
                print("Denna rutan är tagen! ")
                return 0
    return 1
    

def check_win():
    #vågräta linjer
    for n in range(3):
        if all(element == matrix[n][0] for element in matrix[n]):
            if matrix[n][0] == "X":
                print("Spelaren van")
            else:
                print("Bot-Niklas van")
                
    #vågräta linjer
    for n in range(3):
        if matrix[0][n] == matrix[1][n] and matrix[2][n] == matrix[0][n]:
            if matrix[0][n] == "X":
                print("player won")
            else:
                print("Bot-Niklas won")
    
    #korsvis linjerna
    if matrix[0][0] == matrix[1][1] and matrix[0][0]==matrix[2][2]:
        if matrix[0][0] == "X":
            print("player won")
        else:
            print("Bot-Niklas won")
                
    if matrix[0][2] == matrix[1][1] and matrix[0][2]==matrix[2][0]:
        if matrix[0][2] == "X":
            print("player won")
        else:
            print("Bot-Niklas won")
        
def player_move(rounds):
    choise = input("Välj ruta (bokstav sedan nummer): ")
    if check_taken(choise) == 1:
        
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
        print(print_matrix())
        
    else:
        player_move()
    

rounds = 0
while rounds < 4:
    rounds+=1
    print_matrix()
    player_move(rounds)
    
