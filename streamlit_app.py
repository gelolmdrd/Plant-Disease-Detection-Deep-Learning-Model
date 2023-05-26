import streamlit as st

def main():
    st.title('My React App')

    # Embed your React app using an iframe
    st.components.iframe("https://www.example.com/my-react-app")

if __name__ == '__main__':
    main()
