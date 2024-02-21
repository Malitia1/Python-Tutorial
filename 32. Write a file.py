
text = "Helloooo\nThis is some text\nHave a nice day!\n"

with open("testfür32.txt","w") as file:
    file.write(text)


# Wenn text oben geändert wird, wird Datei überschrieben.
# Um was zu ergänzen statt zu überschreiben:
text = "That's funny!"

with open("test.txt","a") as file:
    file.write(text)