from lexer import tokenize

class Assign:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class IfStmt:
    def __init__(self, cond, body, elifs=None, else_body=None):
        self.cond = cond
        self.body = body
        self.elifs = elifs or []
        self.else_body = else_body or []

class ForStmt:
    def __init__(self, var, start=None, end=None, step=None, iterable=None, body=None):
        self.var = var
        self.start = start
        self.end = end
        self.step = step
        self.iterable = iterable
        self.body = body or []

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Print:
    def __init__(self, args):
        self.args = args  # liste d'expressions

def parse(tokens):
    i = 0
    stmts = []

    while i < len(tokens):
        tok_type, tok_val = tokens[i]

        # console.print(...)
        if tok_type == 'ID' and tok_val == 'console.print':
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'LPAREN':
                raise SyntaxError("Expected '(' after console.print")
            i += 1
            args = []
            while i < len(tokens) and tokens[i][0] != 'RPAREN':
                args.append(tokens[i])
                i += 1
                if i < len(tokens) and tokens[i][0] == 'COMMA':
                    i += 1
            if i >= len(tokens) or tokens[i][0] != 'RPAREN':
                raise SyntaxError("Expected ')' after console.print arguments")
            i += 1
            stmts.append(Print(args))
            continue

        # déclaration typée
        elif tok_type == 'ID' and tok_val in ('int','float','string','bool'):
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'ID':
                raise SyntaxError("Expected variable name after type")
            name = tokens[i][1]
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'ASSIGN':
                raise SyntaxError("Expected '=' after variable name")
            i += 1
            left_tok = tokens[i]

            # binop
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

        # assignation simple
        elif tok_type == 'ID':
            name = tok_val
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'ASSIGN':
                raise SyntaxError("Expected '=' after variable name")
            i += 1
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

        
        elif tok_type == 'ID' and tok_val == 'if':
            i += 1
            if tokens[i][0] != 'LPAREN':
                raise SyntaxError("Expected '(' after if")
            i += 1
            cond = tokens[i]
            i += 1
            if tokens[i][0] != 'RPAREN':
                raise SyntaxError("Expected ')' after if condition")
            i += 1
            if tokens[i][0] != 'LBRACE':
                raise SyntaxError("Expected '{' after if condition")
            i += 1

            # === PARSING DU BODY ===
            body_tokens = []
            brace_count = 1  # on est dans la première accolade
            while i < len(tokens) and brace_count > 0:
                if tokens[i][0] == 'LBRACE':
                    brace_count += 1
                elif tokens[i][0] == 'RBRACE':
                    brace_count -= 1
                    if brace_count == 0:
                        i += 1  # on saute le '}'
                        break
                if brace_count > 0:
                    body_tokens.append(tokens[i])
                i += 1

            # Parse récursivement le body
            body = parse(body_tokens)
            stmts.append(IfStmt(cond, body))



        else:
            i += 1

    return stmts
