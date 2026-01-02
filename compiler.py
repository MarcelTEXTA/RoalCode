import re

TOKEN_REGEX = [
    (r'\s+', None),          # espaces -> ignorés
    (r'//.*', None),         # commentaire ligne -> ignoré
    (r'/\*.*?\*/', None),    # commentaire bloc -> ignoré
    (r'\bint\b', 'INT'),
    (r'\bfloat\b', 'FLOAT'),
    (r'\bstring\b', 'STRING'),
    (r'\bbool\b', 'BOOL'),
    (r'\bif\b', 'IF'),
    (r'\belse\b', 'ELSE'),
    (r'\bfor\b', 'FOR'),
    (r'\bwhile\b', 'WHILE'),
    (r'\btrue\b', 'TRUE'),
    (r'\bfalse\b', 'FALSE'),
    (r'\d+\.\d+', 'FLOAT_LIT'),
    (r'\d+', 'INT_LIT'),
    (r'"[^"]*"', 'STRING_LIT'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENT'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MUL'),
    (r'/', 'DIV'),
    (r'==', 'EQ'),
    (r'!=', 'NEQ'),
    (r'>=', 'GTE'),
    (r'<=', 'LTE'),
    (r'>', 'GT'),
    (r'<', 'LT'),
    (r'=', 'ASSIGN'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r'\[', 'LBRACKET'),
    (r'\]', 'RBRACKET'),
    (r',', 'COMMA'),
    (r';', 'SEMICOLON'),
]

def lexer(code):
    pos = 0
    tokens = []
    while pos < len(code):
        match = None
        for pattern, type_ in TOKEN_REGEX:
            regex = re.compile(pattern, re.DOTALL)
            match = regex.match(code, pos)
            if match:
                if type_:
                    tokens.append((type_, match.group(0)))
                break
        if not match:
            raise SyntaxError(f"Unexpected character: {code[pos]}")
        else:
            pos = match.end(0)
    return tokens
