#!/usr/bin/env python3.7
from lexicalPascal import tokens
import ply.yacc as yacc
import lexicalPascal
import sys

VERBOSE = 1

def p_programb(p):
	'programb : PROGRAM ID SEMICOLON basic_d BEGIN declaration_list END'
	pass

def p_basic_d(p):
	'''basic_d : basic_dec
               | basic_d basic_dec 
    '''
	pass

def p_basic_dec(p): 
	'''basic_dec : header_declaration
                | const_declaration
                | comment_declaration
				| var_declaration
    '''
	pass

def p_const_declaration(p):
	'''const_declaration : CONST comment_declaration ID EQUAL NUMBER SEMICOLON
                         | CONST ID EQUAL NUMBER SEMICOLON comment_declaration
	''' 
	pass


def p_declaration_list_1(p):
	'declaration_list : declaration_list  declaration' 
	pass

def p_declaration_list_2(p):
	'''declaration_list : declaration
						| comment_declaration				
	'''
	pass

def p_comment_declaration(p):
	'''comment_declaration : COMMENT
				  			| COMMENT declaration_list
	''' 
	pass

def p_declaration(p):
	'''declaration : fun_declaration
				  | selection_stmt 
				  | iteration_stmt
	'''
	pass

def p_header_declaration_1(p):
	'''header_declaration : HASHTAG DEFINE ID NUMBER
						  | HASHTAG DEFINE ID NUMBER declaration_list '''
	pass

def p_header_declaration_2(p):
	'''header_declaration : HASHTAG INCLUDE ID DOT ID
						  | HASHTAG INCLUDE ID DOT ID declaration_list
	'''
	pass



def p_var_declaration_1(p): #normal variables definition
	'''var_declaration : VAR var_declaration2 COLON type_specifier SEMICOLON declaration_list
						| VAR comment_declaration var_declaration2 COLON type_specifier SEMICOLON declaration_list
						| VAR var_declaration2 COLON type_specifier SEMICOLON comment_declaration declaration_list
	'''
	pass

def p_var_declaration_2(p):#array definition
	'var_declaration : VAR ID LBRACKET NUMBER RBRACKET COLON type_specifier SEMICOLON declaration_list'
	pass

def p_var_declaration_3(p):                     
	'''var_declaration2 : ID COMMA var_declaration2  
	                               | ID
	                               | ID EQUAL NUMBER COMMA var_declaration2
	                               | ID EQUAL NUMBER
	                               | ID EQUAL ID COMMA var_declaration2
	                               | ID EQUAL ID

        '''
	pass

def p_type_specifier_1(p):
	'type_specifier : INT'
	pass

def p_type_specifier_2(p):
	'type_specifier : VOID'
	pass


def p_type_specifier_3(p):
	'type_specifier : FLOAT'
	pass

def p_type_specifier_4(p):
	'type_specifier : CHAR'
	pass

def p_type_specifier_5(p):
	'type_specifier : BOOLEAN'
	pass


	# ---------------------------- Functions -----------------------------------
# 	function name(argument(s): type1; argument(s): type2; ...): function_type;
# local declarations;

# begin
#    ...
#    < statements >
#    ...
#    name:= expression;
# end;

def p_fun_declaration(p):
	'''fun_declaration : FUNCTION ID LPAREN params RPAREN COLON type_specifier SEMICOLON compount_stmt
					   | FUNCTION ID LPAREN params RPAREN COLON type_specifier SEMICOLON declaration_list
	'''
	pass

# def p_function_token(p):
# 	'function_token : function'
# 	pass

def p_params_1(p):
	'params : param_list'
	pass

def p_params_2(p):
	'params : VOID'
	pass

def p_param_list_1(p):
	'param_list : param_list COMMA param'
	pass

def p_param_list_2(p):
	'param_list : param'
	pass

def p_param_list_3(p):
	'param_list : empty'
	pass

def p_param_1(p):
	'param : ID COLON type_specifier'  ###################
	pass

def p_param_2(p):
	'param : type_specifier ID LBRACKET RBRACKET'
	pass

def p_param_3(p):
	'param : ID'
	pass

def p_compount_stmt(p):
	'compount_stmt : local_declarations statement_list'
	pass

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	pass

