def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

uneseno = input("Unesite string: ")

print(reverse_string(uneseno))