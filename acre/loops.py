import json
import sys
import re

from ast_to_json import item_generator, file_to_dict

class Loops:
	def __init__(self, j_ast):
		self.j_ast = j_ast
	
	def get_nested_level(self, nodetype):
		for i, val in enumerate(item_generator(self.j_ast, '_nodetype', nodetype)):
			pass
		
		return i+1
		
	def detect_nested_while_hard(self, level):
		for i, val in enumerate(item_generator(self.j_ast, '_nodetype', 'While')):
			pass
		
		if(i == level-1):
			return True
		
		return False
		
	def detect_nested_while_soft(self, level):
		for i, val in enumerate(item_generator(self.j_ast, '_nodetype', 'While')):
			if(i == level-1):
				return True
				
		return False

if __name__ == '__main__':
	ast_dict = file_to_dict(sys.argv[1])
	l = Loops(ast_dict)
	print(l.get_nested_level('While'))
	print(l.detect_nested_while_hard(2))
	print(l.detect_nested_while_soft(1))