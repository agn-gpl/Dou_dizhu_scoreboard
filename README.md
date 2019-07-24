# Dou_dizhu_scoreboard

At first, the program will ask you to set initial point for each player.

command:

LANDLORD_PLAYER(1 or 2 or 3) BASE_POINT [BOOM]

  ex "1 24 2" means player1 is the landlord and win the game. The base point of this game is 24 and it booms twice in this game.
  
  ex "3 -12" means player3 is the landlord and lose the game. The base point of this game is 12 and there is no boom in this game.

status(or "s" in short)

  Check the game status.

help(or "h" in short)

  Print help message.

set PLAYER POINT

  Set the point of PLAYER to POINT.

set 0 POINT

  Set the initial point to POINT.

reset(or "r" in short) [POINT]

  Reset the initial point. If you add POINT in the command, it will also set the initial point to POINT.

quit(or "q" in short)

  Exit.
