import tests as test
# translates certain characters in strings to certain other characters
def main():
    def encode(st):
        code_dict = {'a':'1','e':'2','i':'3','o':'4','u':'5','5':'u','4':'o','3':'i','2':'e','1':'a'}
        x = []
        for char in st:
            if char in code_dict.keys():
                x.append(code_dict[char])
            else:
                x.append(char)
        return ''.join(x)

    def decode(st):
        return encode(st)


    #tests
    print(test.assert_equals(encode('hello'), 'h2ll4'))
    print(test.assert_equals(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?'))
    print(test.assert_equals(encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.'))
    print(test.assert_equals(decode('h2ll4'), 'hello'))
    return 0


if __name__ == "__main__":
    main()
