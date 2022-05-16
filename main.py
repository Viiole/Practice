import csv

cryptoData = []


with open('currencies22.csv', 'r') as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        cryptoData.append(row)


size = len(cryptoData)


def getCryptoData(size, nameCoin):
    name = ""
    price = ""
    market_cap = ""

    for i in range(size):
        if nameCoin == cryptoData[i][0]:
            name = cryptoData[i][0]
            price = cryptoData[i][1]
            market_cap = cryptoData[i][2]

    if name == "":
        print("Cryptocurrency %s not found" % nameCoin)
    else:
        print("name %s:\nprice %s, market_cap %s" % (name, price, market_cap))


while 1:
    print("1 - database search")
    print("2 - Exit")
    a = int(input())

    if a == 1:
        nameCoin = input("Enter the name of the cryptocurrency:\n")

        getCryptoData(size, nameCoin)
    elif a == 2:
        break


