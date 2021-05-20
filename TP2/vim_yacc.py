import ply.yacc as yacc
from vim_tokens import tokens
import sys

"""
// print(2-3*3+5)

DECL
ENDDECL
INSTR
print(2-3*3+5)
ENDINSTR

pushi 2       
pushi 3           
pushi 3              
mul                          
sub                          
pushi 5
add
writei
"""


def p_Programa(p):
    "Programa : Decl Instr"


def p_Decl(p):
    "Decl : DECL Declaracoes ENDDECL "   

def p_Declaracoes(p):
    "Declaracoes : Declaracoes Declaracao "
    p[0] = str(p[1]) + '\n' + str(p[2])

def p_Declaracoes_Empty(p):
    "Declaracoes : "

def p_Declaracao_Vars_Simples(p):
    "Declaracao : int Vars ';' "
 
def p_Declaracao_Vars_Valor(p):
    "Declaracao : int VarsDeclaradas ';' "

def p_Vars(p):
    "Vars : Vars Var"
    p[0] = str(p[1]) + '\n' + str(p[2])

def p_Vars_Empty(p):
    "Vars : Var "
    p[0] = str(p[1])

def p_Var_ID(p):
    "Var : ID"
    p[0] = 'pushi 0\n'
    p.parser.registers[p[1]] = p.parser.registerindex
    p.parser.registerindex += 1

def p_Var_Array(p):
    "Var : '[' NUM ']' ID"
    p[0] = 'pushn ' + str(p[2]) + '\n'
    p.parser.registers[p[1]] = p.parser.registerindex
    p.parser.registerindex += p[2]

def p_VarsDeclaradas(p):
    "VarsDeclaradas : VarsDeclaradas VarDeclarada"
    p[0] = str(p[1]) + str(p[2])

def p_VarsDeclaradas_Empty(p):
    "VarsDeclaradas : VarDeclarada"
    p[0] = str(p[1])

def p_VarDeclarada(p):
    "VarDeclarada : ID '=' Exp"
    p[0] = 'pushi ' + str(p[3]) + '\n'
    p.parser.registers[p[1]] = p.parser.registerindex
    p.parser.registers[p[1]][p.parser.registerindex] = p[3]
    p.parser.registerindex += 1



def p_Instr(p):
    "Instr : INSTR Instrucoes ENDINSTR "
    p[0] = f'start\n{p[3]}\nstop'

def p_Instrucoes(p):
    "Instrucoes : Instrucoes Instrucao"
    p[0] = str(p[1]) + '\n' + str(p[2])

def p_Instrucoes_Empty(p):
    "Instrucoes : "
    pass
    
def p_Instrucao_print(p):
    "Instrucao : print '(' Exp ')' ';'"
    p[0] = 'writei' + str(p[3]) + '\n'

def p_Instrucao_read(p):
    "Instrucao : input '(' ')' ';'"
    p[0] = 'read\natoi\nstoren\n'

def p_Exp_Termo_add(p):
    "Exp : Exp '+' Termo"
    p[0] = str(p[1]) + str(p[3]) + 'add\n'

def p_Exp_Termo_sub(p):
    "Exp : Exp '-' Termo"
    p[0] = str(p[1]) + str(p[3])+ 'sub\n'

def p_Exp_Termo(p):
    "Exp : Termo"
    p[0] = str(p[1])

def p_Termo_Fator_mul(p):
    "Termo : Termo '*' Fator"
    p[0] = str(p[1]) + str(p[3]) + 'mul\n'

def p_Termo_Fator_div(p):
    "Termo : Termo '/' Fator"
    if (p[3] != '0'):
        p[0] = str(p[1]) + str(p[3]) + 'div\n'
    else:
        p[0] = 'pushi 0\n'

def p_Termo_Fator(p):
    "Termo : Fator"
    p[0] = str(p[1])

def p_Fator_id(p):
    "Fator : ID"
    p[0] = str(p.parser.registers.get(p[1]))

def p_Fator_num(p):
    "Fator : NUM"
    p[0] = 'pushi' + str(p[1]) + '\n'

def p_Fator_Exp(p):
    "Fator : '(' Exp ')'"
    p[0] = str(p[2])

def p_error(p):
    print(f'Syntax Error: {p}')
    parser.success = False

# Build parser
parser = yacc.yacc()
parser.registers = {}
parser.registerindex = 0
parser.fileOut = open('testeLing.vm','w+')

# Read input and parse it
# Line by line
file = open(f"{input('Introduce path to program to be compiled: ')}",'r')

content = ''
for linha in file:
    content += linha
    #print(result)

parser.parse(content)