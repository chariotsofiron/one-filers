"""Evaluate literal math expressions without using eval."""
import ast
import operator as op
from ast import AST, Expression, expr
from typing import Any

binary_operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.BitAnd: op.and_,
    ast.BitOr: op.or_,
    ast.BitXor: op.xor,
    ast.LShift: op.lshift,
    ast.RShift: op.rshift,
}

unary_operators = {ast.UAdd: op.pos, ast.USub: op.neg, ast.Invert: op.inv}


def eval_(node: expr) -> Any:  # type: ignore[misc]
    """Eval ast nodes.

    :param node: The AST node to evaluate.
    :return: The result of the tree
    :raise TypeError: if we encounter an unsupported AST node
    """
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.BinOp):
        return binary_operators[type(node.op)](eval_(node.left), eval_(node.right))
    if isinstance(node, ast.UnaryOp):
        return unary_operators[type(node.op)](eval_(node.operand))  # type: ignore[operator]
    raise TypeError(node)


def eval_expr(expression: str) -> Any:  # type: ignore[misc]
    """Evaluates an arithmetic expression.

    Examples:
    >>> eval_expr("2+3")
    5
    >>> eval_expr("1 + 2*3**(4^5) / (6 + -7)")
    -5.0
    >>> eval_expr("2**6")
    64
    >>> eval_expr("2^6")
    4
    >>> eval_expr("0x3 & 0o6 | 0b100")
    6
    """
    result: AST = ast.parse(expression, mode="eval")
    assert isinstance(result, Expression)
    return eval_(result.body)
