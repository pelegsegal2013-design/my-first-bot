import streamlit as st

# set page config for icon and title
st.set_page_config(page_title="בוט הגיימינג של פלג", page_icon="🎮", layout="centered")

# 1. כותרת ראשית בסגול
st.markdown("<h1 style='text-align: center; color: purple;'>בוט הגיימינג של פלג 🎮</h1>", unsafe_allow_html=True)

# קישורים לתמונות של המשחקים (השתמשתי בקישורים חיצוניים)
images = {
    "מיינקראפט": "https://images.unsplash.com/photo-1627398242454-45a1465c2479?q=80&w=200&auto=format&fit=crop",
    "רובלוקס": "https://images.unsplash.com/photo-1662164434193-2c40c5f2105a?q=80&w=200&auto=format&fit=crop",
    "פורטנייט": "https://images.unsplash.com/photo-1614031679232-00e99b2f6793?q=80&w=200&auto=format&fit=crop",
    "Brawl Stars": "https://images.unsplash.com/photo-1601053264024-e0c1b4e64f72?q=80&w=200&auto=format&fit=crop",
    "FIFA / FC 25": "https://images.unsplash.com/photo-1614632537423-1e6c2e590dac?q=80&w=200&auto=format&fit=crop",
    "Valorant": "https://images.unsplash.com/photo-1613143493489-08ae3e0b7b1c?q=80&w=200&auto=format&fit=crop",
    "League of Legends": "https://images.unsplash.com/photo-1581007871115-f14bc016e0a4?q=80&w=200&auto=format&fit=crop",
    "Counter-Strike 2": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?q=80&w=200&auto=format&fit=crop",
    "Rocket League": "https://images.unsplash.com/photo-1614332287897-ccd48ccaf721?q=80&w=200&auto=format&fit=crop",
    "Call of Duty": "https://images.unsplash.com/photo-1614632537423-1e6c2e590dac?q=80&w=200&auto=format&fit=crop",
    "Apex Legends": "https://images.unsplash.com/photo-1614332287897-ccd48ccaf721?q=80&w=200&auto=format&fit=crop",
    "GTA V": "https://images.unsplash.com/photo-1581007871115-f14bc016e0a4?q=80&w=200&auto=format&fit=crop",
    "Subnautica": "https://images.unsplash.com/photo-1601053264024-e0c1b4e64f72?q=80&w=200&auto=format&fit=crop",
    "Overwatch 2": "https://images.unsplash.com/photo-1613143493489-08ae3e0b7b1c?q=80&w=200&auto=format&fit=crop"
}

# 2. בחירת המשחק ושאלה ראשונה בירוק
st.markdown("<p style='color: green; font-weight: bold;'>איזה משחק אתה הכי אוהב?</p>", unsafe_allow_html=True)
game_list = list(images.keys())
game = st.selectbox("", game_list, label_visibility="collapsed")

# הצגת תמונה בצד (משתמשים בעמודות כדי לשים את התמונה בצד)
col1, col2 = st.columns([3, 1])
with col1:
    # 3. שאלה שנייה צבעונית
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
with col2:
    # הצגת התמונה המתאימה בצד
    st.image(images[game], width=100)

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
        # ההודעה המתוחכמת עם האימוג'י
        st.error("תרשום את מספר השעות אל תנסה לעבוד על הבוט 😏")
