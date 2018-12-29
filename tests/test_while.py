from acre.loops import Loops
from acre.ast_to_json import file_to_dict

import pytest

def test_while_single():
	ast_dict = file_to_dict('tests/c_files/single_while.c')
	l = Loops(ast_dict)
	assert l.get_nested_level('While') == 1
	
def test_while_nested():
	ast_dict = file_to_dict('tests/c_files/nested_while.c')
	l = Loops(ast_dict)
	assert l.get_nested_level('While') == 4
	
def test_while_complex():
	ast_dict = file_to_dict('tests/c_files/complex_while.c')
	l = Loops(ast_dict)
	assert l.get_nested_level('While') == 5

