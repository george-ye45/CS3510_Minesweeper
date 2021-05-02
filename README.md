# CS 3510 Minesweeper Project

### By: Shaan Gill and George Ye

## Files and Directories

All files and directories given by the TAs in the starter code is the same. Some additional code was added to `minesweeperPerformanceTest.py` for testing purposes. Mentioned in later section.

* `minesweeperAI1.py` - Contains algorithm 1
* `minesweeperAI2.py` - Contains algorithm 2
* `minesweeperGameEngine.py` - Given by starter code with same functionality: A GUI game engine for the Minesweeper game.
  * It takes one argument, `-f`, to indicate the json config file to use for the game. The interface has two buttons (AI1 and AI2), and clicking the button once will execute `performAI` once in the respective AI file. You can also play the game manually by clicking on the buttons, but switching between manual play and AI for the same game can lead to errors. 
  * The blue square is the NEXT square your AI will open based on the current board layout, which was determined in the previous iteration of pressing the button. In other words, whenever you press an AI button, the blue square will first open, then the board with the opened blue square is passed to `performAI()`, and then your AI algorithm will determine the next best square to open.
* `minesweeperPerformanceTest.py` - Given by starter code with same functionality: A script where you can specify the board size, number of bombs, safe starting square, the type of AI to use (1 or 2), and the number of games to play. This script will generate a random game board with your configuration and use the AI specified to run the game and determine the number of games you played. Please look at the bottom of the file to understand this in more detail.
* `deterministic_board.json` - An (example) json config file that can be passed to `minesweeperGameEngine.py`.
* `/varied_density_boards` - Directory containing test boards for bomb densities from 2% to 20%
* `/varied_size_boards` - Directory containing test boards for board sizes varying from 100 to 1000 in area
* `test_board.json` - Another sample test board
* `3510-project-S21-v2.1.pdf` - Project Problem Description

## How to run
All of the functionality in the starter code given by the TAs is the same. An additional library that we used is called pandas. Please install it or one of the commands will not work. 

* Make sure all files are in the same directory
* Make sure you have `python3` installed (`python2` will most likely not work). Make sure you have common libraries installed, including `numpy` and `tk`. If you run the program and receive some import error, you are most likely missing a library, which can be downloaded fairly simply through a quick google search. Please let us know if you are unable to run the files on Piazza.
* On command prompt/anaconda/terminal, type and enter `python3 minesweeperGameEngine.py`. Depending on how you installed python, if that does not work, try `python minesweeperGameEngine.py`. A GUI should appear, and clicking either button will run through the algorithm. 
  *  You can also run, for example, `python3 minesweeperGameEngine.py -f deterministic_board.json`, which will use that json file. The default is `test_board.json`
* On command prompt/anaconda/terminal, type and enter `python3 minesweeperPerformanceTest.py`. Depending on how you installed python, if that does not work, try `python minesweeperPerformanceTest.py`. No GUI will appear, but some games will be automatically ran, and you will get a quick summary of how many were won and lost.
  * You can also run, for example, `python3 minesweeperPerformanceTest.py -g 15 16 17 0 3 1 10 `, which indicates 10 randomly generated gameboard of size $15 \times 16$ with 17 bombs and a safe square of (0, 3). Each gameboard will be solved independently using your first (1) algorithm.
  * You run also run, for example, `python3 minesweeperPerformanceTest.py -f deterministic_board.json 2`, which will use the given board json and your second (2) algorithm.  

## Additional Commands

We have added a command that allows for the algorithms to be tested on all the test boards provided in the directories `varied_density_boards` and `varied_size_boards`.

The `-t` flag represents the test command. `d` represents varied density boards. `b` represents varied size boards. `1` represents algo 1 being used. `2` represents algo 2 being used.

```
python3 minesweeperPerformanceTest.py -t d 1
```
```
python3 minesweeperPerformanceTest.py -t b 2
```
Each time the command is ran, it will create a single CSV with the data gathered by `minesweeperPerformanceTest.py` for that specific algo and that specific test. To create all files, you will need to run the command 4 times with the parameters set accordingly.

Example of files created:
```
board_size_change_1.csv
board_size_change_2.csv
density_change_1.csv
density_change_2.csv
```

## Known Bugs

* If there does happen to be an error with the `.csv` files, try deleting the `.csv` files and running the command again.