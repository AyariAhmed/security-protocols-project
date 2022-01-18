import base64


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
