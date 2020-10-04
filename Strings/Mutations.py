def mutate_string(string, position, character):
    a = position
    k = character
    return string[:a] + k + string[a+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
