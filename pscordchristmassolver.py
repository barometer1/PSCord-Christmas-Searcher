with open('names_file.txt', 'r') as fp:
    names = fp.readlines()

def partial(lst, query):
    return [s for s in lst if query in s]

print("Input partial name:")

substring = input()

print(partial(names, substring))
