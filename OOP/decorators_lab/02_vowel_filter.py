def vowel_filter(function):
    def wrapper():
        result = function()
        vowels = [l for l in result if l.lower() in "aeiouy"]
        return vowels

    #   return [l for l in function() if l in "aeiouy"]
    return wrapper


#  Test Code

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
