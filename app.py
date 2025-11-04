import streamlit as st
import time
import random
from datetime import datetime
from textwrap import dedent
import streamlit.components.v1 as components

# Seitenkonfiguration
st.set_page_config(
    page_title="💖 Danke Rita!", 
    page_icon="🌸", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Erweiterte CSS Styles ---
enhanced_styles = """
<style>
/* Verstecke Standard-Elemente */
#MainMenu, header, footer {visibility: hidden;}
.block-container {padding: 0 !important; max-width: 100% !important;}
main[role="main"] {padding: 0 !important;}
section[data-testid="stSidebar"] {display: none;}
html, body, .stApp {height: 100%; overflow-x: hidden;}

/* Animierter Gradient-Hintergrund mit mehr Farben */
.bg {
    position: fixed; 
    inset: 0;
    background: linear-gradient(135deg, 
        #667eea 0%, 
        #f093fb 15%, 
        #f5576c 30%, 
        #fda085 45%, 
        #f6d365 60%, 
        #a8edea 75%, 
        #667eea 100%);
    background-size: 400% 400%;
    animation: gradientShift 20s ease infinite;
    filter: saturate(1.2);
}

@keyframes gradientShift { 
    0% {background-position: 0% 50%} 
    50% {background-position: 100% 50%} 
    100% {background-position: 0% 50%} 
}

/* Glitzer-Overlay */
.sparkle-overlay {
    position: fixed;
    inset: 0;
    background-image: 
        radial-gradient(2px 2px at 20px 30px, white, transparent),
        radial-gradient(2px 2px at 40px 70px, white, transparent),
        radial-gradient(1px 1px at 50px 90px, white, transparent),
        radial-gradient(1px 1px at 130px 80px, white, transparent),
        radial-gradient(2px 2px at 150px 10px, white, transparent);
    background-repeat: repeat;
    background-size: 200px 200px;
    animation: sparkle 8s linear infinite;
    opacity: 0.3;
    z-index: 1;
}

@keyframes sparkle {
    0% {transform: translateX(0);}
    100% {transform: translateX(200px);}
}

/* Hauptbühne */
.stage {
    position: relative;
    z-index: 3;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 2rem;
    animation: fadeInUp 1.5s ease-out;
}

@keyframes fadeInUp {
    from {opacity: 0; transform: translateY(30px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Haupttext mit Glow-Effekt */
.huge {
    font-size: clamp(56px, 10vw, 180px);
    line-height: 1.1;
    font-weight: 900;
    letter-spacing: -1px;
    color: white;
    text-shadow: 
        0 0 40px rgba(255,255,255,0.5),
        0 0 80px rgba(255,182,193,0.4),
        0 10px 30px rgba(0,0,0,0.3);
    margin: 1rem 0;
    animation: pulse 3s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% {transform: scale(1);}
    50% {transform: scale(1.02);}
}

/* Untertext */
.sub {
    margin-top: 1.5rem;
    font-size: clamp(20px, 3vw, 42px);
    color: rgba(255,255,255,0.95);
    font-weight: 600;
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    max-width: 800px;
    line-height: 1.4;
}

/* Badge mit Animation */
.badge {
    display: inline-flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.8rem 1.5rem;
    border-radius: 999px;
    background: linear-gradient(135deg, rgba(255,255,255,0.25), rgba(255,255,255,0.1));
    backdrop-filter: blur(10px);
    color: #fff;
    font-weight: 800;
    font-size: clamp(16px, 2vw, 24px);
    border: 2px solid rgba(255,255,255,0.3);
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    animation: float 6s ease-in-out infinite;
}

@keyframes float {
    0%, 100% {transform: translateY(0);}
    50% {transform: translateY(-10px);}
}

/* Herz-Animation */
.heart-container {
    position: relative;
    margin: 2rem 0;
    height: 120px;
}

.beating-heart {
    font-size: clamp(60px, 8vw, 100px);
    animation: heartbeat 1.5s ease-in-out infinite;
    display: inline-block;
    filter: drop-shadow(0 0 20px rgba(255,105,180,0.6));
}

@keyframes heartbeat {
    0% {transform: scale(1);}
    14% {transform: scale(1.3);}
    28% {transform: scale(1);}
    42% {transform: scale(1.3);}
    70% {transform: scale(1);}
}

/* Schwebende Emojis mit verschiedenen Geschwindigkeiten */
.floaters {position: fixed; inset: 0; pointer-events: none; z-index: 2;}
.emoji {
    position: absolute;
    font-size: clamp(24px, 4vw, 48px);
    opacity: 0.85;
    animation: rise var(--duration) linear infinite;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
}

@keyframes rise {
    from {
        transform: translateY(110vh) rotate(0deg);
        opacity: 0;
    }
    10% {opacity: 0.85;}
    90% {opacity: 0.85;}
    to {
        transform: translateY(-10vh) rotate(360deg);
        opacity: 0;
    }
}

/* Buttons mit Hover-Effekt */
.btn-container {
    margin-top: 3rem;
    display: flex;
    gap: 1.5rem;
    justify-content: center;
    flex-wrap: wrap;
}

.magic-btn {
    cursor: pointer;
    padding: 1rem 2rem;
    border-radius: 50px;
    border: 2px solid rgba(255,255,255,0.4);
    background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
    backdrop-filter: blur(10px);
    color: #fff;
    font-size: clamp(16px, 1.5vw, 20px);
    font-weight: 800;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    text-decoration: none;
    display: inline-block;
}

.magic-btn:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 6px 25px rgba(0,0,0,0.3);
    border-color: rgba(255,255,255,0.6);
    background: linear-gradient(135deg, rgba(255,255,255,0.3), rgba(255,255,255,0.15));
}

/* Message Cards */
.message-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,255,255,0.05));
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem auto;
    max-width: 600px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    animation: slideIn 1s ease-out 0.5s both;
    color: white;
    text-align: center;
}

@keyframes slideIn {
    from {opacity: 0; transform: translateX(-50px);}
    to {opacity: 1; transform: translateX(0);}
}

.quote {
    font-style: italic;
    font-size: clamp(18px, 2.5vw, 26px);
    line-height: 1.6;
    opacity: 0.95;
}

/* Responsivität */
@media (max-width: 768px) {
    .stage {padding: 1rem;}
    .huge {font-size: clamp(48px, 12vw, 120px);}
    .btn-container {flex-direction: column; align-items: center;}
    .magic-btn {width: 250px;}
}

/* Zusätzliche Animationen */
.glow {
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from {text-shadow: 0 0 20px rgba(255,255,255,0.5);}
    to {text-shadow: 0 0 30px rgba(255,255,255,0.8), 0 0 40px rgba(255,105,180,0.6);}
}

/* Sterne-Hintergrund */
.stars {
    position: fixed;
    inset: 0;
    z-index: 1;
}

.star {
    position: absolute;
    width: 2px;
    height: 2px;
    background: white;
    border-radius: 50%;
    animation: twinkle 3s infinite;
}

@keyframes twinkle {
    0%, 100% {opacity: 0;}
    50% {opacity: 1;}
}
</style>
"""

st.markdown(enhanced_styles, unsafe_allow_html=True)

# Hintergründe
st.markdown('<div class="bg"></div>', unsafe_allow_html=True)
st.markdown('<div class="sparkle-overlay"></div>', unsafe_allow_html=True)

# Sterne generieren
stars_html = '<div class="stars">'
random.seed(42)
for _ in range(50):
    left = random.randint(0, 100)
    top = random.randint(0, 100)
    delay = random.uniform(0, 3)
    stars_html += f'<div class="star" style="left:{left}%; top:{top}%; animation-delay:{delay}s;"></div>'
stars_html += '</div>'
st.markdown(stars_html, unsafe_allow_html=True)

# Erweiterte schwebende Emojis mit verschiedenen Geschwindigkeiten
emojis = ["🎉","🎈","✨","💖","🥳","🌟","🎊","💫","🫶","💐","🎀","🤍","🕊️","🌸","🧡","😍","🤩","🦋","🌺","💕","🌈","⭐"]
floater_html = '<div class="floaters">'
random.seed(77)
for i in range(35):
    left = random.randint(5, 95)
    delay = random.uniform(0, 15)
    duration = random.uniform(12, 20)
    emoji = random.choice(emojis)
    floater_html += f'<div class="emoji" style="left:{left}%; animation-delay:{delay}s; --duration:{duration}s;">{emoji}</div>'
floater_html += '</div>'
st.markdown(floater_html, unsafe_allow_html=True)

# Hauptinhalt
st.markdown('<div class="stage">', unsafe_allow_html=True)

# Badge
st.markdown('<div class="badge">💌 Eine besondere Nachricht</div>', unsafe_allow_html=True)

# Animiertes Herz
st.markdown('<div class="heart-container"><span class="beating-heart">💗</span></div>', unsafe_allow_html=True)

# Hauptnachricht mit Glow-Effekt
st.markdown('<div class="huge glow">DANKE<br/>LIEBE RITA</div>', unsafe_allow_html=True)

# Untertitel
st.markdown('''
<div class="sub">
    Deine wunderschöne Karte war wie ein kleiner Sonnenstrahl ☀️<br/>
    Sie hat meinen Tag erhellt und mein Herz erwärmt 🫶
</div>
''', unsafe_allow_html=True)

# Nachrichtenkarte mit persönlicher Note
st.markdown('''
<div class="message-card">
    <div class="quote">
        "Die schönsten Geschenke kommen von Herzen –<br/>
        und deine Karte war ein Meisterwerk der Herzlichkeit."
    </div>
    <br/>
    <div style="font-size: 24px; margin-top: 1rem;">🌸 🤍 🌸</div>
</div>
''', unsafe_allow_html=True)

# Interaktive Buttons
st.markdown('''
<div class="btn-container">
    <button class="magic-btn" onclick="triggerConfetti()">✨ Mehr Magie</button>
    <button class="magic-btn" onclick="showLove()">💕 Extra Liebe</button>
    <button class="magic-btn" onclick="playSound()">🎵 Freudentanz</button>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Verbessertes Konfetti mit mehreren Effekten
enhanced_confetti = """
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
<script>
    // Initiales Feuerwerk
    function launchFireworks() {
        const duration = 3000;
        const animationEnd = Date.now() + duration;
        const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };
        
        function randomInRange(min, max) {
            return Math.random() * (max - min) + min;
        }
        
        const interval = setInterval(function() {
            const timeLeft = animationEnd - Date.now();
            
            if (timeLeft <= 0) {
                return clearInterval(interval);
            }
            
            const particleCount = 50 * (timeLeft / duration);
            
            // Konfetti von zwei Seiten
            confetti(Object.assign({}, defaults, {
                particleCount,
                origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 }
            }));
            confetti(Object.assign({}, defaults, {
                particleCount,
                origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 }
            }));
        }, 250);
    }
    
    // Herz-Konfetti
    function heartConfetti() {
        const scalar = 2;
        const heart = confetti.shapeFromText({ text: '💖', scalar });
        
        const defaults = {
            spread: 360,
            ticks: 100,
            gravity: 0.5,
            decay: 0.95,
            startVelocity: 20,
            shapes: [heart],
            scalar
        };
        
        confetti({
            ...defaults,
            particleCount: 30,
            origin: { x: 0.5, y: 0.35 }
        });
        
        setTimeout(() => {
            confetti({
                ...defaults,
                particleCount: 20,
                origin: { x: 0.5, y: 0.35 }
            });
        }, 300);
    }
    
    // Goldener Regen
    function goldenRain() {
        const duration = 5000;
        const animationEnd = Date.now() + duration;
        
        (function frame() {
            confetti({
                particleCount: 3,
                angle: 60,
                spread: 55,
                origin: { x: 0 },
                colors: ['#FFD700', '#FFA500', '#FFE4B5']
            });
            confetti({
                particleCount: 3,
                angle: 120,
                spread: 55,
                origin: { x: 1 },
                colors: ['#FFD700', '#FFA500', '#FFE4B5']
            });
            
            if (Date.now() < animationEnd) {
                requestAnimationFrame(frame);
            }
        }());
    }
    
    // Funktionen für Buttons
    function triggerConfetti() {
        launchFireworks();
    }
    
    function showLove() {
        heartConfetti();
        // Zusätzliche Herzen nach kurzer Verzögerung
        setTimeout(heartConfetti, 700);
        setTimeout(heartConfetti, 1400);
    }
    
    function playSound() {
        goldenRain();
        // Audio-Feedback simulieren mit visuellem Effekt
        document.body.style.animation = 'pulse 0.5s';
        setTimeout(() => {
            document.body.style.animation = '';
        }, 500);
    }
    
    // Starte mit einem großen Feuerwerk
    setTimeout(launchFireworks, 500);
    setTimeout(heartConfetti, 2000);
    setTimeout(goldenRain, 3500);
</script>
"""

components.html(enhanced_confetti, height=0)

# Streamlit Balloons als Extra
st.balloons()

# Footer mit Zeit-Stempel
current_time = datetime.now().strftime("%d.%m.%Y")
footer_html = f"""
<div style="position: fixed; bottom: 10px; left: 50%; transform: translateX(-50%); 
            color: rgba(255,255,255,0.6); font-size: 14px; z-index: 10;">
    Mit Liebe erstellt am {current_time} 🤍
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
