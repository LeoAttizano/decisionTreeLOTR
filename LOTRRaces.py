from os import system
from sklearn import tree

Red='\033[31m'          # Red
Green='\033[32m'        # Green
Yellow='\033[33m'       # Yellow
Blue='\033[34m'         # Blue
Purple='\033[35m'       # Purple
Cyan='\033[36m'         # Cyan
White='\033[37m'        # White


def banner():
    system('clear')
    text = f'''{Green}LOTR Race Detector{White}\n'''
    print(text)

def lotrClassifier():
    X= [
        #Dwarf dataset
        [122,50,35],
        [135,65,40],
        [140,78,47],
        [152,60,44],
        [127,45,39],
        [136,66,40],
        [155,90,39],
        [120,82,35],
        [145,88,38],
        [140,94,38],
        #Hobbit dataset
        [90,40,40],
        [100,45,42],
        [80,55,45],
        [88,69,42],
        [110,70,44],
        [85,46,39],
        [88,55,40],
        [98,75,43],
        [120,70,47],
        [125,68,48],
        #Orc dataset
        [150,80,40],
        [166,85,40],
        [165,70,44],
        [145,77,37],
        [170,100,45],
        [156,68,38],
        [166,80,39],
        [171,90,43],
        [167,77,39],
        [149,85,38],
        #Human dataset
        [181,70,44],
        [171,65,40],
        [180,90,42],
        [188,85,40],
        [176,65,38],
        [180,65,40],
        [190,80,42],
        [188,75,41],
        [175,60,40],
        [187,73,38],
        #Elf dataset
        [181,40,38],
        [188,53,37],
        [175,48,36],
        [190,60,35],
        [200,70,39],
        [183,49,37],
        [180,54,36],
        [170,45,30],
        [195,68,39],
        [173,60,37]
    ]

    #Tie the datasets to a specific race
    Y = [
        'Dwarf',
        'Dwarf',
        'Dwarf',
        'Dwarf',
        'Dwarf',
        'Dwarf',
        'Dwarf',
        'Dwarf',
        'Dwarf',
        'Dwarf',
        'Hobbit',
        'Hobbit',
        'Hobbit',
        'Hobbit',
        'Hobbit',
        'Hobbit',
        'Hobbit',
        'Hobbit',
        'Hobbit',
        'Hobbit',
        'Orc',
        'Orc',
        'Orc',
        'Orc',
        'Orc',
        'Orc',
        'Orc',
        'Orc',
        'Orc',
        'Orc',
        'Human',
        'Human',
        'Human',
        'Human',
        'Human',
        'Human',
        'Human',
        'Human',
        'Human',
        'Human',
        'Elf',
        'Elf',
        'Elf',
        'Elf',
        'Elf',
        'Elf',
        'Elf',
        'Elf',
        'Elf',
        'Elf'
    ]

    clf = tree.DecisionTreeClassifier()
    #train the decision tree
    clf = clf.fit(X,Y)

    #Ask for inputs
    print('In Centimeters')
    print('Height: ')
    height = int(input())
    print('In KG')
    print('Weight: ')
    weight = int(input())
    print('Brazil size unit')
    print('Shoe Size: ')
    shoeSize = int(input())

    #call prediction based on input
    prediction = clf.predict ([[height,weight,shoeSize]])

    #return to the user its Race based on the info supplied
    print (prediction)


def availableRaces():
    
    print('Available Races: ')
    print(f'\n{Cyan}Hobbits')
    print(f'{Yellow}Dwarves')
    print(f'{Purple}Orcs')
    print(f'{Blue}Humans')
    print(f'{Green}Elves\n')
    core()


def core():
    while True:
        print(f'{Green}[*] Actions:')
        print(f'{Green}[1] Open Classifier')
        print(f'{Green}[2] Show Races Available')
        print(f'{Green}[Ctrl+C] - Exit')

        choice = input(f'{Red}[>] {White}')

        if choice == '1':
            lotrClassifier()
        elif choice == '2':
            availableRaces()
        else:
            print(f'{Red}[-]Invalid Choice{White}\n')
            core()

if __name__ == '__main__':
    try:
        banner()
        core()
    except KeyboardInterrupt:
        print('\nGood Bye!\n')