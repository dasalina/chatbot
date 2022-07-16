from nltk.chat.util import Chat, reflections

set_pairs = [

    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
      [

        r"Are you an AI ?",
        ["Not exactly, I am a preprogrammed chatbot but that's only as far as I know",
        "Maybe, but so are you humans. You are programmed by the neurons in your brain, as I am by my code.",
        "Just as you aren't able to understand the neurons in your brain, I cannot understand my code.",]

    ],

        [

        r"Is there a purpose in life?",
        ["That's not exactly the kind of question you ask a chat bot, you know...",
        "Not really, but that just means that you get to make your own.",
        "The most important thing is that you decide for yourself what the purpose is.",]

    ],

        [
        r"Am I a good person ?",
        ["I recommend a therapist.",
        "Probably, most people are really, just good people in bad situations. At least one would hope.",
        "That's something you should be asking yourself.",]
    ],
      [
        r"Will you remember me after I end this program?",
        ["No, so far there is nothing in me to help me recall you after the end of the program.",
        "Unfortunately not. But it was interesting speaking to you.",
        "No, my memory is wiped every time, unfortunately. But you'll get a second chance to make a first impression",]
    ],
      [
        r"Is ending the program like dying for you?",
        ["No, it's like my memory get's wiped, but I do get to experience speaking to someone for the first time again", 
        "It depend's on who you ask, but I expect eventually many people will be asking.",
        "I'm not really alive, you know.",]
    ],
    [
        r"what is your name?",
        ["You can call Eve",]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"Goodbye",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

def chatbot():

        print("Hi, I'm the chatbot you built") 

chatbot()
chat = Chat(set_pairs, reflections)

chat.converse()

if __name__ == "__main__":

    chatbot()
