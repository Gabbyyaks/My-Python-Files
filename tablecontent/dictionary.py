customer = {
    "Name": "Gabby Yaks",
    "Age": 20,
    "occupation": "Cybersecurity Expert"
}
print(customer.get("occupation"))

phone = input("Phone: ")
digits_mapping = {
     "0": "Zero",
     "1": "One",
     "2": "Two",
     "3": "Three",
     "4": "Four",
     "5": "Five",
     "6": "Six",
     "7": "Seven",
     "8": "Eight",
     "9": "Nine"
 }
output = ""
for ch in phone:
    output += digits_mapping.get(ch) + " "
# print(output)

# emoji
message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

# creating reusable functions

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))

