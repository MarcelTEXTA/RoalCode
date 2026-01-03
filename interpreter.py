from parser import parse, Assign, Print, BinOp, IfStmt, ForStmt
from lexer import tokenize

class Environment:
    def __init__(self):
        self.vars = {}

# ==== EVALUATION D'EXPRESSION ====
def eval_expr(expr, env):
    if isinstance(expr, tuple):
        typ, val = expr
        if typ == 'NUMBER':
            return val
        elif typ == 'STRING':
            return val
        elif typ == 'BOOL':
            return val
        elif typ == 'ID':
            if val not in env.vars:
                raise NameError(f"Variable '{val}' not defined")
            return env.vars[val]
    elif isinstance(expr, BinOp):
        left = eval_expr(expr.left, env)
        right = eval_expr(expr.right, env)
        if expr.op == '+':
            return left + right
        elif expr.op == '-':
            return left - right
        elif expr.op == '*':
            return left * right
        elif expr.op == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right
    else:
        return expr

# ==== EXECUTION DES STATEMENTS ====
def run_statements(stmts, env):
    for stmt in stmts:
        if isinstance(stmt, Assign):
            env.vars[stmt.name] = eval_expr(stmt.expr, env)
        elif isinstance(stmt, Print):
            vals = [str(eval_expr(arg, env)) for arg in stmt.args]
            print(' '.join(vals))
        elif isinstance(stmt, IfStmt):
            if eval_expr(stmt.cond, env):
                run_statements(stmt.body, env)
            else:
                executed = False
                for cond, body in stmt.elifs:
                    if eval_expr(cond, env):
                        run_statements(body, env)
                        executed = True
                        break
                if not executed and stmt.else_body:
                    run_statements(stmt.else_body, env)
        elif isinstance(stmt, ForStmt):
            if stmt.iterable:  # for each
                for val in eval_expr(stmt.iterable, env):
                    env.vars[stmt.var] = val
                    run_statements(stmt.body, env)
            else:  # for classique
                i = eval_expr(stmt.start, env)
                end = eval_expr(stmt.end, env)
                step = eval_expr(stmt.step, env)
                while i < end:
                    env.vars[stmt.var] = i
                    run_statements(stmt.body, env)
                    i += step

# ==== EXECUTION PRINCIPALE ====
def run(code):
    tokens = tokenize(code)
    stmts = parse(tokens)
    env = Environment()
    try:
        run_statements(stmts, env)
    except Exception as e:
        print(f"Erreur: {e}")
    return env
