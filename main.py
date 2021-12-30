import os

def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
        #print(text)
        words = text.splitlines()
       # print(words)
    return words

def get_lines(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
    return text

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    # put your phone number into the string! 
    # if your number is (123)456-7890, the next line should look like this: phone_number = '1234567890'
    phone_number = '4797903472'
    words = get_lines('song.txt')
    for word in words:
        send_message(phone_number, word)