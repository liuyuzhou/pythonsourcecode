path = './test.txt'
with open(path, 'w') as f:
    print(f"write length:{f.write('Hello world!')}")