def p_local_declarations_2(p):
	'local_declarations : empty'
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : empty'	
	pass

def p_statement(p):
	'''statement : expression_stmt
				| compount_stmt
				| selection_stmt 
				| iteration_stmt
				| return_stmt
	'''
	pass

def p_expression_stmt_1(p):
	'expression_stmt : expression SEMICOLON'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : SEMICOLON'
	pass

def p_selection_stmt_1(p):
	'selection_stmt : BEGIN IF LPAREN expression RPAREN THEN statement END SEMICOLON'  ######## 
	pass

def p_selection_stmt_2(p):
	'selection_stmt : BEGIN IF LPAREN expression RPAREN THEN statement ELSE statement END SEMICOLON'
	pass

# def p_selection_stmt_3(p):
# 	'selection_stmt : SWITCH LPAREN var RPAREN statement'
# 	pass


# def p_case_statement(p):
# 	''' case_statement : NUMBER COLON statement SEMICOLON
# 						|ID COLON statement SEMICOLON
# 	'''
# 	pass

# def p_selection_stmt_5(p):
# 	'selection_stmt : DEFAULT COLON statement BREAK SEMICOLON'
# 	pass



def p_iteration_stmt_1(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN DO BEGIN statement END'
	pass

# while statement 
# def p_while_statement(p):
# 	'while_statement : BEGIN statement END'
# 	pass

# -------------- for statement ----------
# For x:=0 to contar do begin
#         write('Voy por el ');
#         writeln(x);
#     end;


def p_iteration_stmt_2(p):
	'iteration_stmt : FOR ID COLON EQUAL TO ID DO BEGIN statement END SEMICOLON '
	pass

def p_return_stmt_1(p):
	'return_stmt : RETURN SEMICOLON'
	pass

def p_return_stmt_2(p):
	'return_stmt : RETURN expression SEMICOLON'
	pass

def p_expression_1(p):
	'expression : variab EQUAL expression' ### variab EQUAL variab EQUAL expression -> it shouldnt
	pass

def p_expression_2(p):
	'expression : simple_expression'
	pass

# def p_expression_3(p):
# 	'expression : variab EQUAL AMPERSANT ID'
# 	pass

def p_variab_1(p):
	'variab : ID'
	pass

def p_variab_2(p):
	'variab : ID LBRACKET expression RBRACKET'
	pass

def p_simple_expression_1(p):
	'simple_expression : expp relop expp'
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass

def p_expp(p):
	'''expp : additive_expression 
			| ID
			| NUMBER
	'''
	pass


def p_relop(p):
	'''relop : LESS 
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| DEQUAL
			| DISTINT
			| ISEQUAL
	'''
	pass

def p_additive_expression_1(p):
	'''additive_expression : additive_expression addop term
                                              
        '''
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass

# def p_additive_expression_3(p):
# 	'additive_expression : term MINUSMINUS'
# 	pass

# def p_additive_expression_4(p):
# 	'additive_expression : term PLUSPLUS'
# 	pass

def p_addop(p):
	'''addop : PLUS 
			| MINUS
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass



def p_mulop(p):
	'''mulop : 	TIMES
				| DIVIDE
	'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	pass

def p_factor_2(p):
	'factor : VAR'
	pass

def p_factor_3(p):
	'factor : call' # function  call :O
	pass

def p_factor_4(p):
	'factor : NUMBER' 
	pass



def p_call(p):
	'call : ID LPAREN args RPAREN' # semicolon?
	pass

def p_args(p):
	'''args : args_list
			| empty
	'''
	pass

def p_args_list_1(p):
	'args_list : args_list COMMA expression'
	pass

def p_args_list_2(p):
	'args_list : expression'
	pass

def p_empty(p):
	'empty :'
	pass


def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		
print('----------')
parser = yacc.yacc()
print('----------xxx')
if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'eval.txt'

	f = open(fin, 'r')
	data = f.read()
	print (data)
	parser.parse(data, tracking=True)
	print("Parser works")
	input()



	#Documentation
	#variables definition: https://www.tutorialspoint.com/pascal/pascal_variable_types.htm
	#functions definition: 