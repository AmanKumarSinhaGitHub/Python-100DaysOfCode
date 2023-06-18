name = "Python-Code"
# Length of String
print(len(name)) 
# Output : 11


# Slice string from index 0 to index 5
print(name[0:6])    # (0:included, 6:excluded) 
# Output : Python
print(name[:6])     # You can skip writing 0
# Output : Python


fruit = "pineapple"
# Print "app"
print(fruit[4:7])
# Print "apple"
print(fruit[4:9]) 
print(fruit[4:]) # Slice from index 4 till the end
# Output : apple


# Negative Slicing
flower = "Lotus"
print(flower[:-3])
print(flower[0:-3]) 
print(flower[:len(flower)-3]) 
print(flower[0:len(flower)-3]) 
          # [0:5-3]
          # [0:2]
# Output for every print statement is : Lo

code = "HelloWorld"
print(code[-5 : -2]) # Output : Wor
# code[len(code)-5 : len(code-2)]
# code[10-5 : 10-2]
# code[5 : 8]
# include index 5 and exlude index 8
# Hello(Wor)ld
# 01234(567)89
#       Wor

alphabets = "ABCDE"
for i in alphabets:
    print(i)
# Print every character in new line