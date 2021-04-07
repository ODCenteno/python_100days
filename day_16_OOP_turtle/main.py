from turtle import Turtle, Screen
from prettytable import PrettyTable

# danny = Turtle()
# danny.shape("turtle")
# danny.color("DarkOliveGreen3")
# danny.forward(100)
# danny.left(90)
# danny.forward(100)

# my_screen = Screen()
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemones", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "c"
print(table)
