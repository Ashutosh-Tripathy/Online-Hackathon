for i in range(1,13):
    for j in range(1, 13):
        result = str(i*j)
        print(result + (3- len(result)) * ' ',  end = ' ')
    print()



