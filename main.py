# main
from lexer import lexer
from ast import *
from compiler import Compiler
from vm import VM

# exemple de code RoalCode
code = """
int a = 10
int b = 5
a = a + b
print(a)
"""

tokens = lexer(code)

# TODO : parser à partir de tokens pour générer AST
ast_root = Program(statements=[
    VarDecl("int","a", IntLiteral(10)),
    VarDecl("int","b", IntLiteral(5)),
    Assign("a", BinOp(IntLiteral(10), "+", IntLiteral(5))),
    Print(VarDecl("int","a", IntLiteral(0)))  # simplifié pour exemple
])

compiler = Compiler()
compiler.compile(ast_root)
bytecode = compiler.bytecode

vm = VM()
vm.run(bytecode)
