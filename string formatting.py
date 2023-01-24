# old method of string formatting

letter = "Hay my name is {} and I am from {}"
name = "Ravi Tiwari"
state = "Biahr"
print(letter.format(name, state))

# New method of string formatting
print(f"\nHay my name is {name} and I am from {state}")

price = 50.3508922222222222222222
print(f"Price of Iphone in USA ${price:.3f}")

txt = "this curly brakets '{}' by using f-string"
print(f"\nYou can write Python code in {txt} ")
