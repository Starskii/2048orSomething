# Welcome to 2048OrSomething
As a programming exercise I decided to create a 2048 program with dynamic width/height and number of blocks to be spawned. This made it slightly more challenging, I hope you enjoy playing around with the game.

## Setup
1) Using python 3.12.1 (although other versions should work, they just were not tested.) 
2) git clone https://github.com/Starskii/2048orSomething.git
3) pip install -r .\2048orSomething\requirements.txt
4) python .\2048orSomething\src\Main.py

## Controls 
- Key_Up:
  - Used in game to move blocks.
  - Used on the splash screen, options screen, loss screen, to navigate menu options.  
- Key_Down:
  - Used in game to move blocks.
  - Used on the splash screen, options screen, loss screen, to navigate menu options.  
- Key_Right:
  - Used in game to move blocks.
  - Used on the options screen screen to increment menu options. (For example increase the board height parameter.)   
- Key_Left:
  - Used in game to move blocks.
  - Used on the options screen screen to decrement menu options. (For example decrease the board height parameter.)   
- Enter:
  - Used to select menu options on splash, options and loss screen.
- Escape Key:
  - Used to return to the splash screen from any screen.

 ## Screens 
 There are 4 screens. Splash, Options, Loss, Game

 ### Splash
 
 ![image](https://github.com/Starskii/2048orSomething/assets/34251559/2732c6b2-7936-466b-b653-f9dc5af96a65)

 The splash screen is the first screen a user is greeted with. It has the following dialogue options: 
 1) New Game, this will create a new game with the options that have been configured in the options screen.
 2) Continue Game, when the program is first launched there is a game already created. If you use the escape key mid-game and want to return to your game select this option.
 3) Options, options will be discussed in full below, but you can use this dialogue option to navigate to the Options screen.
 4) Quit, this will exit the application.

 ### Options 

 ![image](https://github.com/Starskii/2048orSomething/assets/34251559/f097dadb-1cff-4fa2-825d-7cdfc2548828)

 The options screen is where you can modify the game parameters by making the game board bigger/smaller or by increasing the block spawn count. It has the following dialogue options controlled by the arrow keys as described above: 
 1) Board Width, this determines how large the gameboard is in the x-axis. 
 2) Board Height, this determines how large the gameboard is in the y-axis.
 3) Block Spawn Count, this determines the number of blocks to be spawned every time a player makes an action in the game.

### Game

![image](https://github.com/Starskii/2048orSomething/assets/34251559/05ee6067-c3c7-4649-a503-a12dc4ea7974)

This is the primary screen of the application where the user can play 2048. 

### Loss 

![image](https://github.com/Starskii/2048orSomething/assets/34251559/d5480ef7-4c76-4faf-8c31-fe162780bb42)

 Upon losing the game (as a player will eventually) they are shown this screen where the score, number of moves and game parameters are shown.
