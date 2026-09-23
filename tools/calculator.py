import ast
import operator

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

def calculate(node):
    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.BinOp):
        return OPS[type(node.op)](
            calculate(node.left),
            calculate(node.right)
        )

    if isinstance(node, ast.UnaryOp):
        return OPS[type(node.op)](
            calculate(node.operand)
        )

    raise ValueError("Invalid expression")

def calculator(expression):
    tree = ast.parse(expression, mode="eval")
    return calculate(tree.body)