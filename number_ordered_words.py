import tests as t

def main():
    def order(sentence):
        word_list = sentence.split(" ")
        output = {}

        for word in word_list:
            for letter in word:
                if letter.isdigit():
                    output[int(letter)] = word
        x = ""
        for i in sorted(output):
            x= x + output.get(i) + " "
        x = x.strip()
        return x


    print(order("asd3 basd1 gasd2"))
    return None

if __name__ == "__main__":
    main()
