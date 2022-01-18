from simple_term_menu import TerminalMenu
from cryptographic_tools.coding import Encoding
from cryptographic_tools.hashing import Hash


def main_menu():
    while True:
        m_choices = ['0- Encoding', '1- Hashing', '2- Quit']
        terminal = TerminalMenu(m_choices)
        entry = terminal.show()
        if entry == 0:
            Encoding.menu()
        elif entry == 1:
            Hash.menu()
        else:
            break
    print('Until next time...')


if __name__ == '__main__':
    main_menu()


