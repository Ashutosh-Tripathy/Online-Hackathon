# You can use binary search for better performance
while True:
    uinput = input()
    if not (uinput):
        continue
    N, B = map(int, uinput.split())
    if N == -1:
        break
    population = [int(input()) for x in range(N)]
    population.sort(reverse=True)
    index, counter = 1, {x:1 for x in range(N)}
    B -= N
    #print(population)
    while B > 0:
        exit = False
        for i in range(N):
            #print('-------------------')
            calci, calc0 = population[i]/counter[i], population[0]/counter[0]
            #print(calci, calc0)
            if B == 0:
                print(int(max(calci, calc0)))
                exit = True
            else:
                B -= 1
                if calci >= calc0 :
                    counter[i] += 1
                else:
                    counter[0] += 1
                    exit = True
            #print(counter) 
            if exit:
                break
    
    
    
    
    
    
    
