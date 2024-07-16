# import streamlit as st
# from groq import Groq
# from api import api_key

# client = Groq(api_key=api_key)

# st.title("A chatGPT like App") 

# user_question = st.text_input("Ask me anything") 

# message = {
#     "content": f"{user_question}",
#     "role": "user"
# }

# if st.button("ASK", use_container_width=400):
#     try:
#         chat_completion = client.chat.completions.create(
#             messages=[message],
#             model="llama3-8b-8192",
#         )
#         if chat_completion.choices:
#             content = chat_completion.choices[0].message.content
#             st.write(content)
#         else:
#             st.write("Error Occured")
#     except Exception as e:
#         st.write(f"Error occurred: {e}")

import streamlit as st
from groq import Groq
from api import api_key

client = Groq(api_key=api_key)

st.title("A chatGPT like App")

def chatGPT():
    user_question = st.text_input("You: ", "")
    
    if st.button("Ask", key="ask_button"):
        if user_question.strip() == "":
            st.write("Please ask something.")
        else:
            message = {
                "content": user_question,
                "role": "user"
            }
            
            try:
                chat_completion = client.chat.completions.create(
                    messages=[message],
                    model="llama3-8b-8192",
                )
                
                if chat_completion.choices:
                    response = chat_completion.choices[0].message.content
                    st.text_area("ChatGPT:", value=response, height=200)
                else:
                    st.write("ChatGPT: Error Occurred")
            
            except Exception as e:
                st.write(f"Error occurred: {e}")
chatGPT()