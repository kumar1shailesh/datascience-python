import random

# Define a dictionary of legal topics and their corresponding information
legal_topics = {
    "constitution": "The Constitution of India is the supreme law of the country.",
    "fundamental rights": "Fundamental rights are a set of basic rights and freedoms guaranteed to all individuals in India.",
    "criminal law": "Criminal law deals with offenses against society as a whole, such as murder, theft, and fraud.",
    "civil law": "Civil law deals with disputes between individuals or organizations, such as contract disputes or property disputes.",
    "judiciary": "The judiciary in India is an independent body responsible for interpreting and enforcing the law.",
    "ipc": "The Indian Penal Code (IPC) is a criminal code that defines various offenses and their punishments in India.",
    "ipcr": "The Indian Penal Code for Railways (IPCR) is a special criminal code that deals with offenses committed on railways in India.",
    "all laws": "The legal system in India consists of a wide range of laws, including criminal laws, civil laws, labor laws, taxation laws, and more. Each law is designed to govern specific aspects of society and provide guidelines for behavior and dispute resolution.",
}

# Define a function to handle user queries
def chat():
    print("Hello! I am a chatbot that can provide information about the Indian legal system.")
    print("You can ask me questions about legal topics or type 'quit' to exit.")

    while True:
        user_input = input("User: ").lower()

        if user_input == "quit":
            print("Thank you for using the chatbot. Goodbye!")
            break

        response = get_response(user_input)
        print("Chatbot:", response)

# Define a function to generate responses based on user input
def get_response(user_input):
    response = "I'm sorry, but I don't have information about that topic. Could you please ask something else?"

    for topic, info in legal_topics.items():
        if topic in user_input:
            response = info
            break

    return response

# Start the chatbot
chat()
