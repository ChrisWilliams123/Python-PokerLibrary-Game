# Python-PokerLibrary-Game

PokerLib

Containing:

8 functions identifying hand type:
	ishole_suitedconnectors()
        ishole_connectors()
        ishole_suitedonegappers()
        ishole_onegappers()
        ishole_suitedtwogappers()
        ishole_twogappers()
        ishole_suited()
        ishole_pocketpair()
        
        Syntax:
        	import PokerLib
        	PokerLib.ishole_suited(hole_cards)
       	Parameter:
       		holecards: list (length 2) of hole cards, stored in tuple format i.e. (r,s) where s is suit (integer between 1 and 4 inclusive) and r is rank (integer between 2 and 14 inclusive, Ace 14))
       	Returns: 
       		True or False, dependant on nature of hole cards.
        
10 functions indentifying board type: 
	isquads()
        isfullhouse()
        isflush()
        isflush_draw()
        isstraight()
        isstraight_draw()
        isinsidestraight_draw()
        isset()
        istwopair()
        isonepair()
        
        Syntax:
        	import PokerLib
        	PokerLib.isset(cards,score)
        Parameter:
        	cards: list (length 5-7) of hole cards + board cards, stored in tuple format (r,s)
        	score (optional): True/False whether a scoring string is required
        	hole_en (optional): True/False whether hole cards have to be included in identification. Note - hole cards must be first two cards in cards list if set to True
        Returns:
        	score = False: True or False, dependant on nature of hole cards + board cards.
        		e.g.
        			AKs with 34567 passed to isstraight() would return True
        			AKs with 34567 and hole_en=True passed to isstraight() would return False 
        			
        	score = True: tuple, (bool, string), where bool represents nature of cards and string scores the cards. Drawing hands always return a score of '0.0'  
        		e.g. 
        			trip 3s with A, K passed to isset() would return (True,'3.14.13')
        			pair 10s, pair 7s, 3, J, Q passed to istwopair() would return (True, '10.7.12')
        			2,5,7,7,K passed to isflush() would return (False, '0.0')
				     	
2 helper functions:
 	highest()
 	lowest()
 	
 	Syntax:
 	        import PokerLib
        	PokerLib.highest(cards)
        Parameter:
        	cards: list (length 2-7) of cards, stored in tuple format (r,s)
        	score (optional): True/False whether a scoring string is required
        Returns:
        	score = False: rank of highest/lowest card.
        	score = True:  scoring string e.g. 2,5,7,7,K passed to lowest would return '13.7.7.5.2'
        	

To be used with Texas Hold'em simulation/training program. See also PokerVillainLib

Place file in .local/lib/python3.9/site-packages or equivalent.
