# nestes function calls = Ein Konzept, eine Funktion innerhalb einer anderen Funktion aufzurufen 


num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)


# Abgekürzter Code zu oben:
print(round(abs(float(input("Enter a whole positive number: ")))))