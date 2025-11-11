import random
import time

# List of fun messages
messages = [
    "You make me smile every day 😊",
    "I love our little adventures together 💖",
    "You're my favorite notification 💌",
    "Life is sweeter with you 🍫",
    "I can't stop thinking about you 💭❤️",
]

print("✨ Welcome to the Love Message Generator ✨")
time.sleep(1)
print("Generating a special message for you...\n")
time.sleep(2)

# Pick a random message
message = random.choice(messages)

print(f"💌 {message}\n")

# Ask if you want another one
while True:
    again = input("Do you want another message? (yes/no) ").lower()
    if again == "yes":
        print("\n💌 " + random.choice(messages) + "\n")
    else:
        print("\n❤️ Hope you liked it! ❤️")
        break