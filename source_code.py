class Piece:
		
		def __init__(self,piece_color,piece_type):
			
			if piece_color in ('B','W'):
				self.piece_color=piece_color
				
				if piece_color=='B':
					self.disp_col='\033[1;34m'
					
				elif piece_color=='W':
					self.disp_col='\033[1;37m'
					
			else: 
				raise NameError('Piece color has to be B or W')
			
			if piece_type in ('P','Q'):
				self.piece_type=piece_type
			else:
				raise NameError('Piece type has to be P or Q')			


class Board:

    
	def __init__(self,game_version):
		self.game_version=game_version
		
		if game_version=='International':
			self.grid= [['.'] * 10 for i in range(10)]
			self.size_b=10
	
		elif game_version in ('British','American','Russian'):
			self.grid=[['.'] * 8 for i in range(8)]	
			self.size_b=8
       
		else:
			raise NameError('Incorrect version specified: must be American, British, Russian or International')
		
		
			
	def display_grid(self):
		col_numerals=[str(i) for i in range(0,self.size_b)]
		
		print('  '+ ' '.join(col_numerals))   
			
		ticker=0
   
		for line in self.grid:
			print(ticker,end='')
			
			ticker+=1
			
			for obj in line:
				if isinstance(obj,str) and obj=='.': 
					print('|'+obj,end='')
					
				elif isinstance(obj,Piece):
					print('|'+ obj.disp_col + obj.piece_type + '\033[0m',end='')   
				
				else: 
					raise NameError('Unidentified piece spotted')  
			
			print('|')
	
		print('\n')  
	
	
	def valid_coord(self,coordinate):
		
		return coordinate<self.size_b and coordinate>=0 and isinstance(coordinate,int)
	
	def add_piece(self,piece,coord1,coord2):
		if self.valid_coord(coord1) and self.valid_coord(coord2):
			
			if isinstance(piece,Piece):
				
				if isinstance(self.grid[coord1][coord2],Piece):
					raise NameError('We already have a piece at the current place')
				
				else:	
					self.grid[coord1][coord2]=piece
			
			else:
				raise NameError('Add piece did not get a piece as argument ')	
		
		else:
			raise NameError('Invalid coordinates given when adding a piece')	  
     

   
def main():

		board1=Board('British')
		board1.display_grid()
		piece1=Piece('B','P')
		piece2=Piece('W','P')
		board1.add_piece(piece1,1,1)
		board1.add_piece(piece2,6,4)
		board1.display_grid()	

		return 0
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main())
