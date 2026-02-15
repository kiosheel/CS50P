def main():
    word = input("Greeting: ").replace(",","").strip()
    word2 = word.split()
    if word.startswith("H") and word2[0] != "Hello":
        print("$20")
    elif word.startswith("Hello"):
        print("$0")
    else:
        print("$100")


main()
    