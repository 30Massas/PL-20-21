import ply.yacc as yacc
from vim_tokens import tokens
import sys

#############################################################
#                       Main Program                        #
#############################################################
def p_Programa(p):
    "Programa : Decl Instr"
    p.parser.fileOut.write(f'{p[1]}start\n{p[2]}stop')

#############################################################
#                     Bloco Declarações                     #
#############################################################
def p_Decl(p):
    "Decl : DECL Declaracoes ENDDECL "   
    p[0] = p[2]

def p_Declaracoes(p):
    "Declaracoes : Declaracoes Declaracao "
    p[0] = p[1] + p[2]

def p_Declaracoes_Empty(p):
    "Declaracoes : "
    p[0] = ""

def p_Declaracao_Variaveis(p):
    "Declaracao : int Variaveis ';' "
    p[0] = p[2]

def p_Declaracao_Arrays(p):
    "Declaracao : int Arrays ';'" 
    p[0] = p[2]   

def p_Variaveis(p):
    "Variaveis : Variaveis ',' Variavel "
    p[0] = p[1] + p[3]

def p_Variaveis_Simples(p):
    "Variaveis : Variavel "
    p[0] = p[1]

def p_Variavel_Vars(p):
    "Variavel : Var"
    p[0] = p[1]

def p_Variavel_VarsDeclaradas(p):
    "Variavel : VarDeclarada"
    p[0] = p[1]

def p_Arrays(p):
    "Arrays : Arrays Array"
    p[0] = p[1] + p[2]

def p_Arrays_Unica(p):
    "Arrays : Array"
    p[0] = p[1]

def p_Array_Uma_Dimensao(p):
    "Array : ArrayDimensaoSimples"
    p[0] = p[1]

def p_Array_Duas_Dimensoes(p):
    "Array : ArrayDimensaoDupla"
    p[0] = p[1]
    
def p_ArrayDimensaoSimples(p):
    "ArrayDimensaoSimples : '[' NUM ']' ID"
    p[0] = 'pushn ' + p[2] + '\n'
    p.parser.registers[p[4]] = p.parser.registerindex
    p.parser.registerindex += int(p[2])

def p_ArrayDimensaoDupla(p):
    "ArrayDimensaoDupla : '[' NUM ']' '[' NUM ']' ID"
    p[0] = 'pushn ' + str(int(p[2])*int(p[5])) + '\n'
    p.parser.registers[p[7]] = p.parser.registerindex
    p.parser.registerindex += int(p[2])*int(p[5])
    p.parser.matrizes[p[7]] = int(p[5])

def p_Var_ID(p):
    "Var : ID"
    p[0] = 'pushi 0\n'
    p.parser.registers[p[1]] = p.parser.registerindex
    p.parser.registerindex += 1

def p_VarDeclarada(p):
    "VarDeclarada : ID EQUALS Exp"
    p[0] = p[3]
    p.parser.registers[p[1]] = p.parser.registerindex
    p.parser.registerindex += 1

#############################################################
#                      Bloco Instruções                     #
#############################################################

def p_Instr(p):
    "Instr : INSTR Instrucoes ENDINSTR "
    p[0] = p[2]

def p_Instrucoes(p):
    "Instrucoes : Instrucoes Instrucao"
    p[0] = p[1] + p[2]

def p_Instrucoes_Empty(p):
    "Instrucoes : "
    p[0] = ""
    
def p_Instrucao_Print(p):
    "Instrucao : print '(' Exp ')' ';'"
    p[0] = p[3] + 'writei' + '\n'

def p_Instrucao_Read(p):
    "Instrucao : input '(' ID ')' ';'"
    p[0] = 'read\natoi\n' + 'storeg ' + str(p.parser.registers.get(p[3])) + '\n'

def p_Instrucao_Atrib(p):
    "Instrucao : ID EQUALS Exp ';'"
    p[0] = p[3] + 'storeg ' + str(p.parser.registers.get(p[1])) + '\n'

def p_Instrucao_Atrib_Array(p):
    "Instrucao : ID '[' Exp ']' EQUALS Exp ';'"
    p[0] = 'pushgp\npushi ' + str(p.parser.registers.get(p[1]))  + '\npadd\n' + p[3] + p[6] + 'storen\n'

def p_Instrucao_Atrib_Matrix(p):
    "Instrucao : ID '[' Exp ']' '[' Exp ']' EQUALS Exp ';'"
    p[0] = 'pushgp\npushi ' + str(p.parser.registers.get(p[1])) + '\npadd\n' +  p[6] + p[3] + 'pushi ' + str(p.parser.matrizes[p[1]]) + '\nmul\nadd\n'  + p[9] + 'storen\n'

def p_Instrucao_If(p):
    "Instrucao : IF '(' Conds ')' Instrucoes ENDIF "
    p[0] = f'{p[3]}jz endif{p.parser.ifs}\n{p[5]}endif{p.parser.ifs}:\n'
    p.parser.ifs += 1

