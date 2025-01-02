import openai
import streamlit as st
# Setting up OpenAI API Key
openai.api_key = "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"

def chat_with_gpt(prompt):
        # Request to OpenAI's ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        # Return the model's response
        return response.choices[0].message['content'].strip()


# main loop to interact with the chatbot
if __name__ == "__main__":
    print("Welcome to the Chatbot!")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        # Get chatbot response
        chatbot_response = chat_with_gpt(user_input)
        
        # Printing the chatbot's response
        print(f"Chatbot: {chatbot_response}")
