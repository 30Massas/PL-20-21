import ply.lex as lex
import sys

#tokens = ['NUM','ID','POTENCIA','EQUIV','REPEATUNTIL']
tokens = ['BEGIN','DECL','INSTR','NUM','ID','int','print','END']


literals = ['=','+','-','/','*',
            '(',')',';',',',
#            '<','>',
            '{','}']

#t_EQUIV = r'=='
t_BEGIN = r'BEGIN'
t_DECL = r'DECL'
t_ID = r'\w'
t_NUM = r'\d+'
t_int = r'int'
t_INSTR = r'INSTR'
t_print = r'print'
#t_POTENCIA = r'potencia'
#t_REPEATUNTIL = r'repeatuntil'
t_END = r'END'

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