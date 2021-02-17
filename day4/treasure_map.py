
rowA = [ "0", "1" , "2", "3"]
row1 = ["1", "⬜️","⬜️","⬜️"]
row2 = ["2", "⬜️","⬜️","⬜️"]
row3 = ["3", "⬜️","⬜️","⬜️"]

map = [rowA, row1, row2, row3]
print(f"{rowA}\n{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\nChoose the column and row number: ").strip()
position.replace(' ', '')

# First Atempt to get this excercise:
# if position[1] == "1":
#     map[1][int(position[0])] = 'X'
# elif position[1] == "2":s
#     map[2][int(position[0])] = 'X'
# elif position[1] == "3":
#     map[3][int(position[0])] = 'X'
# print(f"{rowA}\n{row1}\n{row2}\n{row3}")

# An easy way to do it.
map[int(position[1])][int(position[0])] = 'X'
print(f"{rowA}\n{row1}\n{row2}\n{row3}")