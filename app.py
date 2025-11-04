import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
from urllib.parse import quote
import textwrap

st.set_page_config(page_title="Danke! 🎉", page_icon="🎉", layout="centered")

# --- Sidebar settings ---
st.sidebar.header("⚙️ Einstellungen")
app_title = st.sidebar.text_input("Titel der Seite", value="Danke für eure wunderschönen Karten! 🎂💌")
your_name = st.sidebar.text_input("Dein Name", value="Christian")
public_app_link = st.sidebar.text_input("(Optional) Öffentlicher Link zu dieser Seite", value="")
show_confetti = st.sidebar.checkbox("Konfetti/Ballons zeigen", value=True)

st.title(app_title)
st.write("Diese kleine App ist mein persönliches, digitales Dankeschön an alle, die mir so liebevoll gestaltete Karten geschickt haben. 💖")

if show_confetti:
    st.balloons()

# --- Upload section ---
st.subheader("1) Eure Karten – Galerie")
images = st.file_uploader("Lade Fotos/Scans der Karten hoch (JPG/PNG)", type=["jpg","jpeg","png"], accept_multiple_files=True)

if images:
    cols = st.columns(3)
    for i, f in enumerate(images):
        with cols[i % 3]:
            st.image(f, use_container_width=True, caption=f.name)
else:
    st.info("Noch keine Bilder hochgeladen. Du kannst die Galerie jederzeit später befüllen.")

# --- Recipients & notes ---
st.subheader("2) Namen & kurze Notizen")
st.caption("Eine Zeile pro Person. Format: **Name | kurze Notiz** (Notiz optional)")
raw_lines = st.text_area(
    "Beispiel:\nAlex | Die Aquarellblumen waren der Wahnsinn!\nMara | Deine Collage hat mich mega berührt.\nNonno",
    value="Alex | Die Aquarellblumen waren der Wahnsinn!\nMara | Deine Collage hat mich mega berührt.\nNonno",
    height=140
)

# --- Template ---
st.subheader("3) Dankestext‑Vorlage")
st.caption("Nutze Platzhalter: **{name}**, **{dein_name}** und **{notiz}**")
msg_template = st.text_area(
    "Vorlage",
    value=(
        "Hoi {name}!\n\n"
        "Von Herzen danke für die wunderschöne Karte – sie hat mir den Tag versüsst. "
        "{notiz}\n\n"
        "Herzlich, {dein_name}"
    ),
    height=140
)

colA, colB = st.columns(2)
with colA:
    add_wa_link = st.checkbox("WhatsApp‑Link mit Nachricht generieren", value=True)
with colB:
    include_app_link = st.checkbox("App‑Link (oben) am Ende der Nachricht anhängen", value=False)

# --- Parse recipients ---
recipients = []
for line in raw_lines.splitlines():
    if not line.strip():
        continue
    if "|" in line:
        n, note = [p.strip() for p in line.split("|", 1)]
    else:
        n, note = line.strip(), ""
    recipients.append({"name": n, "note": note})

# --- Message builder ---
if recipients:
    st.subheader("4) Vorschau & WhatsApp‑Links")
    for person in recipients:
        name = person["name"]
        note = person["note"]
        text = msg_template.replace("{name}", name).replace("{dein_name}", your_name).replace("{notiz}", note)
        if include_app_link and public_app_link:
            text += f"\n\n➡️ {public_app_link}"
        st.markdown(f"**{name}**")
        st.text(text)
        if add_wa_link:
            wa = f"https://wa.me/?text={quote(text)}"
            st.markdown(f"[📲 Nachricht in WhatsApp öffnen]({wa})")
        st.divider()
else:
    st.info("Füge mindestens eine Person hinzu, um Nachrichten zu erzeugen.")

# --- Thank‑you card generator ---
st.subheader("5) Persönliche Dankeskarte als Bild erzeugen (PNG)")
st.caption("Optional: Erzeuge ein einzelnes Bild mit deinem Dankestext – ideal zum Versenden.")

bg_choice = None
if images:
    selected_name = st.selectbox("Hintergrundbild wählen (optional)", ["(einfarbig)"] + [f.name for f in images])
    if selected_name != "(einfarbig)":
        bg_choice = next((f for f in images if f.name == selected_name), None)

card_text = st.text_area("Text für die Bildkarte", value="Danke für eure liebevollen Karten!\nIhr seid grossartig. 💫", height=100)

col1, col2, col3 = st.columns(3)
with col1:
    card_w = st.number_input("Breite", value=1200, min_value=600, step=50)
with col2:
    card_h = st.number_input("Höhe", value=1600, min_value=800, step=50)
with col3:
    margin = st.number_input("Rand (px)", value=60, min_value=20, step=5)

# Helper: draw wrapped text

def draw_wrapped(draw, text, box, font):
    x0, y0, x1, y1 = box
    max_width = x1 - x0
    # Estimate wrap width based on font size
    est_chars = max(10, int(max_width / (font.size * 0.55)))
    lines = []
    for para in text.split("\n"):
        lines += textwrap.wrap(para, width=est_chars) or [""]
    y = y0
    for line in lines:
        w, h = draw.textbbox((0, 0), line, font=font)[2:]
        draw.text((x0, y), line, fill=(255, 255, 255), font=font)
        y += h + 8

if st.button("🖼️ Karte erzeugen"):
    # Background
    if bg_choice:
        bg_img = Image.open(bg_choice).convert("RGB")
        bg_img = bg_img.resize((card_w, card_h))
        canvas = bg_img
        overlay = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 120))  # darken for readability
        canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay)
        canvas = canvas.convert("RGB")
    else:
        # gradient background
        canvas = Image.new("RGB", (card_w, card_h), (38, 38, 58))
        grad = Image.new("RGB", (1, card_h), 0)
        for y in range(card_h):
            c = int(38 + (y / card_h) * 40)
            grad.putpixel((0, y), (c, c, c + 10))
        grad = grad.resize((card_w, card_h))
        canvas.paste(grad, (0, 0))

    draw = ImageDraw.Draw(canvas)

    # Fonts: use default PIL font if no TTF is available on host
    try:
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", size=64)
        body_font = ImageFont.truetype("DejaVuSans.ttf", size=44)
    except Exception:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()

    # Header
    title_text = "Danke!"
    tw, th = draw.textbbox((0, 0), title_text, font=title_font)[2:]
    draw.text(((card_w - tw) // 2, margin), title_text, fill=(255, 255, 255), font=title_font)

    # Body box
    box = (margin, margin + th + 30, card_w - margin, card_h - margin)
    draw_wrapped(draw, card_text, box, body_font)

    buf = io.BytesIO()
    canvas.save(buf, format="PNG")
    data = buf.getvalue()
    st.image(data, caption="Vorschau", use_container_width=True)
    st.download_button("PNG herunterladen", data=data, file_name="danke_karte.png", mime="image/png")

st.markdown("---")
st.caption("Tipp: Teile diese Seite per Link oder generiere pro Person direkt eine WhatsApp‑Nachricht oben in Abschnitt 4.")