def p_Instrucao_If_Else(p):
    "Instrucao : IF '(' Conds ')' Instrucoes Else ENDIF "
    p[0] = f'{p[3]}jz else{p.parser.elses}\n{p[5]}jump endelse{p.parser.elses}\nelse{p.parser.elses}:\n{p[6]}jump endelse{p.parser.elses}\nendelse{p.parser.elses}:\n'
    p.parser.elses += 1

def p_Else(p):
    "Else : ELSE Instrucoes ENDELSE"
    p[0] = p[2]

def p_Instrucao_Repeat_Until(p):
    "Instrucao : REPEAT Instrucoes UNTIL '(' Conds ')' "
    p[0] = f'r{p.parser.ciclos}:\n{p[2]}{p[5]}jz r{p.parser.ciclos}\n'
    p.parser.ciclos += 1

def p_Instrucao_While_Do(p):
    "Instrucao : WHILE '(' Conds ')' DO Instrucoes ENDWHILE"
    p[0] = f'while{p.parser.ciclos}:\n{p[3]}jz fimwhile{p.parser.ciclos}\n{p[6]}jump while{p.parser.ciclos}\nfimwhile{p.parser.ciclos}:\n'
    p.parser.ciclos += 1

#############################################################
#                      Bloco Condições                      #
#############################################################

def p_Conds_And(p):
    "Conds : Conds AND Cond"
    p[0] = p[1] + p[3] + 'add\npushi 2\nequal\n'

def p_Conds_Or(p):
    "Conds : Conds OR Cond"
    p[0] = p[1] + p[3] + 'add\npushi 0\nsup\n'

def p_Conds_Unica(p):
    "Conds : Cond"
    p[0] = p[1]

def p_Cond_Equivalent(p):
    "Cond : Exp EQUIVALENT Exp"
    p[0] = p[1] + p[3] + 'equal\n'

def p_Cond_Different(p):
    "Cond : Exp DIFFERENT Exp"
    p[0] = p[1] + p[3] + 'equal\nnot\n'

def p_Cond_Greater(p):
    "Cond : Exp GREATER Exp"
    p[0] = p[1] + p[3] + 'sup\n'

def p_Cond_Greater_Equal(p):
    "Cond : Exp GREATEREQUAL Exp"
    p[0] = p[1] + p[3] + 'supeq\n'

def p_Cond_Lesser(p):
    "Cond : Exp LESSER Exp"
    p[0] = p[1] + p[3] + 'inf\n'

def p_Cond_Lesser_Equal(p):
    "Cond : Exp LESSEREQUAL Exp"
    p[0] = p[1] + p[3] + 'infeq\n'


#############################################################
#                      Bloco Expressões                     #
#############################################################

def p_Exp_Termo_add(p):
    "Exp : Exp ADD Termo"
    p[0] = p[1] + p[3] + 'add\n'

def p_Exp_Termo_sub(p):
    "Exp : Exp SUB Termo"
    p[0] = p[1] + p[3]+ 'sub\n'

def p_Exp_Termo(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_Fator_mul(p):
    "Termo : Termo MUL Fator"
    p[0] = p[1] + p[3] + 'mul\n'

def p_Termo_Fator_div(p):
    "Termo : Termo DIV Fator"
    if (p[3] != '0'):
        p[0] = p[1] + p[3] + 'div\n'
    else:
        p[0] = 'pushi 0\n'

def p_Termo_Fator_mod(p):
    "Termo : Termo MOD Fator"
    p[0] = p[1] + p[3] + 'mod\n'

def p_Termo_Fator(p):
    "Termo : Fator"
    p[0] = p[1]

def p_Fator_ID(p):
    "Fator : ID"
    p[0] = 'pushg ' + str(p.parser.registers.get(p[1])) + '\n'

def p_Fator_ID_Array(p):
    "Fator : ID '[' Exp ']' "
    p[0] = 'pushgp\npushi ' + str(p.parser.registers.get(p[1])) + '\npadd\n' + p[3] + 'loadn\n'

def p_Fator_ID_Matrix(p):
    "Fator : ID '[' Exp ']' '[' Exp ']' "
    p[0] = 'pushgp\npushi ' + str(p.parser.registers.get(p[1])) + '\npadd\n' + p[6] + p[3] + 'pushi ' + str(p.parser.matrizes[p[1]]) + '\nmul\nadd\n' + 'loadn\n'

def p_Fator_num(p):
    "Fator : NUM"
    p[0] = 'pushi ' + p[1] + '\n'

def p_Fator_Exp(p):
    "Fator : '(' Exp ')'"
    p[0] = p[2]

#############################################################
#                      Bloco Yacc Geral                     #
#############################################################

def p_error(p):
    print(f'Syntax Error: {p}')
    parser.success = False

# Build parser
parser = yacc.yacc()
parser.registers = {} # id : offset
parser.matrizes = {} # id : tamanho das colunas 
parser.registerindex = 0 # valor do offset
parser.ifs = 0 # total de ifs
parser.elses = 0 # total de elses
parser.ciclos = 0 # total de ciclos
parser.fileOut = open('teste.vm','w+')

# Read input and parse it
# Line by line
file = open(f"{input('Introduce path to program to be compiled: ')}",'r')

content = ''
for linha in file:
    content += linha
    #print(result)

parser.parse(content)