import json
import sys
import re

from ast_to_json import item_generator, file_to_dict

class Loops:
	def __init__(self, j_ast):
		self.j_ast = j_ast

	def detect_nested_while_hard(self, level):
		for i in item_generator(self.j_ast, '_nodetype', 'While'):
			print(i)
		

if __name__ == '__main__':
	ast_dict = file_to_dict(sys.argv[1])
	l = Loops(ast_dict)
	l.detect_nested_while(2)