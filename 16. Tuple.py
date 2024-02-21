# tuple =   Uveränderlichete, geordnete Sequenz von Elementen 
#           Änlich wie Listen, können nur hier nicht verändert werden nach Erstellung. 
#           Werden oft verwendet, um Daten zu gruppieren und weiterzugeben


student = ("Bro",21,"male")

print(student.count("Bro"))         # zählt, wie oft "Bro" vorkommt
print(student.index("male"))        # gibt an, wo sich "male" befindet (2)

for x in student:
    print(x)                        # x gibt alle Elemente an

if "Bro" in student:
    print ("Bro is here")