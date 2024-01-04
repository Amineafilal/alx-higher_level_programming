!  # /usr/bin/python3


def magic_calculation(a, b):
    """"the same as the following Python bytecode"""
    import magic_calculation_102 as magical

    if a < b:
        c = magical.add(a, b)
        for i in range(4, 6):
            c = magical.add(c, i)
        return (c)
    else:
        return (sub(a, b))
