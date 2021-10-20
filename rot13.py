import tests as t

def main():
    def rot13(message):
        letters = [i for i in message]
        ascii_low = [chr(i) for i in range(97,123)]
        ascii_high = [chr(i) for i in range(65,91)]

        cipher = []
        for i in letters:
            if i in ascii_low or i in ascii_high:
                if i.islower():
                    x = ascii_low.index(i) + 13
                    if x >= len(ascii_low) - 1:
                        x = x - len(ascii_low)
                    cipher.append(ascii_low[x])
                else:
                    x = ascii_high.index(i) + 13
                    if x >= len(ascii_high) - 1:
                        x = x - len(ascii_high)
                    cipher.append(ascii_high[x])
            else:
                cipher.append(i)

        return "".join(cipher)

    print(t.assert_equals(rot13("test test"), "grfg grfg"))
    print(t.assert_equals(rot13("Test"),"Grfg"))

if __name__ == "__main__":
    main()
