from simple_term_menu import TerminalMenu
from cryptographic_tools.coding import Encoding
from cryptographic_tools.hashing import Hash
from os import system


def clear():
    system('clear')


def main_menu():
    while True:
        m_choices = ['0- Encoding', '1- Hashing', '2- Symmetric encryption', '3- Asymmetric encryption',
                     '4- Authentication', '5- Quit']
        terminal = TerminalMenu(m_choices)
        entry = terminal.show()
        if entry == 0:
            Encoding.menu()
            clear()
        elif entry == 1:
            Hash.menu()
            clear()
        elif entry == 2:
            pass
            clear()
        elif entry == 3:
            pass
            clear()
        elif entry == 4:
            pass
            clear()
        else:
            break
    print('Until next time...')


if __name__ == '__main__':
    main_menu()
