import pvc, pvp, cvc

# function to prompt the welcome message
def message():
    print("Welcome to X-Rudder game!")
    print("Choose what kind of mode you want to play:")
    print("===============================================================")
    print("1 - Player vs Player")
    print("2 - Player vs Computer (Easy)")
    print("3 - Player vs Computer (Hard)")
    print("Q - to quit")
    
def mainmenu():
    message()
    user_input = input("Enter the mode: ")[0]
    if user_input == '1':
        pvp.runPVP()
    elif user_input == '2':
        heuristic_two = False
        pvc.runPVC(heuristic_two)
    elif user_input == '3':
        heuristic_two = True
        pvc.runPVC(heuristic_two)
    elif user_input != 'q':
        mainmenu()

if __name__ == '__main__':
    mainmenu()