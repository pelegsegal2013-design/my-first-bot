import streamlit as st

st.title("האתר של פלג 🚀")

# יצרנו תיבה שבה המשתמש כותב את הציון שלו
grade = st.text_input("מה הציון שלך במתמטיקה?")

# הוספנו כפתור כדי שהבדיקה לא תרוץ "ישר"
if st.button("בדוק ציון"):
    if grade: # בודק שלא השארת ריק
        if int(grade) > 90:
            st.success("Excellent logic! 🏆")
            st.disco()
        else:
            st.warning("Keep practicing! 💪")
else:
    st.error("תרשום את הציון שלך לא משהו אחר!")
