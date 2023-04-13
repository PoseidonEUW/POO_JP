from passwordGuesser import PasswordGuesser

# Create an instance of the PasswordGuesser class
guesser = PasswordGuesser(words=['password', 'secret'], dates=['01011980', '12311999'], options={
    'lowercase': True,
    'uppercase': True,
    'use_numbers': True,
    'use_special_chars': True,
    'special_chars': '!@#$%^&*()_+-=[]{}|;:,.<>?'
})

# Set some additional options
guesser.set_max_special_chars(2)
guesser.set_language('en')

# Generate a list of passwords and print them
passwords = guesser.generate_passwords()
print(passwords)

# Generate a JSON string of passwords and print it
json_passwords = guesser.generate_passwords_json()
print(json_passwords)
