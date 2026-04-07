import streamlit as st

# 1. כותרת ראשית בסגול (בלי המילה purple רשומה)
st.markdown("<h1 style='text-align: center; color: purple;'>בוט הגיימינג של פלג 🎮</h1>", unsafe_allow_html=True)

# 2. שאלה ראשונה בירוק
st.markdown("<p style='color: green; font-weight: bold;'>איזה משחק אתה הכי אוהב?</p>", unsafe_allow_html=True)
game = st.selectbox("", ["מיינקראפט", "רובלוקס", "פורטנייט" ,"אוור וואצ ,], label_visibility="collapsed")

# 3. שאלה שנייה צבעונית (נשתמש בכחול למשל)
st.markdown("<p style='color: #0080ff; font-weight: bold;'>כמה שעות שיחקת היום?</p>", unsafe_allow_html=True)
hours = st.text_input("", label_visibility="collapsed")

# 4. כפתור כתום (ב-Streamlit אי אפשר לצבוע רק את הכפתור בקלות, אז נשים טקסט כתום מעליו או נשתמש בטריק)
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: orange;
        color: white;
    }
    </style>""", unsafe_allow_html=True)

if st.button("נתח את מצבי"):
    if hours.isdigit():
        h = int(hours)
        if h > 5:
            st.error("אחי, הגזמת! לך תבעט קצת בכדור בחוץ ⚽")
        elif h > 2:
            st.warning("אתה בדרך להיות פרו, אבל אל תשכח לאכול!")
        else:
            st.success("מצב מעולה, יש לך עוד זמן לשחק!")
            st.balloons()
    else:
        st.error("תרשום את הציון שלך לא משהו אחר!")
