import tests as test
import re

# Description:
# The word i18n is a common abbreviation of internationalization in the developer community, used instead of typing the whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.
# 
# Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:
# 
# A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
# The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").

def main():
    def abbreviate(s):

        words = re.findall('[a-zA-Z]+|\W+|[0-9]|[_]',s)
        x = []
        for word in words:
            if len(word) < 4:
                x.append(word)
            else:
                x.append('{}{}{}'.format(word[0], len(word[1:-1]), word[-1]))

        return ''.join(x)


    print(test.assert_equals(abbreviate("internationalization"), "i18n"))
    print(test.assert_equals(abbreviate("accessibility"), "a11y"))
    print(test.assert_equals(abbreviate("Accessibility"), "A11y"))
    print(test.assert_equals(abbreviate("elephant-ride"), "e6t-r2e"))
    print(test.assert_equals(abbreviate("a balloon monolithic_monolithic_on. sits-mat;"), "a b5n m8c_m8c_on. s2s-mat;"))
    return 0


if __name__ == "__main__":
    main()
