import pvc, pvp, cvc

# function to prompt the welcome message
def message():
    print("Welcome to X-Rudder game!")
    print("Choose what kind of mode you want to play:")
    print("===============================================================")
    print("1 - Player vs Player")
    print("2 - Player vs Computer (Weak Heuristic)")
    print("3 - Player vs Computer (Strong Heuristic)")
    print("Q - to quit")
    
def mainmenu():
    message()
    user_input = input("Enter the mode: ")[0]
    if user_input == '1':
        pvp.runPVP()
    elif user_input == '2':
        strong_heuristic = False
        pvc.runPVC(strong_heuristic)
    elif user_input == '3':
        strong_heuristic = True
        pvc.runPVC(strong_heuristic)
    elif user_input == '4':
        cvc.runCVC()
    elif user_input != 'q':
        mainmenu()

if __name__ == '__main__':
    mainmenu()