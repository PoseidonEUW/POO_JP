import sys


class PasswordGuesser:
    def __init__(self, words, dates, options):
        self.words = words
        self.dates = dates
        self.options = options
        
        self.lowercase = False
        self.uppercase = False
        self.capitalize = False
        self.remove_accents = False
        self.l33t = False
        self.date_numbers = False
        self.date_words = False
        self.date_2_digits_year = False
        self.date_4_digits_year = False
        self.special_chars_common = False
        self.special_chars_all = False
        self.special_chars_max = None

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
            if option == "lowercase":
                self.lowercase = True
            elif option == "uppercase":
                self.uppercase = True
            elif option == "capitalize":
                self.capitalize = True
            elif option == "remove_accents":
                self.remove_accents = True
            elif option == "l33t":
                self.l33t = True
            elif option == "date_numbers":
                self.date_numbers = True
            elif option == "date_words":
                self.date_words = True
            elif option == "date_2_digits_year":
                self.date_2_digits_year = True
            elif option == "date_4_digits_year":
                self.date_4_digits_year = True
            elif option == "special_chars_common":
                self.special_chars_common = True
            elif option == "special_chars_all":
                self.special_chars_all = True
            elif option.startswith("special_chars_max_"):
                self.special_chars_max = int(option.split("_")[-1])
            else:
                print("Unknown option: %s" % option)
                sys.exit(1)



                    
