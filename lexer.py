# pylint: skip-file
import ply.lex as lex

# Lista de nombres de los tokens
tokens = [
    'INTEGER',
    'VARIABLE',
    'IF',
    'ELSE',
    'WHILE',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'GREATER',
    'EXPONENT',
    'BREAK',
]

# Expresiones regulares para los tokens
t_INTEGER = r'\d+'

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Verifica si es una palabra reservada
    return t

# Palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'break': 'BREAK',
}

# Tokens de operadores
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GREATER = r'>'
t_EXPONENT = r'\^'

# Caracteres ignorados
t_ignore = ' \t'

# Manejo de errores para caracteres invalidos
def t_error(t):
    print("Invalid character: ", t.value[0])
    t.lexer.skip(1)

# Creacion del lexer
lexer = lex.lex()

# Funcion para leer el archivo de entrada
def read_input_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# Ejemplo
file_name = "programa.txt"
input_text = read_input_file(file_name)
lexer.input(input_text)

for token in lexer:
    print(token)