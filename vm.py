class VM:
    def __init__(self):
        self.stack = []
        self.globals = {}
        self.ip = 0

    def run(self, bytecode):
        self.ip = 0
        while self.ip < len(bytecode):
            instr = bytecode[self.ip]
            op, *args = instr
            if op == "LOAD_INT":
                self.stack.append(args[0])
            elif op == "STORE_VAR":
                self.globals[args[0]] = self.stack.pop()
            elif op == "LOAD_VAR":
                self.stack.append(self.globals[args[0]])
            elif op == "ADD":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif op == "PRINT":
                print(self.stack.pop())
            self.ip += 1
