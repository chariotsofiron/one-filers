def construct_function(mapping: dict[int, int]) -> str:
    """Constructs an unsimplified polynomial expression for a dictionary
    representing an injective function.

    Example:
    >>> construct_function({0: 0, 1: 2, -1: 1})
    '(x-1)(x--1)(0/-1)+(x-0)(x--1)(2/2)+(x-0)(x-1)(1/2)'

    ...which simplifies to 1/2n(3n+1)
    """
    terms = []
    for i, j in mapping.items():
        coeff = 1
        term = ""
        for k in mapping:
            if i != k:
                coeff *= i - k
                term += f"(x-{k})"
        term += f"({j}/{coeff})"
        terms.append(term)
    return "+".join(terms)
