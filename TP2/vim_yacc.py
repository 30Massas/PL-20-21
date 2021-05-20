import ply.yacc as yacc
from vim_tokens import tokens
import sys

"""
// print 2-3*3+5

BEGIN{
    DECL{
    }
    INSTR{
        print(2-3*3+5)
    }
}END

pushi 2       
pushi 3           
pushi 3              
mul                          
sub                          
pushi 5
add
writei
"""


# Programa -> Decl Instr
#
# Decl -> DECL '{' Declaracoes '}'
#
# Declaracoes -> Declaracoes Declaracao
#              | Declaracao
#
# Declaracao -> €
#              | ListaIdsSimples RestoIdsSimples
#              | ListaIdsDeclarado RestoIdsDeclarado
#
# ListaIdsSimples -> int id
#     
# RestoIds -> ';'
#           | ',' id ListaIds
#           | ',' id '=' num ListaIds
#
#
# Instr -> INSTR '{' Instrucoes '}'
# 
# Instrucoes -> €
#             | print '(' Exp ')' ';'
#                   
#
# Exp -> Exp '+' Termo
#      | Exp '-' Termo
#      | Termo
#
# Termo -> Termo '*' Fator
#        | Termo '/' Fator
#        | Fator
#
# Fator -> '(' Exp ')'
#        | num
#        | id
#

def p_Programa(p):
    "Programa : Decl Instr"

def p_Decl(p):
    "Decl : DECL '{' Declaracoes '}' "
    
# def p_Decl_Empty(p):
#     "Decl : "    

def p_Declaracoes(p):
    "Declaracoes : Declaracoes Declaracao"

def p_Declaracoes_Unica(p):
    "Declaracoes : Declaracao"

def p_Declaracao_Simples(p):
    "Declaracao : int ID ';' " #ListaIds"
    p.parser.fileOut.write(f'pushi 0\n')
    p.parser.registers[p[2]] = p.parser.registerindex
    p.parser.registerindex += 1

def p_Declaracao_Valor(p):
    "Declaracao : int ID '=' Exp ';' "
    p.parser.fileOut.write(f'pushi {p[4]}')

def p_Declaracao_Empty(p):
    "Declaracao : "

# def p_ListaIds_End(p):
#     "ListaIds : ';'"

# def p_ListaIds_Simples(p):
#     "ListaIds : ',' ID ListaIds"

# def p_ListaIds_Valor(p):
#     "ListaIDs : ',' ID '=' NUM ListaIds"

def p_Instr(p):
    "Instr : INSTR '{' Instrucoes '}' "
    p.parser.fileOut.write(f'start\n{p[3]}\nstop')

# def p_Instr_Empty(p):
#     "Instr : "

def p_Instrucoes(p):
    "Instrucoes : Instrucoes Instrucao"

def p_Instrucoes_Unica(p):
    "Instrucoes : Instrucao"

def p_Instrucao(p):
    "Instrucao : print '(' Exp ')' ';'"
    p.parser.fileOut.write(f'pushg {p.parser.registers.get(p[3])}\nwritei\n')

def p_Instrucao_Empty(p):
    "Instrucao : "

def p_Exp_Termo_add(p):
    "Exp : Exp '+' Termo"
    p[0] = p[1] + p[3] + 'add\n'

def p_Exp_Termo_sub(p):
    "Exp : Exp '-' Termo"
    p[0] = p[1] + p[3] + 'sub\n'

def p_Exp_Termo(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_Fator_mul(p):
    "Termo : Termo '*' Fator"
    p[0] = p[1] + p[3] + 'mul\n'

def p_Termo_Fator_div(p):
    "Termo : Termo '/' Fator"
    if (p[3] != '0'):
        p[0] = p[1] + p[3] + 'div\n'
    else:
        p[0] = 'pushi 0\n'

def p_Termo_Fator(p):
    "Termo : Fator"
    p[0] = p[1]

def p_Fator_id(p):
    "Fator : ID"
    p[0] = str(p.parser.registers.get(p[1]))

def p_Fator_num(p):
    "Fator : NUM"
    p[0] = 'pushi' + p[1] + '\n'

def p_Fator_Exp(p):
    "Fator : '(' Exp ')'"
    p[0] = p[1]

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