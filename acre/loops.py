import json
import sys
import re
from pprint import pprint

from acre.ast_to_json import item_generator, file_to_dict

class Loops:
	def __init__(self, j_ast):
		self.j_ast = j_ast
		
		
	def _annotate_dict(self, json_input, nodetype):
		if isinstance(json_input, dict):
			for k in list(json_input.keys()):
				if k == '_nodetype' and json_input[k] == nodetype:
					json_input['visited'] = False
				else:
					(self._annotate_dict(json_input[k], nodetype))
		elif isinstance(json_input, list):
			for item in json_input:
				self._annotate_dict(item, nodetype)
	
	def _get_level(self, body, nodetype, level):
		_check = item_generator(body, '_nodetype', nodetype)
		
		try:
			next(_check)
		except(StopIteration):
			pprint(self.j_ast)
			return level
		
		val = item_generator(body, '_nodetype', nodetype)
		
		levels = []
		for v in val:
			levels.append(self._get_level(v, nodetype, level+1))
		
		return max(levels)

	def get_all_levels(self, nodetype):
		levels = []
		self._annotate_dict(self.j_ast, nodetype)
		# pprint(self.j_ast)
		for i, val in enumerate(item_generator(self.j_ast, '_nodetype', nodetype)):
			levels.append(self._get_level(val, nodetype, 0))
		
		return levels
	
	def get_nested_level(self, nodetype):
		return max(self.get_all_levels(nodetype))+1
		
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
	print(l.get_all_levels('While'))
	print(l.get_nested_level('While'))
	# print(l.detect_nested_while_hard(2))
	# print(l.detect_nested_while_soft(1))