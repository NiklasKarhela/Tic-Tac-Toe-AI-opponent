matrix =[["","",""], ["","",""], ["","",""]]
positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

def print_matrix():
    for lis in matrix:
        print(lis)

def player_move():
    choise = input("Välj ruta (bokstav sedan nummer): ")
    
    #Denna for loop sätter in spelarens märke på givna position.
    for idx, pos in enumerate(positions):
        if pos == choise:
            choise = list(choise)

            if choise[0] == "A":
                if idx<=2:
                    matrix[0].insert(int(choise[1])-1, "X")
                    matrix[0].pop(int(choise[1]))
                elif idx<=5 and idx>2:
                    matrix[1].insert(int(choise[1])-1, "X")
                    matrix[1].pop(int(choise[1]))
                else:
                    matrix[2].insert(int(choise[1])-1, "X")
                    matrix[2].pop(int(choise[1]))
                    
            elif choise[0] == "B":
                if idx<=2:
                    matrix[0].insert(int(choise[1])-1, "X")
                    matrix[0].pop(int(choise[1]))
                elif idx<=5 and idx>2:
                    matrix[1].insert(int(choise[1])-1, "X")
                    matrix[1].pop(int(choise[1]))
                else:
                    matrix[2].insert(int(choise[1])-1, "X")
                    matrix[2].pop(int(choise[1]))
            else:
                if idx<=2:
                    matrix[0].insert(int(choise[1])-1, "X")
                    matrix[0].pop(int(choise[1]))
                elif idx<=5 and idx>2:
                    matrix[1].insert(int(choise[1])-1, "X")
                    matrix[1].pop(int(choise[1]))
                else:
                    matrix[2].insert(int(choise[1])-1, "X")
                    matrix[2].pop(int(choise[1]))
            
    print(print_matrix())

while True:
    print_matrix()
    player_move()
    break
