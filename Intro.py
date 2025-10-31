import streamlit as st
from PIL import Image

# ==============================
# CONFIGURACIÓN GENERAL
# ==============================
st.set_page_config(page_title="🌊 Aplicaciones IA - Tema Oceánico", page_icon="🐚", layout="wide")

# ==============================
# ESTILOS DE LA PÁGINA (Tema marino)
# ==============================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #a3d5e0 0%, #0077b6 100%);
    color: #022b3a;
    font-family: 'Arial', sans-serif;
}
h1, h2, h3, h4 {
    color: #012a4a !important;
    text-align: center;
}
.card {
    border: 2px solid #00b4d8;
    border-radius: 15px;
    padding: 15px;
    background-color: #f0fbff;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    text-align: center;
    transition: transform 0.2s ease-in-out;
}
.card:hover {
    transform: scale(1.03);
    box-shadow: 0 6px 14px rgba(0,0,0,0.2);
}
.card img {
    border-radius: 10px;
    width: 100%;
    height: 180px;
    object-fit: cover;
}
a {
    color: #0077b6 !important;
    font-weight: bold;
    text-decoration: none;
}
a:hover {
    color: #00b4d8 !important;
    text-decoration: underline;
}
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #caf0f8 0%, #0096c7 100%);
    color: #012a4a;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# SIDEBAR
# ==============================
with st.sidebar:
    st.subheader("🐠 Aplicaciones con Inteligencia Artificial")
    st.write("""
    Explora distintas herramientas impulsadas por IA en un entorno visual marino 🌐.
    """)
    st.markdown("[🔗 Enlace general al sitio](https://sites.google.com/view/aplicacionesdeia/inicio)")

# ==============================
# TÍTULO PRINCIPAL
# ==============================
st.title("🌊 Aplicaciones de Inteligencia Artificial")
st.markdown("### Explora diferentes herramientas tecnológicas con estilo oceánico 🐚")

# ==============================
# DATOS DE TARJETAS
# ==============================
titles = [
    "ChatGPT", "DALL·E", "Copilot",
    "Runway", "Midjourney", "Soundful",
    "Grammarly", "DeepL", "Synthesia",
    "Pictory", "Fireflies", "Murf",
    "Descript", "Leonardo AI", "Replit Ghostwriter"
]

images = [
    "img/chatgpt.png", "img/dalle.png", "img/copilot.png",
    "img/runway.png", "img/midjourney.png", "img/soundful.png",
    "img/grammarly.png", "img/deepl.png", "img/synthesia.png",
    "img/pictory.png", "img/fireflies.png", "img/murf.png",
    "img/descript.png", "img/leonardo.png", "img/replit.png"
]

codes = [
    "https://chat.openai.com/", "https://openai.com/dall-e", "https://github.com/features/copilot",
    "https://runwayml.com/", "https://www.midjourney.com/", "https://soundful.com/",
    "https://www.grammarly.com/", "https://www.deepl.com/translator", "https://www.synthesia.io/",
    "https://pictory.ai/", "https://fireflies.ai/", "https://murf.ai/",
    "https://www.descript.com/", "https://leonardo.ai/", "https://replit.com/"
]

# ==============================
# CREAR TARJETAS EN 5 FILAS (3 POR FILA)
# ==============================
index = 0
for fila in range(5):
    col1, col2, col3 = st.columns(3)
    for col in [col1, col2, col3]:
        if index < len(titles):
            with col:
                st.markdown(
                    f"""
                    <div class="card">
                        <h4>{titles[index]}</h4>
                        <img src="{images[index]}" alt="{titles[index]}">
                        <br><br>
                        <a href="{codes[index]}" target="_blank">🌐 Ir al sitio</a>
                    </div>
                    """, unsafe_allow_html=True
                )
            index += 1
