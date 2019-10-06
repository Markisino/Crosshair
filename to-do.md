# To-Do Document
## Introduction
This is a To-Do list in order to do the assignment.    
This list is subject to change    
The game is called X-Rudder, two player game.

## Important Dates
__Deliverable 1__ is due on Wednesday October 16<sup>th</sup>    
__Deliverable 2__ is due on Wednesday November 6<sup>th</sup>    
__Deliverable 3__ is due on Wednesday November 20<sup>th</sup>    
__Late submission__: 20% per day.

## Set-Up
board with 30 square tokens (15/per color)    
12x10 (12 width and 10 height).    
Board is id'ed the same way as Chess.    
Black and white square represent tokens.    
15 tokens each

## Game Rules
Turn-based game. Objective is to make a cross with 5 tokens. The opponent can block the cross by strikthrough (horizontal) __not__ vertical. When it is your turn, you can either move your token or insert a new one. Decision should be done within five (5) seconds

## To-Do
### Deliverable 1
- [X] Start a counter to track total move when the game start (max 30 moves) <font color=blue><b>MARCO</b></font>
- [X] Build a manual mode (PvP) <font color=gren><b>ALL</b></font>
- [X] Each state of the board is known <font color=yellow><b>EARL</b></font>
- [ ] Test it on Labs machine
- [X] Make a CLI board class <font color=yellow><b>EARL</b></font>
- [X] Players input <font color=red><b>THOMAS</b></font>
- [X] Add a Move Token option <font color=yellow><b>EARL</b></font>
- [X] Adding an option to quit the game <font color=red><b>THOMAS</b></font>
- [X] After 30 moves both loses. <font color=blue><b>MARCO</b></font>
- [X] Added winning condition <font color=blue><b>MARCO</b></font> 
- [ ] Code cleanup and programming quality <font color=red><b>THOMAS</b></font>

### Deliverable 2
- [ ] 5 second to make a decision (AI speed)<font color=yellow><b>EARL</b></font>
- [ ] Build an automatic mode (PvC)
- [ ] Heuristics chosen
- [ ] Notes on different heuristics and why we chose what we did
- [ ] Code cleanup and programming quality
- [X] board to reflect new set and move. Adapt changes to AI turn selection <font color=yellow><b>EARL</b></font> Note: Subject to change depending on how the board is. Up to date as of October 5
- [X] Search space generation (tree) <font color=yellow><b>EARL</b></font>
- [ ] Search space generation (alternating between players) <font color=yellow><b>EARL</b></font>
- [ ] Minimax algorithm implementation (do we want alpha beta pruning?)


### Deliverable 3
- [ ] Report 
- [ ] more or less 1 page of __Introduction__ and __Technical details__
- [ ] 1-2 page: Description and justification of __heuristic__ chosen. Game feature, how we balance speed of evaluation with performance. Explain why we chose that __heuristic__
- [ ] 1 page: description and analysis of result either at __tournament__ or when you played against it. (why heuristic/search made good/bad decision)
- [ ] half of page of description of __responsibilities__ and __contributions__ of each teamte (GitHub ftw)
- [ ] (optional) References, Appendix, Figure, tables not included in the page count
