comp472-project1
================

Repo for Project 1 of COMP 472 - Artificial Intelligence

RUN ON WINDOWS LAB COMPUTER
---------------------------

1.  Open Anaconda Prompt.

2.  Change the current location to the folder of the project.
3.  type this command: `pip install anytree --user` since you do not have write on the computer.
4.  Type `py main.py` to run the game

    a.  The `main.py` is the main file of the game, it contains the main menu allowing the player to choose the game mode.
5.  You have a choice between these three game mode, the first choice is the Player vs Player game, the second and third choice are both Player vs Computer mode but with two different algorithms. 

6.  The possible input are shown when you start the game

    a.  The list of all available input can be displayed again by
        typing:

    -   'h' or 'H' and press 'RETURN' (**help**).

    b.  This is also possible to exit the game by typing:

    -   'q' or 'Q' and press 'RETURN'

    c.  This is possible to add a new token in the game by typing:

    -   'T <LETTERNUMBER>' combination: EX: 'T A1' is an acceptable
        combination.
    -   'M <PREVIOUSPOSITION> <NEWPOSITION>' combination, the position
        must follow this format <LETTERNUMBER> as well. EX: 'M A1 B1' is
        an acceptable combination.

    d.  in all these case, the input are case-insensitive.

6.  Hope you will enjoy the game!

## Deliverable 2 files
The files used for D1 are:
- main.py (main game file)
- pvp.py (The PvP game configuration)
- pvc.py (the PvC game configuration)
- config.py
- board.py
- player.py (The player file)
- minimax.py (The Computer file)
- README.md and README.pdf
- Expectation of Originality

Disregard the other files for the moment. These are for future Deliverable and iteration.
- earl-teststuff
- treeTests.py
- tester.py
- To-Do.md (to keep track team task)