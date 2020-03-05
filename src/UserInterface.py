import Deck
import Menu

class UserInterface():
    def __init__(self):
        self.valid_card_input = False

    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False


    def __createDeck(self):
        """Command to create a new Deck"""
        # TODO: Get the user to specify the card size, max number, and number of cards

        valid_card_size = False
        while valid_card_size == False:
            card_size = input("Enter the size of the card: (3-15)")
            if card_size.isnumeric():
                if 3 <= int(card_size) <= 15:
                    valid_card_size = True
                    card_width = int(card_size)



        valid_max_num = False
        while valid_max_num == False:
            max_num = input("Enter maximum number on the Bingo card: (" + str((2 * card_width * card_width)) + ' - ' + str((4 * card_width * card_width)) + ')')
            if max_num.isnumeric():
                if int(max_num) >= 2 * card_width * card_width and int(max_num) <= 4 * card_width * card_width:
                    valid_max_num = True
                    max_number = int(max_num)


        valid_num_cards = False
        while valid_num_cards == False:
            num_cards = input("Enter the number of cards: (3 - 10,000)")
            if num_cards.isnumeric():
                if int(num_cards) >= 3 and int(num_cards) <= 10_000:
                    valid_num_cards = True
                    card_count = int(num_cards)

        # TODO: Create a new deck
        self.__m_currentDeck = Deck.Deck(card_width, card_count, max_number)
        # TODO: Display a deck menu and allow user to do things with the deck
        self.__deckMenu()


    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False

    def __getNumberInput(self, prompt, low, high):
        ask = input(prompt)
        while self.valid_card_input == False:
            if int(low) >= 1 and int(high) <= 10_000:
                self.valid_card_input = True
        return int(ask)

    def __getStringInput(self, param):
        string_input = input(param)
        return string_input

    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumberInput("Id of card to print", 1, self.__m_currentDeck.getCardCount())
        if cardToPrint > 0:
            print()
            self.__m_currentDeck.print(idx=cardToPrint)


    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name")
        if fileName != "":
            # TODO: open a file and pass to currentDeck.print()
            outputStream = open(fileName, 'w')
            self.__m_currentDeck.print(outputStream)
            outputStream.close()
            print("Done!")


