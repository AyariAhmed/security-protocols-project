import base64

from simple_term_menu import TerminalMenu


class Encoding:
    """"Allows the encoding and decoding of a message based on the specified method """

    @staticmethod
    def encode(message: str, method: str):
        if method in ['utf8', 'ascii']:
            encoded_text = str.encode(message, encoding=method)
            print(f'Encoded message: {encoded_text}')
            return encoded_text

        elif method == 'base64':
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print(f'Encoded message: {base64_message}')
            return base64_message

        elif method == 'base32':
            message_bytes = message.encode('ascii')
            base32_bytes = base64.b32encode(message_bytes)
            base32_message = base32_bytes.decode('ascii')
            print(f'Encoded message: {base32_message}')
            return base32_message

        elif method == 'base16':
            message_bytes = message.encode('ascii')
            base16_bytes = base64.b16encode(message_bytes)
            base16_message = base16_bytes.decode('ascii')
            print(f'Encoded message: {base16_message}')
            return base16_message

        else:
            print("Provided encoding method is not supported!")

    @staticmethod
    def decode(encoded_message: str, method: str):
        if method in ['utf8', 'ascii']:
            message = encoded_message.decode(encoding=method)
            print(f"Decoded message: {message}")
            return message

        elif method == 'base64':
            message_bytes = encoded_message.encode('ascii')
            base64_bytes = base64.b64decode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print('your decoded text is : ' + base64_message)
            return base64_message

        elif method == 'base32':
            message_bytes = encoded_message.encode('ascii')
            base32_bytes = base64.b32decode(message_bytes)
            base32_message = base32_bytes.decode('ascii')
            print(f"Decoded message: {base32_message}")
            return base32_message

        elif method == 'base16':
            message_bytes = encoded_message.encode('ascii')
            base16_bytes = base64.b16decode(message_bytes)
            base16_message = base16_bytes.decode('ascii')
            print(f"Decoded message: {base16_message}")
            return base16_message

        else:
            print("Provided decoding method is not supported!")

    @staticmethod
    def menu():
        while True:
            print("====> Encoding")
            m_choices = ['Encode a message', 'Decode a message', 'Go back']
            terminal = TerminalMenu(m_choices)
            entry = terminal.show()
            if entry == 0:
                while True:
                    message = None
                    while message is None:
                        message = str(input("-Message to encode: "))
                    print("---choose the encoding method---")
                    choices = ['0- utf-8', '1- ascii', '2- base64', '3- base32', '4- base16', '5 - Go back']
                    terminal = TerminalMenu(choices)
                    menu_entry_index = terminal.show()
                    encoded = None
                    if menu_entry_index == 0:
                        encoded = Encoding.encode(message, 'utf8')
                    elif menu_entry_index == 1:
                        encoded = Encoding.encode(message, 'ascii')
                    elif menu_entry_index == 2:
                        encoded = Encoding.encode(message, 'base64')
                    elif menu_entry_index == 3:
                        encoded = Encoding.encode(message, 'base32')
                    elif menu_entry_index == 4:
                        encoded = Encoding.encode(message, 'base16')
                    else:
                        break

                    print('Decode the encoded message ?')
                    yn_choices = ['Yes', 'No']
                    terminal = TerminalMenu(yn_choices)
                    resp = terminal.show()
                    if resp == 1:
                        print('No')
                        break
                    if menu_entry_index == 0:
                        Encoding.decode(encoded, 'utf8')
                    elif menu_entry_index == 1:
                        Encoding.decode(encoded, 'ascii')
                    elif menu_entry_index == 2:
                        Encoding.decode(encoded, 'base64')
                    elif menu_entry_index == 3:
                        Encoding.decode(encoded, 'base32')
                    elif menu_entry_index == 4:
                        Encoding.decode(encoded, 'base16')

                    print('\t------------------------')
                    break
            elif entry == 1:
                encoded = None
                while encoded is None:
                    encoded = str(input("-Encoded Message: "))
                print("---choose the encoding method---")
                choices = ['0- utf-8', '1- ascii', '2- base64', '3- base32', '4- base16', '5 - Go back']
                terminal = TerminalMenu(choices)
                menu_entry_index = terminal.show()
                if menu_entry_index == 0:
                    Encoding.decode(encoded, 'utf8')
                elif menu_entry_index == 1:
                    Encoding.decode(encoded, 'ascii')
                elif menu_entry_index == 2:
                    Encoding.decode(encoded, 'base64')
                elif menu_entry_index == 3:
                    Encoding.decode(encoded, 'base32')
                elif menu_entry_index == 4:
                    Encoding.decode(encoded, 'base16')
                else:
                    break
            else:
                break
