from lexer import tokenize

class Assign:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Print:
    def __init__(self, expr):
        self.expr = expr

def parse(tokens):
    i = 0
    stmts = []

    while i < len(tokens):
        tok_type, tok_val = tokens[i]

        # --- print(expr) ---
        if tok_type == 'ID' and tok_val == 'print':
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'LPAREN':
                raise SyntaxError("Expected '(' after print")
            i += 1
            if i >= len(tokens):
                raise SyntaxError("Expected expression inside print()")
            expr = tokens[i]
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'RPAREN':
                raise SyntaxError("Expected ')' after print()")
            i += 1
            stmts.append(Print(expr))
            continue

        # --- déclaration typée : int a = 10 ---
        elif tok_type == 'ID' and tok_val in ('int', 'float', 'string', 'bool'):
            var_type = tok_val
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'ID':
                raise SyntaxError("Expected variable name after type")
            name = tokens[i][1]
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'ASSIGN':
                raise SyntaxError("Expected '=' after variable name")
            i += 1
            if i >= len(tokens):
                raise SyntaxError("Expected expression after '='")

            # expression simple ou binaire
            left_tok = tokens[i]
            if i+2 < len(tokens) and tokens[i+1][0] in ('PLUS','MINUS','MUL','DIV'):
                op = tokens[i+1][1]
                right_tok = tokens[i+2]
                expr = BinOp(left_tok, op, right_tok)
                i += 3
            else:
                expr = left_tok
                i += 1

            stmts.append(Assign(name, expr))
            continue

        # --- assignation simple : a = b + 5 ---
        elif tok_type == 'ID':
            name = tok_val
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'ASSIGN':
                raise SyntaxError("Expected '=' after variable name")
            i += 1
            if i >= len(tokens):
                raise SyntaxError("Expected expression after '='")

            left_tok = tokens[i]
            if i+2 < len(tokens) and tokens[i+1][0] in ('PLUS','MINUS','MUL','DIV'):
                op = tokens[i+1][1]
                right_tok = tokens[i+2]
                expr = BinOp(left_tok, op, right_tok)
                i += 3
            else:
                expr = left_tok
                i += 1

            stmts.append(Assign(name, expr))
            continue

        else:
            i += 1

    return stmts
