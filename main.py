#This program is used to generate a name for your band.

def main():
    print("Welcome to the Band Name Generator.")
    city = input("Which city did you grow up in? \n")
    pet = input("What's the name of your favorite pet? \n")
    print(f'Your band name could be: "{city} {pet}!" \n')


if __name__ == '__main__':
    main()
