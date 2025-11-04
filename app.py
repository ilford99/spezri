import streamlit as st
import time
import random
from textwrap import dedent
import streamlit.components.v1 as components

st.set_page_config(page_title="Danke!", page_icon="🎉", layout="wide")

# --- Clean UI ---
hide_default = """
<style>
#MainMenu, header, footer {visibility: hidden;}
.block-container {padding: 0 1rem 2rem;}
html, body, .stApp {height: 100%;}
/* Fullscreen animated gradient */
.bg {
  position: fixed; inset: 0;
  background: linear-gradient(120deg, #4b3cff, #ff2d78, #ffb703, #00d4ff);
  background-size: 300% 300%;
  animation: move 18s ease-in-out infinite;
  filter: saturate(1.1);
}
@keyframes move { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }

/* Center stage */
.stage { position: relative; z-index: 2; min-height: 100vh; display: grid; place-items: center; text-align: center; }
.huge {
  font-size: clamp(48px, 9vw, 150px);
  line-height: 1.0; font-weight: 900; letter-spacing: 1px;
  color: white; text-shadow: 0 10px 30px rgba(0,0,0,.35);
}
.sub {
  margin-top: .6rem; font-size: clamp(18px, 2.5vw, 38px);
  color: rgba(255,255,255,.95); font-weight: 600;
}
.badge { display:inline-flex; align-items:center; gap:.6rem; padding:.6rem 1rem; border-radius:999px; background:rgba(255,255,255,.12); backdrop-filter: blur(6px); color:#fff; font-weight:700; border:1px solid rgba(255,255,255,.25); }
.btnrow{margin-top:2rem; display:flex; gap:1rem; justify-content:center; flex-wrap:wrap}
.btn{cursor:pointer; padding:.9rem 1.2rem; border-radius:14px; border:1px solid rgba(255,255,255,.35); background:rgba(0,0,0,.25); color:#fff; font-size:1rem; font-weight:700}
.btn:hover{transform: translateY(-1px); filter:brightness(1.08)}

/* Subtle floating emojis */
.floaters { position: fixed; inset:0; pointer-events:none; z-index:1; }
.emoji { position:absolute; font-size: clamp(20px, 4vw, 42px); opacity:.9; animation: rise 14s linear infinite; }
@keyframes rise { from { transform: translateY(15vh) } to { transform: translateY(-110vh) } }
</style>
<div class="bg"></div>
"""
st.markdown(hide_default, unsafe_allow_html=True)

# --- Floating emojis (pure CSS, randomized positions) ---
import random
emojis = ["🎉","🎈","✨","💖","🥳","🌟","🎊","💫"]
positions = []
random.seed(7)
for i in range(28):
    left = random.randint(0, 100)
    delay = random.uniform(0, 12)
    emoji = random.choice(emojis)
    positions.append((left, delay, emoji))
html_floaters = [f'<div class="emoji" style="left:{l}%; bottom:-10vh; animation-delay:{d:.1f}s">{e}</div>' for l,d,e in positions]
st.markdown('<div class="floaters">' + ''.join(html_floaters) + '</div>', unsafe_allow_html=True)

