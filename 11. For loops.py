import time
# for loop =    Eine Anweisung, die ihren Codeblock für eine begrenzte Zeit ausführt

# Unterschied while loop und for loop:
    # while loop =  Unbegrenzt
    # for loop =    Begrenzt


for i in range(10):
    print(i+1)                  # +1, weil der Computer bei 0 anfängt zu zählen und hierdurch bei 9 aufhört


for i in range(50,100+1,2):     # 2 sind die steps (s. Slicing Strings mit [start:end:step])
    print(i)


for i in("Karoline Klein"):     # Ohne () geht auch
    print(i)


# Countdown coden:
for seconds in range(10,0,-1):
    print(seconds)              # print was i=index ist, hier seconds
    time.sleep(1)
print("0 - Happy New Year!")