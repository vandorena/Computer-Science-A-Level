def tower_builder(n_floors):
    # build here
    d = 2
    n1 = n_floors - 1
    a = 1
    array = ["*"]
    try:
        for i in range(n_floors):
            spaces = ' ' * (n_floors - i - 1)
            stars = "*" * (i*2 + 1)
            array.append(spaces + stars + spaces)
        return array
    
    except BaseException:
        array = ["*"]
        return array