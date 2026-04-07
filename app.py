import streamlit as st

# 1. כותרת ראשית בסגול
st.markdown("<h1 style='text-align: center; color: purple;'>בוט הגיימינג של פלג 🎮</h1>", unsafe_allow_html=True)

# 2. רשימת משחקים מטורפת (הוספתי את כל המוכרים)
st.markdown("<p style='color: green; font-weight: bold;'>איזה משחק אתה הכי אוהב?</p>", unsafe_allow_html=True)
game_list = [
    "מיינקראפט", "רובלוקס", "פורטנייט", "Brawl Stars", "FIFA / FC 25", 
    "Valorant", "League of Legends", "Counter-Strike 2", "Rocket League", 
    "Call of Duty", "Apex Legends", "GTA V", "Subnautica", "Overwatch 2"
]
game = st.selectbox("", game_list, label_visibility="collapsed")

# 3. שאלה שנייה צבעונית (כל מילה בצבע אחר!)
st.markdown("""
    <p style='font-weight: bold;'>
        <span style='color: red;'>כמה</span> 
        <span style='color: orange;'>שעות</span> 
        <span style='color: yellow;'>שיחקת</span> 
        <span style='color: blue;'>היום</span> 
        <span style='color: violet;'>במשחק?</span>
    </p>
    """, unsafe_allow_html=True)
hours = st.text_input("", label_visibility="collapsed")

# 4. עיצוב הכפתור הכתום
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: orange;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        width: 100%;
    }
    </style>""", unsafe_allow_html=True)

if st.button("נתח את מצבי"):
    if hours.isdigit():
        h = int(hours)
        if h > 5:
            st.error(f"אחי, {h} שעות ב-{game} זה מוגזם! לך תבעט קצת בכדור בחוץ ⚽")
        elif h > 2:
            st.warning(f"אתה בדרך להיות פרו ב-{game}, אבל אל תשכח לאכול!")
        else:
            st.success(f"מצב מעולה, {game} זה אחלה משחק! יש לך עוד זמן לשחק.")
            st.balloons()
    else:
        st.error("תרשום את מספר השעות שלך, לא משהו אחר!")
