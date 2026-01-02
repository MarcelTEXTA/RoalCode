import compiler

class Node: pass

class VarDecl(Node):
    def __init__(self, var_type, name, value):
        self.var_type = var_type
        self.name = name
        self.value = value

class BinOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class IntLiteral(Node):
    def __init__(self, value):
        self.value = value

# parser minimal pour "int a = 10"
tokens = compiler.lexer('int a = 10')
# AST = VarDecl('int','a', IntLiteral(10))
