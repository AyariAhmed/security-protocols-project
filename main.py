from simple_term_menu import TerminalMenu
from cryptographic_tools.coding import Encoding
from cryptographic_tools.hashing import Hash
from cryptographic_tools.symmetric_encryption import Symmetric
from os import system




def clear():
    system('clear')


def main_menu():

    while True:
        clear()
        print('Which tool are you looking for?')
        m_choices = ['0- Encoding', '1- Hashing', '2- Symmetric encryption', '3- Asymmetric encryption',
                     '4- Authentication', '5- Quit']
        terminal = TerminalMenu(m_choices)
        entry = terminal.show()
        if entry == 0:
            Encoding.menu()
        elif entry == 1:
            Hash.menu()
        elif entry == 2:
            Symmetric.menu()
        elif entry == 3:
            pass
        elif entry == 4:
            pass
        else:
            break
    print('Until next time...')


if __name__ == '__main__':
    main_menu()
