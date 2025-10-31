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
    st.subheader("🐠 Portafolio Multimodales")
    st.write("""
    .
    """)

# ==============================
# TÍTULO PRINCIPAL
# ==============================
st.title("🌊  Portafolio Multimodales")

# ==============================
# DATOS DE TARJETAS
# ==============================
titles = [
    "Intro", "Tezto a voz", "Reconocimiento de Texto en Imágenes",
    "Traductor", "Analisis ENG", "Analisis Sentimientos",
    "Analizador de Texto ESP", "Detección de Objetos", "Chat PDF",
    "Análisis de Imagen", "Reconocimiento de Dígitos", "Tablero Oceánico Inteligente",
    "CONTROL POR VOZ", "ector de Sensor MQTT", "MQTT Control"
]

images = [
    "image_2025-10-31_024804638.png", "image_2025-10-31_024828456.png", "image_2025-10-31_024840470.png",
    "image_2025-10-31_024857834.png", "image_2025-10-31_024932307.png, "image_2025-10-31_024951539.png",
    "image_2025-10-31_025008782.png", "image_2025-10-31_025044312.png", "image_2025-10-31_025100531.png",
    "image_2025-10-31_025120114.png", "image_2025-10-31_025139338.png", "image_2025-10-31_025210860.png",
    "image_2025-10-31_025230111.png", "image_2025-10-31_025253076.png", "image_2025-10-31_025330730.png"
]

codes = [
    "https://intro1phio.streamlit.app", "https://cuentovoz.streamlit.app", "https://intro1phio.streamlit.app",
    "https://voz-txt-traductor.streamlit.app", "https://gestosap.streamlit.app", "https://tenlengl.streamlit.app",
    "https://anaisistexto.streamlit.app", "https://chatpdfphio.streamlit.app", "https://visionapphio.streamlit.app",
    "https://handwv1dibujo.streamlit.app", "https://drawrecogv2.streamlit.app", "https://drawrecogv2.streamlit.app",
    "https://ctrlvoicephio.streamlit.app", "https://recepmqttphio.streamlit.app", "https://sendcmqttphio.streamlit.app"
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
