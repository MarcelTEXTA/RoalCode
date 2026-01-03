import re

TOKEN_SPEC = [
    ('COMMENT1', r'//.*'),
    ('COMMENT2', r'/\*[\s\S]*?\*/'),
    ('NUMBER',   r'\d+(\.\d+)?'),
    ('STRING',   r'"[^"]*"'),
    ('ID',       r'[A-Za-z_][A-Za-z0-9_\.]*'),
    ('ASSIGN',   r'='),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('MUL',      r'\*'),
    ('DIV',      r'/'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('COMMA',    r','),
    ('NEWLINE',  r'\n'),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.')
]

TOKEN_REGEX = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPEC)

def tokenize(code):
    tokens = []
    for mo in re.finditer(TOKEN_REGEX, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind in ('SKIP','NEWLINE','COMMENT1','COMMENT2'):
            continue
        elif kind == 'NUMBER':
            if '.' in value:
                tokens.append((kind, float(value)))
            else:
                tokens.append((kind, int(value)))
        elif kind == 'STRING':
            tokens.append((kind, value[1:-1]))
        elif kind == 'ID':
            if value in ('true', 'false'):
                tokens.append(('BOOL', value == 'true'))
            else:
                tokens.append((kind, value))
        elif kind in ('ASSIGN','PLUS','MINUS','MUL','DIV','LPAREN','RPAREN','COMMA'):
            tokens.append((kind, value))
        else:
            raise RuntimeError(f"Unexpected character: {value}")
    return tokens