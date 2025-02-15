phrase = "Today is a great day"
new_phrase = phrase.upper()
print(new_phrase)  # Output: "TODAY IS A GREAT DAY"

tweet = "I CAN'T WAIT FOR THE WEEKEND!!!"
print(tweet.lower())  # Output: "i can't wait for the weekend!!!"

text = "hElLo, HOW Are YoU?"
print(text.capitalize())  # Output: "Hello, how are you?"

url = "https://www.example.com"
domain = url.find("example")
print(domain)  # Output: 8

error_message = "404 Not Found"
fixed_message = error_message.replace("404", "200")
print(fixed_message)  # Output: "200 Not Found"

name = "Sarah"
event = "wedding"
invitation = "Dear {}, you are invited to my {}!".format(name, event)
print(invitation)  # Output: "Dear Sarah, you are invited to my wedding!"

sentence = "The quick brown fox jumps over the lazy dog."
result = sentence.startswith("The quick")
print(result)  # Output: True


email = "contact@company.com"
print(email.endswith(".com"))  # Output: True


sentence = "   Visit us at www.website.com  "
print(sentence.strip())  # Output: "Visit us at www.website.com"


addresses = "221B Baker Street, London; 742 Evergreen Terrace, Springfield"
addresses_list = addresses.split("; ")
print(addresses_list)  # Output: ["221B Baker Street, London", "742 Evergreen Terrace, Springfield"]

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Output: "Python is awesome"


article = "Python is great. Python is easy to learn."
print(article.replace("Python", "Java"))  # Output: "Java is great. Java is easy to learn."


text = "I love Python. Python is fun!"
print(text.count("Python"))  # Output: 2


greeting = "Good evening!"
print(len(greeting))  # Output: 13

age = 25

text = "I am " + str(age) + " years old."

print(text)

text = "python programming"
print(text.upper())

text = "HELLO PYTHON"
print(text.lower())

text = "learning python is fun"
print(text.capitalize())

sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.find("fox"))  # Output: 16
print(sentence.find("cat"))

quote = "An apple a day keeps the doctor away"
new_quote = quote.replace("apple", "banana")
print(new_quote)

city = "Paris"
country = "France"
message = "I visited {} in {}.".format(city, country)
print(message)

name = "John"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)

greeting = "Good morning, everyone!"
print(greeting.startswith("Good"))  # Output: True
print(greeting.startswith("Hello")) # Output: False

title = "Python for Beginners"
print(title.endswith("Beginners"))  # Output: True
print(title.endswith("Experts"))

sentence = "   Hello, World!   "
print(sentence.strip())  # Output: "Hello, World!"
print(sentence.lstrip())  # Output: "Hello, World!   "
print(sentence.rstrip())

colors = "red,blue,green,yellow"
color_list = colors.split()
color_list = colors.split(",")
print(color_list)

words = ["Coding", "is", "awesome"]
sentence = "-".join(words)
print(sentence)

