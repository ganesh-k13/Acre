import json
import sys
import re

from acre.ast_to_json import item_generator, file_to_dict

class Loops:
	def __init__(self, j_ast):
		self.j_ast = j_ast
	
	def _get_level(self, body, nodetype, level):
		_check = item_generator(body, '_nodetype', nodetype)
		
		try:
			next(_check)
		except(StopIteration):
			return level
		
		val = item_generator(body, '_nodetype', nodetype)
		
		levels = []
		for v in val:
			levels.append(self._get_level(v, nodetype, level+1))
		
		return max(levels)
		
	def get_nested_level(self, nodetype):
		levels = []
		for i, val in enumerate(item_generator(self.j_ast, '_nodetype', nodetype)):
			levels.append(self._get_level(val, nodetype, 0))
			
		return max(levels)+1
		
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
	# print(l.detect_nested_while_hard(2))
	# print(l.detect_nested_while_soft(1))