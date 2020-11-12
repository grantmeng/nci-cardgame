## Welcome to "Card Game"  

It's a simple card game with 2 players. Each card has a color (red, yellow or green) and number. Players will draw 3 cards by taking turns. Whoever has the high score wins the game. (color point calculation, red = 3, yellow =2, green = 1) the point is calculated by color point * number in the card.  

Classes defined
Card:   with color and value (number) attributes, defined in card.py  
Deck:   consists of list of cards, with draw(), shuffle(), etc methods, defined in deck.py  
Player: with name and rule (default is SimpleRule) attribute, defined in player.py  
Rule:   consists of different rules for score calculation, defined in rule.py  

Main script: the main script to start the game, run as 'python play.py' or 'python3 play.py' (depends on your Python version)  

Unit testing:  
Run pytest or py.test  
(Note: As I got the coding challenge done in just two hours, testing cases covered some not all, just for demo purpose) 
