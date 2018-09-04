
n = int(input("Enter the length of the sequence: ")) 

listi = [1,2,3]
teljari1 = 0
teljari2 = 1
teljari3 = 2

for x in range(n):
    number1 = listi[teljari1]
    number2 = listi[teljari2]
    number3 = listi[teljari3]

    seq = number1 + number2 + number3
    
    
    teljari1 += 1
    teljari2 += 1
    teljari3 += 1
    
    listi.append(seq)

    print (number1)
    
    #Create variables to store
    #append list for each run case
    #add to variables in each run