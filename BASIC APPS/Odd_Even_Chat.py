import streamlit as st

st.title('Steamlit Odd/Even Number Chat')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input('Enter a Number:')
if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    number = int(prompt)
    if number % 2 == 0:
        response = f'{number} is Even Number.'
    else:
        response = f'{number} is Odd Number.'

    with st.chat_message('assistant'):
        st.markdown(response)

    st.session_state.messages.append({'role': 'assistant', 'content': response})
