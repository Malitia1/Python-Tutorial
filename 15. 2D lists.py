# 2D lists = Eine Liste aus Listen

drinks = ["Coffee","Soda","Tea"]            # 0 / 0, 1, 2
dinner = ["Pizza","Hamburger","Hotdog"]     # 1 / 0, 1, 2
dessert = ["Cake","Ice Cream"]              # 2 / 0, 1, 2

food = [drinks, dinner, dessert]

print(food[0][1])                           # Erstes [] gibt an, welche Liste wir brauchen, zweites [] gibt an, welches Element wir genau aus erstem [] wollen
