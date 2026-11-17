def check_palindrome():
    user_input = input("Enter a word to check if it's a palindrome: ")
    
    # Convert everything to lowercase to ignore uppercase/lowercase differences
    cleaned_word = user_input.lower()
    
    # checkwhether the word is a palindrome
    reversed_word = cleaned_word[::-1]
    
    if cleaned_word == reversed_word:
        print(f"Yes! '{user_input}' is a palindrome.")
    else:
        print(f"No, '{user_input}' is not a palindrome.")
(check_palindrome())