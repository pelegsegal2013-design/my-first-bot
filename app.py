import streamlit as st

st.title("בוט הגיימינג של :purple[פלג] 🎮")

# 1. הבוט שואל שאלה
game = st.selectbox("איזה משחק אתה הכי אוהב?", ["מיינקראפט", "רובלוקס", "פורטנייט"])
hours = st.text_input("כמה שעות שיחקת היום?")

# 2. הבוט מבצע לוגיקה כשלוחצים על הכפתור
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
        st.write("תכתוב מספר שעות, אל תנסה לעבוד על הבוט!")
