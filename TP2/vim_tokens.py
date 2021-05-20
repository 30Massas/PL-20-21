import ply.lex as lex
import sys

#tokens = ['NUM','ID','POTENCIA','EQUIV','REPEATUNTIL']


reserved = {
    'DECL' : 'DECL',
    'int' : 'int',
    'INSTR' : 'INSTR',
    'print' : 'print' 
}

literals = ['{','}','=','+','-','/','*',
            '(',')',';',',']

tokens = ['NUM','ID'] + list(reserved.values())
#t_EQUIV = r'=='

def t_ID(t):
    r'\w+'
    t.type = reserved.get(t.value,'ID')
    return t

def t_NUM(t):
    r'\d+'
    t.type = reserved.get(t.value,'NUM')
    t.value = int(t.value)
    return t

#t_POTENCIA = r'potencia'
#t_REPEATUNTIL = r'repeatuntil'

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