from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['#', 'Pokemon Name', 'Type']
table.add_row(["001", "Bulbasaur", "Grass/posion"])
table.add_row(["002", "Ivysaur", "Grass/posion"])
table.add_row(["003", "Venusaur", "Grass/posion"])
table.add_row(["004", "Charmander", "Fire"])
table.add_row(["005", "Charmeleom", "Fire"])
table.add_row(["006", "Charizard", "Fire/Flying"])
table.add_row(["007", "Squirtle", "Water"])
table.add_row(["008", "Wartortle", "Water"])
table.add_row(["009", "Blastoise", "Water"])
table.add_row(["010", "Caterpie", "Bug"])
table.align = "r"

print(table)
