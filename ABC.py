
def letras():
    for i in range(ord('a'), ord('m')+1):
        yield (chr(i))


if __name__ == '__main__':
    letra = letras()
    try:
        for i in range(ord('m')):
            print(next(letra))
            if i == 'm':
                break
    except Exception as e:
        print(e)

