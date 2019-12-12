#!/usr/bin/python3
#  coding: UTF-8
#------------------------------------------------------------
# lex.py
# Melissa Escobar Gutiérrez, melissa.escobar@utp.edu.co
# tokenizer
# ------------------------------------------------------------

import ply.lex as lex
import sys

# This is a list of reserved words available in Pascal:

# and	    array	begin	    case	    const       else        int
# div	    do	    downto	    else	    end         REAL       return
# file	    for	    function	goto	    if          not         skip
# in	    label	mod	        nil	        not         break       and 
# of	    or	    packed 	    procedure	program     
# record	repeat	set	        then	    to
# type	    until	var	        while	    with

# list of tokens
tokens = (
	# Reserverd words

	'ELSE',
	'BREAK', 
	'CASE',
	'IF',
	'INT',
	'FLOAT',
	'CHAR',
	'BOOLEAN',
	'DEFINE',
	'EXTERN',
	'DEFAULT', 
	'FOR',
	'RETURN',
	'WHILE',
	'AND',
	'OR',
	'FALSE',
	'TRUE',
	'END',
   
	# Symbols
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'LESS',
	'LESSEQUAL',
	'GREATER',
	'GREATEREQUAL',
	'EQUAL',
	'DEQUAL',
	'ISEQUAL',
	'DISTINT',
	'SEMICOLON',
	'COMMA',
	'LPAREN',
	'RPAREN',
	'LBRACKET',
	'RBRACKET',
	'COLON',
	'LBLOCK',
	'RBLOCK',
   	'DO',
	'DOT',
	'VOID',
	'INCLUDE',
	'PROGRAM',

	# Others   
	'ID', 
	'NUMBER',
	'COMMENT',
	'VAR',
	'FUNCTION',
	'BEGIN',
	'THEN',
	'OF',
	'TO',
	'HASHTAG',
	'PROCEDURE',
	'CONST'
	)

# Regular expressions rules for tokens

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_DOT = r'\.'
t_HASHTAG = r'\#'

# 
def t_BREAK(t):
	r'break'
	return t

def t_OR(t):
	r'or'
	return t

def t_AND(t):
	r'and'
	return t

def t_PROGRAM(t):
	r'program'
	return t


def t_CASE(t):
	r'case'
	return t

def t_INCLUDE(t):
	r'include'
	return t

def BEGIN(t):
	r'begin'
	return t

def t_END(t):
	r'end'
	return t

def t_CHAR(t):
	r'char'
	return t

def t_BOOLEAN(t):
	r'boolean'
	return t

def t_EXTERN(t):
	r'extern'
	return t


def t_FALSE(t):
	r'false'
	return t

def t_TRUE(t):
	r'true'
	return t

def t_DEFINE(t):
	r'define'
	return t

def t_CONTINUE(t):
	r'continue'
	return t

def t_DEFAULT(t):
	r'default'
	return t

def t_DO(t):
	r'do'
	return t


def t_ELSE(t):
	r'else'
	return t

def t_REAL(t):
	r'real'
	return t

def t_FOR(t):
	r'for'
	return t

def t_IF(t):
	r'if'
	return t

def t_INT(t):
	r'int'
	return t


def t_RETURN(t):
	r'return'
	return t

def t_VOID(t):
	r'void'
	return t

	
def t_WHILE(t):
	r'while'
	return t

def t_VAR(t):
	r'var'
	return t

def t_FUNCTION(t):
	r'function'
	return t

def t_THEN(t):
	r'then'
	return t

def t_OF(t):
	r'of'
	return t

def t_TO(t):
	r'to'
	return t

def t_PROCEDURE(t):
	r'PROCEDURE'
	return t

def t_CONST(t):
	r'CONST'
	return t


def t_NUMBER(t):
	r'\d+(\.\d+)?'
	t.value = float(t.value)
	return t

def t_ID(t):
	r'\w+(_\d\w)*'
	return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t
	

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_COMMENT(t):
	r'\(\*([-|_|+|.|:| |\n]|[a-zA-Z]|[0-9])*\*\)|{([-|_|+|.|:| |\n]|[a-zA-Z]|[0-9])*}'
	t.lexer.lineno += t.value.count('\n')
	return t

def t_error(t):
	print("Lexical error:{} on line:{} ".format( str(t.value[0]),t.lexer.lineno ))
	t.lexer.skip(1)
	
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = '../compilers/eval.txt'
	f = open(fin, 'r')
	data = f.read()
	# print (data)
	test(data, lexer)
	input()


