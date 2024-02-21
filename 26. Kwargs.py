# **kwargs = Parameter, der es einer Funktion ermöglicht, eine variable Anzahl von schlüsselwortbasierten Argumenten entgegenzunehmen und sie als Wörterbuch (Dictionary) zu behandeln

#               *args =     Position Arguments
#               **kwargs =  Keyword Arguments


def hello(**kwargs):        # Name irreveant, wichtig ist **
    print("Hello "+kwargs["title"]+" "+kwargs["first"]+" "+kwargs["middle"]+" "+kwargs["last"])

# Alternativer Code:
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")


hello(title="Mr.",first="Bob",middle="Bobby",last="Schulz")