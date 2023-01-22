def construct_function(mapping: dict[int, int]) -> str:
    """Construct a mathematical expression for an injective function represented as a
    dictionary.

    Example:
        >>> construct_function({0: 0, 1: 2, -1: 1})
        1/2n(3n+1)

    :param mapping: A dictionary representing an injective function
    :returns: An unsimplified polynomial expression
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
