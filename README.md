PokerLib library<br>
<br>
Containing:<br>
<br>
8 functions identifying hand type:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ishole_suitedconnectors()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ishole_connectors()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ishole_suitedonegappers()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ishole_onegappers()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ishole_suitedtwogappers()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ishole_twogappers()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ishole_suited()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ishole_pocketpair()<br>
<br>        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Syntax:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import PokerLib<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PokerLib.ishole_suited(hole_cards)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameter:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;holecards: list (length 2) of hole cards, stored in tuple format i.e. (r,s) wheres is suit (integer between 1 and 4 inclusive) and r is rank &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(integer between 2 and 14 inclusive, Ace 14))<br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns:<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;True or False, dependant on nature of hole cards.<br>
<br>        
10 functions indentifying board type:<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isquads()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isfullhouse()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isflush()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isflush_draw()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isstraight()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isstraight_draw()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isinsidestraight_draw()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isset()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;istwopair()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isonepair()<br>
<br>        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Syntax:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import PokerLib<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PokerLib.isset(cards,score)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameter:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cards: list (length 5-7) of hole cards + board cards, stored in tuple format (r,s)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;score (optional): True/False whether a scoring string is required<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hole_en (optional): True/False whether hole cards have to be included in identification.<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note - hole cards must be first two cards in cards list if set to True<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;score = False: True or False, dependant on nature of hole cards + board cards.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AKs with 34567 passed to isstraight() would return True<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AKs with 34567 and hole_en=True passed to isstraight() would return False<br> 
<br>        			
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;score = True: tuple, (bool, string), where bool represents nature of cards and string scores the cards. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Drawing hands always return a score of '0.0'.<br>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g.<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trip 3s with A, K passed to isset() would return (True,'3.14.13')<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pair 10s, pair 7s, 3, J, Q passed to istwopair() would return (True, '10.7.12')<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2,5,7,7,K passed to isflush() would return (False, '0.0')<br>
<br>				     	
2 helper functions:<br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;highest()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lowest()<br>
<br> 	
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Syntax:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import PokerLib<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PokerLib.highest(cards)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameter:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cards: list (length 2-7) of cards, stored in tuple format (r,s)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;score (optional): True/False whether a scoring string is required<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;score = False: rank of highest/lowest card.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;score = True:  scoring string e.g. 2,5,7,7,K passed to lowest would return '13.7.7.5.2'<br>
<br>        	
<br>
To be used with Texas Hold'em simulation/training program. See also PokerVillainLib<br>
<br>
Place file in .local/lib/python3.9/site-packages or equivalent.<br>
