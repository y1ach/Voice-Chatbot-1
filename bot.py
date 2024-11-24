import pyttsx3
import time
import random

# pyttsx3 motoru başlatma
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def prompt(topic):
    if topic == "calc":
        print("Hesap Makinesi")
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division")

        operation = input("Choose an operation (1/2/3/4): ")

        try:
            sayi1 = int(input("Input the first number: "))
            sayi2 = int(input("Input the second number: "))
        except ValueError:
            result = "Invalid input! Please enter numbers only."
        else:
            if operation == '1':
                result = f"{sayi1} plus {sayi2} = {sayi1 + sayi2}"
            elif operation == '2':
                result = f"{sayi1} minus {sayi2} = {sayi1 - sayi2}"
            elif operation == '3':
                result = f"{sayi1} times {sayi2} = {sayi1 * sayi2}"
            elif operation == '4':
                if sayi2 != 0:
                    result = f"{sayi1} divided by {sayi2} = {sayi1 / sayi2}"
                else:
                    result = "We can't divide a number with zero!"
            else:
                result = "Invalid operation. Please choose 1, 2, 3, or 4."

        print(result)
        engine.say(result)
        engine.runAndWait()

    elif topic == "time":
        current_time = time.ctime()
        print(current_time)
        engine.say(current_time)
        engine.runAndWait()

    elif topic == "rmq":
        quotes = [
            "Believe you can and you're halfway there.",
            "Success is not the key to happiness. Happiness is the key to success.",
            "Don’t watch the clock; do what it does. Keep going.",
            "The future depends on what you do today.",
            "It always seems impossible until it’s done.",
            "Start where you are. Use what you have. Do what you can.",
            "Dream big and dare to fail.",
            "Do what you can, with what you have, where you are.",
            "Hardships often prepare ordinary people for an extraordinary destiny.",
            "Don’t let yesterday take up too much of today.",
            "The secret of getting ahead is getting started.",
            "You are never too old to set another goal or to dream a new dream.",
            "The only way to achieve the impossible is to believe it is possible.",
            "Keep your face always toward the sunshine—and shadows will fall behind you.",
            "Perseverance is not a long race; it is many short races one after the other.",
            "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
            "Success is walking from failure to failure with no loss of enthusiasm.",
            "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.",
            "Act as if what you do makes a difference. It does.",
            "Keep going. Everything you need will come to you at the perfect time.",
            "You don’t have to be great to start, but you have to start to be great.",
            "The best way to predict the future is to create it.",
            "What you get by achieving your goals is not as important as what you become by achieving your goals.",
            "Believe in yourself, take on your challenges, and dig deep within yourself to conquer fears.",
            "Don’t count the days; make the days count.",
            "You miss 100% of the shots you don’t take.",
            "The harder you work for something, the greater you’ll feel when you achieve it.",
            "Do something today that your future self will thank you for.",
            "Your limitation—it’s only your imagination.",
            "Great things never come from comfort zones.",
            "Dream it. Wish it. Do it.",
            "The key to success is to focus on goals, not obstacles.",
            "Your passion is waiting for your courage to catch up.",
            "Don’t stop when you’re tired. Stop when you’re done.",
            "Wake up with determination. Go to bed with satisfaction.",
            "Little things make big days.",
            "It’s going to be hard, but hard does not mean impossible.",
            "Don’t wait for opportunity. Create it.",
            "Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",
            "The only limit to our realization of tomorrow will be our doubts of today.",
            "Push yourself, because no one else is going to do it for you.",
            "Failure is the opportunity to begin again more intelligently.",
            "Action is the foundational key to all success.",
            "Great works are performed not by strength but by perseverance.",
            "Strive not to be a success, but rather to be of value.",
            "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
            "Motivation gets you going, but discipline keeps you growing.",
            "Your only limit is your mind."
        ]
        sentence = random.choice(quotes)
        print(sentence)
        engine.say(sentence)
        engine.runAndWait()

    else:
        print("Invalid topic. Please choose calc, time, or rmq.")

while True:
    user_input = input("Choose a topic:\n - calculator(calc)\n - time(time)\n - random motivational quote(rmq)\n - exit(exit)\nYour choice: ").strip().lower()
    if user_input == "exit":
        print("Goodbye!")
        break
    prompt(user_input)
