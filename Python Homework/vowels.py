vowels=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
word="Shabingus"
count=0

for i in range(len(word)):
    if word[i] in vowels:
        count +=1
print(count)