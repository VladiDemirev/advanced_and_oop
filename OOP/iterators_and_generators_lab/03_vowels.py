class vowels():
    def __init__(self, string):
        self.string = string
        vowel_letters = "aeiouy"
        self.string_vowels = [char for char in self.string if char.lower() in vowel_letters]
        self.current_index = 0
        self.end_index = len(self.string_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.end_index:
            raise StopIteration()
        index = self.current_index
        self.current_index += 1
        return self.string_vowels[index]


#   TEST CODE

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
