import itertools
import sys
import json

# PasswordGuesser
class PasswordGuesser:
    def __init__(self, words, dates, options):
        self.words = words
        self.dates = dates
        self.options = options
        self.passwords = []

    def set_lowercase(self, value):
        self.lowercase = value
        
    def set_uppercase(self, value):
        self.uppercase = value
        
    def set_capitalize(self, value):
        self.capitalize = value
        
    def set_remove_accents(self, value):
        self.remove_accents = value
        
    def set_l33t(self, value):
        self.l33t = value
        
    def set_date_as_numbers(self, value):
        self.date_as_numbers = value
        
    def set_date_as_words(self, value):
        self.date_as_words = value
        
    def set_two_digit_year(self, value):
        self.two_digit_year = value
        
    def set_four_digit_year(self, value):
        self.four_digit_year = value
        
    def set_language(self, value):
        self.language = value
        
    def set_common_special_chars(self, value):
        self.common_special_chars = value
        
    def set_all_special_chars(self, value):
        self.all_special_chars = value
        
    def set_max_special_chars(self, value):
        self.max_special_chars = value
        
    def get_options(self):
        return {
            'lowercase': self.lowercase,
            'uppercase': self.uppercase,
            'capitalize': self.capitalize,
            'remove_accents': self.remove_accents,
            'l33t': self.l33t,
            'date_as_numbers': self.date_as_numbers,
            'date_as_words': self.date_as_words,
            'two_digit_year': self.two_digit_year,
            'four_digit_year': self.four_digit_year,
            'language': self.language,
            'common_special_chars': self.common_special_chars,
            'all_special_chars': self.all_special_chars,
            'max_special_chars': self.max_special_chars
        }

    def set_options(self, options):
        for option in options:
            if option == 'lowercase':
                self.lowercase = True
            elif option == 'uppercase':
                self.uppercase = True
            elif option == 'capitalize':
                self.capitalize = True
            elif option == 'remove_accents':
                self.remove_accents = True
            elif option == 'l33t':
                self.l33t = True
            elif option == 'date_numbers':
                self.date_numbers = True
            elif option == 'date_words':
                self.date_words = True
            elif option == 'date_2_digits_year':
                self.date_2_digits_year = True
            elif option == 'date_4_digits_year':
                self.date_4_digits_year = True
            elif option == 'special_chars_common':
                self.special_chars_common = True
            elif option == 'special_chars_all':
                self.special_chars_all = True
            elif option.startswith('special_chars_max_'):
                self.special_chars_max = int(option.split('_')[-1])
            else:
                print("Unknown option: %s" % option)
                sys.exit(1)



                    

    def generate_passwords(self):
        word_options = []
        if self.options['lowercase']:
            word_options.append('lower')
        if self.options['uppercase']:
            word_options.append('upper')
        if self.options['capitalize']:
            word_options.append('capitalize')
        if self.options['remove_accents']:
            word_options.append('remove_accents')
        if self.options['leet']:
            word_options.append('leet')

        word_combinations = self.get_combinations(self.words, word_options)

        date_options = []
        if self.options['use_numbers']:
            date_options.append('use_numbers')
        if self.options['use_month_names']:
            date_options.append('use_month_names')
        if self.options['two_digit_year']:
            date_options.append('two_digit_year')
        if self.options['four_digit_year']:
            date_options.append('four_digit_year')

        date_combinations = self.get_combinations(self.dates, date_options)

        special_character_options = []
        if self.options['common_special_characters']:
            special_character_options.append('common')
        if self.options['all_special_characters']:
            special_character_options.append('all')

        special_character_combinations = self.get_combinations(
            self.options['special_characters'], special_character_options)

        all_combinations = itertools.product(
            word_combinations, date_combinations, special_character_combinations)

        for combination in all_combinations:
            password = ''.join(combination)
            if self.options['max_length'] is not None and len(password) > self.options['max_length']:
                continue
            self.passwords.append(password)

        def generate_passwords_json(self):
            self.generate_passwords()
            json_passwords = json.dumps(self.passwords)
            return json_passwords

        def get_combinations(self, data, options):
            combinations = []
            for option in options:
                if option == 'lower':
                    data = [word.lower() for word in data]
                elif option == 'upper':
                    data = [word.upper() for word in data]
                elif option == 'capitalize':
                    data = [word.capitalize() for word in data]
                elif option == 'remove_accents':
                    data = [self.remove_accents(word) for word in data]
                elif option == 'leet':
                    data = self.generate_leet(data)
                
            combinations = []
            for i in range(1, len(data) + 1):
                for combination in itertools.combinations(data, i):
                    combinations.append(''.join(combination))
            
            return combinations
        
        def remove_accents(self, word):
            return word.replace('é', 'e').replace('è', 'e').replace('ê', 'e')
        
        def generate_leet(self, data):
            leet_characters = {
                'a': '4',
                'e': '3',
                'i': '1',
                'o': '0',
                'l': '1',
                's': '5',
                'b': '8',
                't': '7',
                'z': '2',
                'g': '6'
            }
            leet_combinations = []
            for word in data:
                for c in range(1, len(word) + 1):
                    for subset in itertools.combinations(range(len(word)), c):
                        new_word = list(word)
                        for i in subset:
                            if new_word[i].lower() in leet_characters:
                                new_word[i] = leet_characters[new_word[i].lower()]
                        leet_combinations.append(''.join(new_word))
            return leet_combinations
        
