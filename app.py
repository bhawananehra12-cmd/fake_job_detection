import streamlit as st
import pickle
import os
import re
import base64

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="SafeApply",
    page_icon="🛡️",
    layout="wide"  
)

# =========================
# COLORS
# =========================
top_col1, top_col2 = st.columns([10, 1])
with top_col2:
    dark_mode = st.toggle("🌙")

if dark_mode:
    bg_color = "#0A2342"
    card_bg = "#102A43"
    text_color = "white"
    heading_color = "white"
else:
    bg_color = "#EBF4FA"  
    card_bg = "rgba(255,255,255,0.85)"
    text_color = "#111827"
    heading_color = "#1e3a8a"

# =========================
# CSS 
# =========================
st.markdown(f"""
<style>
.stApp {{
    background:{bg_color};
}}
.hero-sub {{
    color:{text_color};
}}
.glass {{
    background:{card_bg};
}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
#MainMenu { visibility:hidden; }
footer { visibility:hidden; }
header { visibility:hidden; }

[data-testid="stImage"] {
    pointer-events: none !important;
}
button[title="View fullscreen"] {
    display: none !important;
}

.logo-container {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 0;
}

.logo-text {
    font-size: 42px;
    font-weight: 900;
    font-family: sans-serif;
    white-space: nowrap;
}

.hero {
    text-align:center;
    padding:10px;
}

.hero-title {
    font-size: clamp(32px, 5vw, 60px); 
    font-weight:900;
    line-height: 1.2;
}

.fake { color:#ff69b4; }

.hero-sub {
    font-size: clamp(14px, 2vw, 20px); 
    font-weight:600;
    margin-top: 8px;
}

.glass {
    padding:25px;
    border-radius:25px;
    box-shadow:0px 8px 20px rgba(0,0,0,.25);
}

.stButton > button {
    width:100%;
    height:60px;
    font-size:20px;
    font-weight:bold;
    border-radius:15px;
    background:linear-gradient(90deg,#2563eb,#3b82f6);
    color:white;
    border:none;
}

.side-img-wrapper img {
    border-radius: 12px;
    width: 100% !important;
    height: auto !important;
}

.fake-crop-container img {
    object-fit: cover !important;
    object-position: top center !important;
    max-height: 310px !important; 
}

.center-result-box {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 100%;
}

.real-card-mod, .fake-card-mod {
    color:white;
    padding:12px 35px;
    border-radius:15px;
    font-size: clamp(18px, 4vw, 24px); 
    font-weight:bold;
    display: inline-block;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
    max-width: 90%;
}

.real-card-mod { background:#10b981; }
.fake-card-mod { background:#ef4444; }

.footer {
    margin-top:50px;
    text-align:center;
    font-size:18px;
    font-weight:600;
}

@media (max-width: 768px) {
    .logo-container {
        justify-content: center;
    }
    .logo-text {
        font-size: 32px; 
    }
    .side-img-wrapper {
        display: none !important;
    }
    .glass {
        padding: 15px;
        border-radius: 15px;
    }
    .stTextArea textarea {
        height: 220px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# TOP BAR LOGO
# =========================
with top_col1:
    def load_img_base64(path):
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        return None

    base64_data = load_img_base64("lock.jpg") or load_img_base64("lock.jpeg")
    
    if base64_data:
        src_string = f"data:image/jpeg;base64,{base64_data}"
    else:
        src_string = "https://img.icons8.com/fluency/48/lock.png"

    st.markdown(f"""
    <div class="logo-container">
        <img src="{src_string}" width="45" height="45" style="border-radius: 8px; object-fit: cover;">
        <div class="logo-text">
            <span style="color:#1565C0;">Safe</span><span style="color:#50C878;">Apply</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown(f"""
<div class="hero">
    <div class="hero-title" style="color:{heading_color};">
        🛡️ <span class="fake">Fake Job Detection System</span>
    </div>
    <div class="hero-sub">
        Stay Safe • Verify Jobs • Apply With Confidence
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# LOAD MODEL
# =========================
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# =========================
# MAIN SECTION
# =========================
left, center, right = st.columns([1, 3, 1])

with left:
    st.markdown('<div class="side-img-wrapper">', unsafe_allow_html=True)
    if os.path.exists("real.jpg"):
        st.image("real.jpg", use_container_width=True)
    elif os.path.exists("real.jpeg"):
        st.image("real.jpeg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with center:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color:{heading_color}; margin-top:0;'>Job Description</h2>", unsafe_allow_html=True)

    job_text = st.text_area(
        label="Job Input Field",
        label_visibility="collapsed",
        height=320,
        placeholder="""Paste complete job description here...

Example:
We are hiring a Python Developer with Django, Machine Learning and Cloud experience..."""
    )

    analyze = st.button("🔍 Analyze Job Posting")
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown('<div class="side-img-wrapper fake-crop-container">', unsafe_allow_html=True)
    if os.path.exists("fake.jpg"):
        st.image("fake.jpg", use_container_width=True)
    elif os.path.exists("fake.jpeg"):
        st.image("fake.jpeg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# RESULT
# =========================
if analyze:
    if not job_text.strip():
        st.warning("Please enter job description.")
    else:
        cleaned_text = job_text.strip().lower()
        
        data = vectorizer.transform([cleaned_text])
        prediction = model.predict(data)
        
        print("\n=== SAFEAPPLY ML DEBUGGER ===")
        print(f"Raw Prediction Output: {prediction[0]}")
        print(f"Matrix Token Sum: {data.sum()}")
        print("===============================\n")

        st.markdown("<br>", unsafe_allow_html=True)

        sad_img_path = "sad.jpg" if os.path.exists("sad.jpg") else "sad.jpeg"
        happy_img_path = "happy.jpg" if os.path.exists("happy.jpg") else "happy.jpeg"

        if prediction[0] == 1:
            st.markdown("""
            <div class="center-result-box">
                <div class="fake-card-mod">
                    🚨 FAKE JOB DETECTED
                </div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2, c3 = st.columns([2.2, 1, 2.2])
            with c2:
                st.markdown("<br>", unsafe_allow_html=True)
                st.image(sad_img_path, use_container_width=True)

        elif prediction[0] == 0:
            st.markdown("""
            <div class="center-result-box">
                <div class="real-card-mod">
                    ✅ REAL JOB POST
                </div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2, c3 = st.columns([2.2, 1, 2.2])
            with c2:
                st.markdown("<br>", unsafe_allow_html=True)
                st.image(happy_img_path, use_container_width=True)

# =========================
# FOOTER
# =========================
st.markdown(f"""
<div class="footer" style="color:{text_color};">
Made with ❤️ by Bhawana Nehra 💙🐶
</div>
""", unsafe_allow_html=True)
