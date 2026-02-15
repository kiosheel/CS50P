def main():
    emote = input("Entrez un phrase avec une emorte triste ou joyeuse à la fin: ")
    print(convert(emote))

   
def convert(new):
    return new.replace(":)","🙂").replace(":(", "🙁")


main()