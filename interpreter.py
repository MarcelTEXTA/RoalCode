from parser import parse
from lexer import tokenize

class Environment:
    def __init__(self):
        self.vars = {}

def eval_expr(expr, env):
    # simple binop
    if isinstance(expr, tuple):
        typ, val = expr
        if typ == 'NUMBER':
            return val
        elif typ == 'ID':
            return env.vars[val]
    else:  # BinOp
        left = eval_expr(expr.left, env)
        right = eval_expr(expr.right, env)
        if expr.op == '+':
            return left + right
        if expr.op == '-':
            return left - right
        if expr.op == '*':
            return left * right
        if expr.op == '/':
            return left / right

def run(code):
    tokens = tokenize(code)
    stmts = parse(tokens)
    env = Environment()
    for stmt in stmts:
        if isinstance(stmt, Assign):
            value = eval_expr(stmt.expr, env)
            env.vars[stmt.name] = value
        elif isinstance(stmt, Print):
            value = eval_expr(stmt.expr, env)
            print(value)
            # auto print for test.rc call of print(a) ?
    return env

