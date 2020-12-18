'''
Caesar Cipher or shift cipher encryption technique.
The rotation of letters will be determined by the encryption 'key'.
example: word = "hello" 
         key = 5 (rotating forward)
         caesar_cipher output: "mjqqt"
'''

# cipher object
class CaesarCipher():
    def __init__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.translated_message = ''
    # encryption needs a message and a key, default to 0
    def encrypt(self, message, key=0):
        self.translated_message = ""
        self.key = key
        self.message = message
        return self.__cryption('encrypt')
    # encryption needs a message and a key, default to 0
    def decrypt(self, message, key=0):
        self.translated_message = ""
        self.key = key
        self.message = message
        return self.__cryption('decrypt')
    #main function to encrypt or decrypt message with type switch    
    def __cryption(self, type):
        # loop through each letter in the message
        for letter in self.message:
             # if there is a character not in the eltters string add to new string
            if letter not in self.letters:
                self.translated_message += letter
                continue
            # if the letter is in the list of letters then assign the place of letter in string of letters
            if letter in self.letters:
                n = self.letters.find(letter)
                if type == 'encrypt':
                    n = n + self.key
                elif type == 'decrypt':
                    n = n - self.key
               
                # if the number is larger than the length of the letters, subtract by len(letters) to get difference    
                if n >= len(self.letters):
                    n = n - len(self.letters)
                # if number less than 0 then add to get difference 
                elif n < 0:
                    n = n + len(self.letters)
                # append letters to translated message
                self.translated_message += self.letters[n]
        # return the message
        print(self.translated_message)
# initialize
if __name__ == '__main__':
    cipher = CaesarCipher()
    cipher.encrypt(message='This is a very secret message.', key=13)
    cipher.decrypt(message='qbag gryy nalbar', key=13)
