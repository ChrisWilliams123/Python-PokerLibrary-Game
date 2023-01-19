import random
from PokerLib import*

deck = [(i,j) for j in range(1,5) for i in range(2,15)]

random.shuffle(deck)

player1_holes = deck[0:2]
player2_holes = deck[2:4]

board = deck[4:9]

print(f"player 1 holes: {player1_holes}\nplayer 2 holes: {player2_holes}\nboard: {board}\n")

player1 = player1_holes+board
player2 = player2_holes+board

print(f"player 1 has suited connectors?: {ishole_suitedconnectors(player1_holes)}")
print(f"player 2 has two gappers?: {ishole_twogappers(player2_holes)}\n")

board_types = [(isquads,'quads'),
               (isfullhouse,'fullhouse'),
               (isflush,'flush'),
               (isflush_draw,'flush draw'),
               (isstraight,'straight'),
               (isstraight_draw,'straight draw'),
               (isinsidestraight_draw,'insidestraight draw'),
               (isset,'set'),
               (istwopair,'twopair'),
               (isonepair,'onepair')]

for board, name in board_types:
	TF, result = board(player1, score=True)
	if TF:
		print(f"player 1 has {name}: {result}")



