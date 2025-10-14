# def inkop():
#     a = "lök"
#     b = "mjölk"

# x = 1
# y = 2
# z = x+y

# När vi inte använder range, så loopar vi 
# igenom alla elementen i listan
# Vi skapar alltså separata variabler för varje element
# i listan, i vårt fall, först bob sen woff sen sten
hundar = ["bob","woff", "sten"]
for hund in hundar:
    hund = hund + " är en hund"
    print(hund)

# Hur kan vi ändra loopen om  vi vill kunna använda flera
# hästar i samma loop?
# hästar = ["lars","stina", "torkel"]
# # # Vi skapar en loop igen, 
# # # range(len(hästar)) => range(3) => [0,1,2]
# grann_lista = []
# for i in range(len(hästar)-1):
#     grannar = hästar[i] + " är granne med, till höger: " + hästar[i+1]
#     print(grannar)
#     ny_häst = input("Vad heter den nya hästen?: ")
#     hästar.append(ny_häst)
#     print(hästar)
#     grann_lista.append(grannar)
#     print("Grannlista: ", grann_lista)

# """ Om vi vill lägga till ett värde till en lista, 
#     hur gör vi då? """

# nbr_list = [7, 3, 25, 543]
# nbr_list.append(2)
# print("Den nya listan är: ", nbr_list)


# Med range så skapar vi en ny lista som är lika
# lång som vi anger i range, i vårt fall 3 => [0,1,2]
# for _ in range(3): 
#     print("Hello")

# x = [0,1,2]
# for i in range(3):
#     print("Hello")
#     print(i)

# konradIsAtHome = 0

# while konradIsAtHome < 6:
#     print("Värdet av konradIsAtHome är nu: ", konradIsAtHome)
#     if konradIsAtHome < 3:
#         print("Konrad inte hemma, släcker lamporna")
#     elif konradIsAtHome >= 3 and konradIsAtHome < 5:
#         print("Konrad på väg hem, rosta bröd")
#         #checkerfunction(), output som är ett state för konradIsAtHome (True/False) 
#     else:
#         print("Konrad är hemma, tänd glöggen, basta tofflorna")
#     konradIsAtHome += int(input("Hur fort rör sig Konrad hemåt [1-10]?"))
#     # x += 1 innebär samma som, x = x + 1


#x = 0
"""

x = int(input("Sätt ett första värde (<70): "))

while x < 70:
    print("Värdet av x är nu: ", x)
    if x < 3: 
        print("x mindre än 3 (0,1 eller 2)")
    elif x >= 3 and x < 5:
        print("x är mellan 3 och mindre än 5, (3 eller 4)")
    elif x%7 == 0 or x%5 == 0:
        print("Delbart med sju eller delbart med 5")
        print("Värdet är: ", x)
    else: 
        print("Alla andra värden, i vårt fall massa värden mellan 0 och 70")
        print("Värdet är: ", x)

    if x%3 == 0:
        print("Delbart med 3")
    if x%2 == 0:
        print("Jämnt tal")

    x = int(input("Valfritt tal för nästa loop: "))
"""

    # x += 1 innebär samma som, x = x + 1
    # x += 2, samma som x = x + 2 
    # x += (-1), samma som x = x + (-1) = x - 1


x = 0
while x < 15:
    print("x är nu: ", x)
    if x % 2 == 0:
        x -= 1
    else:
        x += 3
