## Welcome to "Card Game"  

It's a simple card game with a few players. Each card has a color (eg. red, yellow or green) and value number. Players draw some cards by turn. Whoever has the high score wins the game. The point is calculated by color point * number in the card (color point example, red=3, yellow=2, green=1) .  

Classes defined
Card:   with color and value (number) attributes, defined in card.py  
Deck:   consists of list of cards, with draw(), shuffle(), etc methods, defined in deck.py  
Player: with name and rule (default is SimpleRule) attribute, defined in player.py  
Rule:   consists of different rules for score calculation, defined in rule.py  

Configuration: config.py  
You can change the number of players, number of drawing cards, card max value (number), color points are configuable  

Main script: play.py  
The main script to start the game. To play, run 'python play.py' or 'python3 play.py' (depends on your Python version)  

Unit testing:  
Unit testing has been put into 'tests' folder  
Run pytest or py.test  
(Note: As I got this done just in two hours, testing cases are not fully covered) 
