# pylint: skip-file
import ply.lex as lex

# List of token names
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

# Regular expression rules for tokens
t_INTEGER = r'\d+'

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Check if it's a reserved word
    return t

# Reserved words
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'break': 'BREAK',
}

# Operator tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GREATER = r'>'
t_EXPONENT = r'\^'

# Ignored characters
t_ignore = ' \t'

# Error handling rule for invalid characters
def t_error(t):
    print("Invalid character: ", t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Example usage
input_text = "if x > 5 + y * 2 ^ 3 break"
lexer.input(input_text)

for token in lexer:
    print(token)