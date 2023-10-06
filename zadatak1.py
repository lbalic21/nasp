def reverse_sort(names :list) -> list:
    reverse_names = sorted(names)
    reverse_names.reverse()
    return reverse_names


names = ["Ana", "Petar", "Ana", "Lucija", "Vanja", "Pavao", "Lucija"]
names_desc = reverse_sort(names)
selected_names = names_desc[:-1]
unique_selected_names = set(selected_names)

pass_names = []
for item in unique_selected_names :
    item += "- pass"
    pass_names.append(item)




print(names)
print(names_desc)
print(selected_names)
print(unique_selected_names)
print(pass_names)

