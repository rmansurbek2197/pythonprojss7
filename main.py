class Interpreter:
    def __init__(self):
        self.variables = {}

    def parse(self, code):
        tokens = code.split()
        for token in tokens:
            if token == 'let':
                self.assign(tokens)
            elif token == 'print':
                self.print_value(tokens)

    def assign(self, tokens):
        var_name = tokens[1]
        value = int(tokens[3])
        self.variables[var_name] = value

    def print_value(self, tokens):
        var_name = tokens[1]
        print(self.variables[var_name])

    def run(self, code):
        self.parse(code)

def main():
    interpreter = Interpreter()
    while True:
        code = input('>>> ')
        if code == 'exit':
            break
        try:
            interpreter.run(code)
        except Exception as e:
            print(f'Error: {e}')

class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0

    def tokenize(self):
        tokens = []
        while self.pos < len(self.code):
            char = self.code[self.pos]
            if char.isspace():
                self.pos += 1
            elif char.isdigit():
                token = ''
                while self.pos < len(self.code) and self.code[self.pos].isdigit():
                    token += self.code[self.pos]
                    self.pos += 1
                tokens.append(token)
            else:
                tokens.append(char)
                self.pos += 1
        return tokens

def tokenize_code(code):
    lexer = Lexer(code)
    return lexer.tokenize()

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        ast = []
        while self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            if token == 'let':
                ast.append(self.parse_assign())
            elif token == 'print':
                ast.append(self.parse_print())
            else:
                self.pos += 1
        return ast

    def parse_assign(self):
        self.pos += 1
        var_name = self.tokens[self.pos]
        self.pos += 1
        value = int(self.tokens[self.pos])
        self.pos += 1
        return {'type': 'assign', 'var_name': var_name, 'value': value}

    def parse_print(self):
        self.pos += 1
        var_name = self.tokens[self.pos]
        self.pos += 1
        return {'type': 'print', 'var_name': var_name}

def parse_tokens(tokens):
    parser = Parser(tokens)
    return parser.parse()

def interpret_ast(ast):
    variables = {}
    for node in ast:
        if node['type'] == 'assign':
            variables[node['var_name']] = node['value']
        elif node['type'] == 'print':
            print(variables[node['var_name']])

class ScriptingLanguage:
    def __init__(self):
        pass

    def execute(self, code):
        tokens = tokenize_code(code)
        ast = parse_tokens(tokens)
        interpret_ast(ast)

language = ScriptingLanguage()

while True:
    code = input('>>> ')
    if code == 'exit':
        break
    try:
        language.execute(code)
    except Exception as e:
        print(f'Error: {e}')