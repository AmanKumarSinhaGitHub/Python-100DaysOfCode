name = "Aman"
college = "R.N. College"

sentence = "My name is {} and My college name is {}"

print(sentence.format(name, college)) 
# My name is Aman and My college name is R.N. College


# f-string
print(f"My name is {name} and My college name is {college}")
# My name is Aman and My college name is R.N. College


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.8769))
# For only 49.88 dollars!

price = 49.8769
text = f"For only {price:.2f} dollars!"
print(text)
# # For only 49.88 dollars!