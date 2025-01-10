def baholar(*talabalar):
    baho = {}
    for i in talabalar:
        baho.update({i:int(input(f"{i} ning baxosi"))})
    return baho
