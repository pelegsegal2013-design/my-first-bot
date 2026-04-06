import streamlit as st

st.title("הבוט של פלג")
st.write("היי, אני בוט שיעזור לך.")

user_input = st.text_input("איך אתה מרגיש היום (טוב/לא טוב)?")

if user_input == "טוב":
    st.success("אני שמח לשמוע את זה! 😊")
elif user_input == "לא טוב":
    st.warning("אני מצטער לשמוע... איך אני יכול לעזור? 😔")
elif user_input != "":
    st.info("אני לא מבין, נסה לכתוב 'טוב' או 'לא טוב'.")
