
def highest(filename):
    result = {}
    f = open(filename, 'r')
    for line in f:
        line = line[:-1]
        tokens = line.split(',')
        for i in range(1, len(tokens)):
            tokens[i] = int(tokens[i])
        if tokens[0] not in result:
            result[tokens[0]] = 0;
        if max(tokens[1:]) > result[tokens[0]]:
            result[tokens[0]] = max(tokens[1:])
    print(result)
        
highest('test.txt')