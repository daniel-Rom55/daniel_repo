inicioCicloExterior = int(input("dame el inico del ciclo exterior: "))
finCicloExterior = int(input("dame el fin del ciclo exterior: "))
inicioCicloInterior = int(input("dame el inico del ciclo interior: "))
finCicloInterior = int(input("dame el fin del ciclo interior: "))
i = inicioCicloExterior
while True:    #This simulates a Do Loop
    print("TABLA")
    j = inicioCicloInterior
    while True:    #This simulates a Do Loop
        print(str(i) + " x " + str(j) + " = " + str(i * j))
        j = j + 1
        if j > finCicloInterior: break
    i = i + 1
    if i > finCicloExterior: break #hola 
