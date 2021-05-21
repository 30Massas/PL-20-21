import ply.lex as lex
import sys

#tokens = ['NUM','ID','POTENCIA','EQUIV','REPEATUNTIL']


reserved = {
    'DECL' : 'DECL',
    'ENDDECL' : 'ENDDECL',
    'int' : 'int',
    'INSTR' : 'INSTR',
    'ENDINSTR' : 'ENDINSTR',
    'print' : 'print',
    'input' : 'input',
    'IF' : 'IF',
    'ENDIF' : 'ENDIF',
    'ELSE' : 'ELSE',
    'ENDELSE' : 'ENDELSE',
    'AND' : 'AND',
    'OR'  : 'OR',
    'REPEAT' : 'REPEAT',
    'UNTIL' : 'UNTIL'
}

literals = ['(',')',';',',','[', ']']

tokens = ['NUM','ID',
          'ADD','SUB','MUL','DIV','MOD',
          'GREATER','LESSER','GREATEREQUAL','LESSEREQUAL','EQUIVALENT','DIFFERENT','EQUALS'] + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_ADD(t):
    r'\+'
    t.type = reserved.get(t.value,'ADD')
    return t

def t_SUB(t):
    r'-'
    t.type = reserved.get(t.value,'SUB')
    return t

def t_MUL(t):
    r'\*'
    t.type = reserved.get(t.value,'MUL')
    return t

def t_DIV(t):
    r'/'
    t.type = reserved.get(t.value,'DIV')
    return t

def t_MOD(t):
    r'%'
    t.type = reserved.get(t.value,'MOD')
    return t

def t_EQUIVALENT(t):
    r'=='
    t.type = reserved.get(t.value, 'EQUIVALENT')
    return t

def t_DIFFERENT(t):
    r'!='
    t.type = reserved.get(t.value, 'DIFFERENT')
    return t

def t_GREATEREQUAL(t):
    r'>='
    t.type = reserved.get(t.value, 'GREATEREQUAL')
    return t

def t_GREATER(t):
    r'>'
    t.type = reserved.get(t.value, 'GREATER')
    return t

def t_LESSEREQUAL(t):
    r'<='
    t.type = reserved.get(t.value, 'LESSEREQUAL')
    return t

def t_LESSER(t):
    r'<'
    t.type = reserved.get(t.value, 'LESSER')
    return t


def t_EQUALS(t):
    r'='
    t.type = reserved.get(t.value,'EQUALS')
    return t

def t_NUM(t):
    r'-?\d+'
    t.type = reserved.get(t.value,'NUM')
    return t

'''

BLOCO DECLARAÇÕES
int x;
int ow;


BLODO DE INSTRUÇÕES

potencia(2,3)

POTENCIAL LINGUAGEM

{ || BEGIN // start

    DECL
    {
        int a,b,c,d;
    }

    INSTR
    {
        a = input();
        b = input();
        c = input();
        d = input();

        if(a==b){
            if(b==c){
                if(c==d){
                    print(1);
                }
                else{
                    print(0);
                }
            }
            else{
                print(0);
            }
        }
        else{
            print(0);
        }        
    }

} || END // stop

EXEMPLO

    int a,b,c,d

    read(a) -> Compilador pede ao utilizador para introduzir valor 
    read(b)
    read(c)
    read(d)
    
    RESTO DO CODIGO

'''

t_ignore = " \t\n"

def t_error(t):
    print(f'Caratér ilegal: {t.value[0]}')
    t.lexer.skip(1)
    return t

#build the lexer
lexer = lex.lex()

# file = open('teste.txt')

# for line in file:
#     lexer.input(line)
#     tok = lexer.token()
#     while tok:
#         print(tok)
#         tok = lexer.token()