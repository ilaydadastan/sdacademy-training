
greeting = "Good morning!   "
print(len(greeting))


age = 25
text = "I am " + str(age) + " years old."
print(text)

text = "python Programming"
print(text.upper())

text = "HELLO PYTHON"
print(text.lower())

text = "learning python is fun"
print(text.capitalize())

sentence = "an apple a day keeps the doctor away"
print(sentence.find("doctor"))
print(sentence.replace("apple", "banana"))


city = "Paris"
country = "France"
message = "I visited {} in {}".format(city, country)
print(message)


greeting = "Good morning everyone!!"
print(greeting.startswith("good"))
print(greeting.endswith("!"))


title = "   Python Programming Built in Features  "
print(title.strip())
print(title.lstrip())
print(title.rstrip())


colors = "red,blue,green,yellow"
color_list = colors.split(",")
print(color_list)

words = ["Coding", "is", "awesome"]
sentence = "-".join(words)
print(sentence)




