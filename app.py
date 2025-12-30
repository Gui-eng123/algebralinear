import os
import glob
import random
import streamlit as st
from PIL import Image

# ----------------------------
# Config
# ----------------------------
st.set_page_config(
    page_title="Surpresa 🎁",
    page_icon="🎉",
    layout="wide",
)

FOTOS_DIR = "fotos"

# ----------------------------
# CSS (estilo)
# ----------------------------
st.markdown(
    """
    <style>
      /* ===== PRIMEIRA TELA (BOTÃO) ===== */
      .center-wrap {
          min-height: 85vh;
          display: flex;
          align-items: center;
          justify-content: center;
          flex-direction: column;
          gap: 28px;
          text-align: center;
      }

      .primeira-tela-titulo {
          font-size: 3.2rem;
          font-weight: 900;
          margin: 0;
      }

      .primeira-tela-subtitulo {
          font-size: 1.6rem;
          opacity: 0.85;
          margin: 0;
      }

      .botao-surpresa button {
          font-size: 1.4rem !important;
          padding: 14px 32px !important;
          border-radius: 14px !important;
      }

      /* ===== TELA DE ANIVERSÁRIO ===== */
      .aniversario-container {
          min-height: 80vh;
          display: flex;
          justify-content: center;
          align-items: center;
      }

      .aniversario-card {
          text-align: center;
          padding: 40px 50px;
          border-radius: 24px;
          background: rgba(255, 255, 255, 0.06);
          border: 1px solid rgba(255,255,255,0.10);
          box-shadow: 0 0 40px rgba(255, 75, 145, 0.25);
      }

      .aniversario-titulo {
          font-size: 4rem;
          font-weight: 900;
          margin: 0 0 20px 0;
      }

      .aniversario-frase {
          font-size: 1.6rem;
          opacity: 0.9;
          margin: 0;
      }

      .photo-card {
          background: rgba(255,255,255,0.06);
          border: 1px solid rgba(255,255,255,0.10);
          padding: 12px;
          border-radius: 18px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# Estado (qual "tela" está)
# ----------------------------
if "revelado" not in st.session_state:
    st.session_state.revelado = False

if "frase" not in st.session_state:
    st.session_state.frase = None

# ----------------------------
# Funções auxiliares
# ----------------------------
def listar_fotos():
    exts = ("*.jpg", "*.jpeg", "*.png", "*.webp")
    paths = []
    for e in exts:
        paths.extend(glob.glob(os.path.join(FOTOS_DIR, e)))
    return sorted(paths)

def escolher_frase():
    frases = [
        "Nerd 🤓",
        "Cada frase tem 11,11% de chance de aparecer✨",
        "Quem gosta de álgebra linear?",
        "Frase easter egg, sortuda",
        "Safira está de desejando parabens",
        "Obrigado por existir na minha vida"
        "Felicidades para a sua vida",
        "Que Deus te proteja do desemprego",
        "Frase para preencher espaço",
    ]
    return random.choice(frases)

# ----------------------------
# Tela 1 / Tela 2 (controlado por estado)
# ----------------------------
if not st.session_state.revelado:
    # -------- Tela 1: botão central --------
    st.markdown(
        """
        <div class="center-wrap">
            <h1 class="primeira-tela-titulo"> Desafio do botão surpresa</h1>
            <p class="primeira-tela-subtitulo">Dúvido apertar no botão</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="botao-surpresa">', unsafe_allow_html=True)
    if st.button("BOTÃO ESCONDIDO "):
        st.session_state.revelado = True
        st.session_state.frase = escolher_frase()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # -------- Tela 2: mensagem + fotos --------
    st.markdown(
        f"""
        <div class="aniversario-container">
            <div class="aniversario-card">
                <h1 class="aniversario-titulo">🎉 Feliz Aniversário! 🎂</h1>
                <p class="aniversario-frase">{st.session_state.frase or ""}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    fotos = listar_fotos()

    if not fotos:
        st.warning("Não encontrei fotos na pasta `fotos/`. Coloque imagens (.jpg/.png/.webp) lá.")
    else:
        st.subheader("Fotos 🤓☝️")
        cols = st.columns(3)
        for i, path in enumerate(fotos):
            with cols[i % 3]:
                img = Image.open(path)
                st.markdown("<div class='photo-card'>", unsafe_allow_html=True)
                st.image(img, use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        if st.button("🔁 Ver de novo"):
            st.session_state.revelado = False
            st.rerun()
    with c2:
        if st.button("🎲 Troque sua frase genérica de parábens"):
            st.session_state.frase = escolher_frase()
            st.rerun()
    with c3:
        st.markdown(
            "<p style='text-align:right;opacity:0.75;margin-top:10px;'>Feito com carinho 💛</p>",
            unsafe_allow_html=True
        )