# --- Hero content ---
col = st.container()
with col:
    st.markdown('<div class="stage">', unsafe_allow_html=True)
    st.markdown('<div class="badge">💌 Von Herzen: Danke!</div>', unsafe_allow_html=True)
    st.markdown('<div class="huge">DANKE<br/>FÜR EURE WUNDERSCHÖNEN KARTEN</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub">Ihr habt mir den Tag versüsst – ihr seid grossartig. 💫</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Confetti via JS (canvas-confetti) ---
confetti_html = dedent(
    """
    <div id="confetti-root"></div>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
    <script>
      function burst() {
        const count = 300; // intense!
        const defaults = { origin: { y: 0.7 } };
        function fire(particleRatio, opts) {
          confetti(Object.assign({}, defaults, opts, { particleCount: Math.floor(count * particleRatio) }));
        }
        fire(0.25, { spread: 46, startVelocity: 55 });
        fire(0.2,  { spread: 60 });
        fire(0.35, { spread: 120, decay: 0.91, scalar: 1.0 });
        fire(0.1,  { spread: 120, startVelocity: 35, decay: 0.92 });
        fire(0.1,  { spread: 120, startVelocity: 25 });
      }
      // Grand opening
      burst();
      // Encore bursts
      let times = 0;
      const encore = setInterval(()=>{ burst(); times++; if(times>2) clearInterval(encore); }, 2200);

      // Subtle stream for a few seconds
      const duration = 3000;
      const end = Date.now() + duration;
      (function frame() {
        confetti({ particleCount: 4, angle: 60, spread: 55, origin: { x: 0 } });
        confetti({ particleCount: 4, angle: 120, spread: 55, origin: { x: 1 } });
        if (Date.now() < end) requestAnimationFrame(frame);
      }());
    </script>
    """
)
components.html(confetti_html, height=0)

# --- Balloons (Streamlit native, triggers once per rerun) ---
st.balloons()

# --- Optional: one tap to replay confetti ---
replay = st.button("✨ Noch mehr Konfetti!")
if replay:
    components.html(confetti_html, height=0)
    st.balloons()
import streamlit as st
import time
import random
from textwrap import dedent
import streamlit.components.v1 as components

st.set_page_config(page_title="Danke!", page_icon="🎉", layout="wide")

# --- Clean UI ---
hide_default = """
<style>
#MainMenu, header, footer {visibility: hidden;}
.block-container {padding: 0 1rem 2rem;}
html, body, .stApp {height: 100%;}
/* Fullscreen animated gradient */
.bg {
  position: fixed; inset: 0;
  background: linear-gradient(120deg, #4b3cff, #ff2d78, #ffb703, #00d4ff);
  background-size: 300% 300%;
  animation: move 18s ease-in-out infinite;
  filter: saturate(1.1);
}
@keyframes move { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }

/* Center stage */
.stage { position: relative; z-index: 2; min-height: 100vh; display: grid; place-items: center; text-align: center; }
.huge {
  font-size: clamp(48px, 9vw, 150px);
  line-height: 1.0; font-weight: 900; letter-spacing: 1px;
  color: white; text-shadow: 0 10px 30px rgba(0,0,0,.35);
}
.sub {
  margin-top: .6rem; font-size: clamp(18px, 2.5vw, 38px);
  color: rgba(255,255,255,.95); font-weight: 600;
}
.badge { display:inline-flex; align-items:center; gap:.6rem; padding:.6rem 1rem; border-radius:999px; background:rgba(255,255,255,.12); backdrop-filter: blur(6px); color:#fff; font-weight:700; border:1px solid rgba(255,255,255,.25); }
.btnrow{margin-top:2rem; display:flex; gap:1rem; justify-content:center; flex-wrap:wrap}
.btn{cursor:pointer; padding:.9rem 1.2rem; border-radius:14px; border:1px solid rgba(255,255,255,.35); background:rgba(0,0,0,.25); color:#fff; font-size:1rem; font-weight:700}
.btn:hover{transform: translateY(-1px); filter:brightness(1.08)}

/* Subtle floating emojis */
.floaters { position: fixed; inset:0; pointer-events:none; z-index:1; }
.emoji { position:absolute; font-size: clamp(20px, 4vw, 42px); opacity:.9; animation: rise 14s linear infinite; }
@keyframes rise { from { transform: translateY(15vh) } to { transform: translateY(-110vh) } }
</style>
<div class="bg"></div>
"""
st.markdown(hide_default, unsafe_allow_html=True)

# --- Floating emojis (pure CSS, randomized positions) ---
import random
emojis = ["🎉","🎈","✨","💖","🥳","🌟","🎊","💫"]
positions = []
random.seed(7)
for i in range(28):
    left = random.randint(0, 100)
    delay = random.uniform(0, 12)
    emoji = random.choice(emojis)
    positions.append((left, delay, emoji))
html_floaters = [f'<div class="emoji" style="left:{l}%; bottom:-10vh; animation-delay:{d:.1f}s">{e}</div>' for l,d,e in positions]
st.markdown('<div class="floaters">' + ''.join(html_floaters) + '</div>', unsafe_allow_html=True)

# --- Hero content ---
col = st.container()
with col:
    st.markdown('<div class="stage">', unsafe_allow_html=True)
    st.markdown('<div class="badge">💌 Von Herzen: Danke!</div>', unsafe_allow_html=True)
    st.markdown('<div class="huge">DANKE<br/>FÜR EURE WUNDERSCHÖNEN KARTEN</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub">Ihr habt mir den Tag versüsst – ihr seid grossartig. 💫</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Confetti via JS (canvas-confetti) ---
confetti_html = dedent(
    """
    <div id="confetti-root"></div>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
    <script>
      function burst() {
        const count = 300; // intense!
        const defaults = { origin: { y: 0.7 } };
        function fire(particleRatio, opts) {
          confetti(Object.assign({}, defaults, opts, { particleCount: Math.floor(count * particleRatio) }));
        }
        fire(0.25, { spread: 46, startVelocity: 55 });
        fire(0.2,  { spread: 60 });
        fire(0.35, { spread: 120, decay: 0.91, scalar: 1.0 });
        fire(0.1,  { spread: 120, startVelocity: 35, decay: 0.92 });
        fire(0.1,  { spread: 120, startVelocity: 25 });
      }
      // Grand opening
      burst();
      // Encore bursts
      let times = 0;
      const encore = setInterval(()=>{ burst(); times++; if(times>2) clearInterval(encore); }, 2200);

      // Subtle stream for a few seconds
      const duration = 3000;
      const end = Date.now() + duration;
      (function frame() {
        confetti({ particleCount: 4, angle: 60, spread: 55, origin: { x: 0 } });
        confetti({ particleCount: 4, angle: 120, spread: 55, origin: { x: 1 } });
        if (Date.now() < end) requestAnimationFrame(frame);
      }());
    </script>
    """
)
components.html(confetti_html, height=0)

# --- Balloons (Streamlit native, triggers once per rerun) ---
st.balloons()

# --- Optional: one tap to replay confetti ---
replay = st.button("✨ Noch mehr Konfetti!")
if replay:
    components.html(confetti_html, height=0)
    st.balloons()
