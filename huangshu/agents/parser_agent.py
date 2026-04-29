import ast

class ParserAgent:
    def analyze_file(self, code):
        tree = ast.parse(code)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        return {
            "functions": functions,
            "lines": len(code.splitlines())
        }
