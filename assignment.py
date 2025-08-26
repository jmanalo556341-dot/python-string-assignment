sentence = input("Enter sentence:  ")

while True:
    print('\nChoose an operation: ')
    print('1: Reverse the sentence')
    print('2: Count vowels')
    print('3: Check palindrome')
    print('4: Find and replace a word')
    print('5: Format (Title Case)')
    print('6: Split into words')
    print('7: Word frequency counter')
    print('8: Swap Case')
    print('9: Exit')

    choice = input('Enter your choice (1-9): ')

    if choice =="1":
      print('Reversed: ', sentence[::-1])

    elif choice =="2":
      vowels = "aeiouAEIOU"
      count = sum(1 for ch in sentence if ch in vowels)
      print('Vowel count: ', count)

    elif choice =="3":
         palindrome = sentence.replace(" ", "").lower()
         if palindrome == palindrome[::-1]:
              print('It is palindrome')
    else:
        print('It is not palindrome')

    if choice =="4":
      old = input("Enter a word to replace")
      new = input("Enter a new word ")
      updated = sentence.replace(old, new)
      print('Updated sentence is: ', updated)

    elif choice =="5":
      print("Title Case: ", sentence.title())    
  
    elif choice =="6":
      print("Splited: ", sentence.split())

    elif choice =="7":
      words = sentence.split()
      freq = {}
      for w in words:
        freq[w] = freq.get(w, 0) + 1
      print("Word frequencies:", freq)

    elif choice =="8":
      print('Swap case: ', sentence.swapcase())

    elif choice == "9":
      print("Goodbye!")
      break

    else:
      print("Invalid Choice! Try Again!")
    



