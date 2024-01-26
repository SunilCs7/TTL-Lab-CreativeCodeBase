# Get user input for the word
word2954 = input("Enter a word: ")

# Check if the word is magic
is_magic2954 = all(
    (word2954[i] < word2954[-i - 1]) if i % 2 == 0 else (word2954[i] > word2954[-i - 1])
    for i in range(len(word2954) // 2)
)

if is_magic2954:
    print("The word is a magic word2954.")
else:
    print("The word is not a magic word2954.")
