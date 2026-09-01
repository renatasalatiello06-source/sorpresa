import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Una sorpresa per te ❤️", page_icon="❤️", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown("### --- Un piccolo quiz per sbloccare la sorpresa ---")

tentativo = st.text_input(
    "come diciamo per sempre?"
)
risposta_segreta = "ei ei"

if tentativo:
    if tentativo.strip().lower() == risposta_segreta:
        st.success("Esatto! ❤️ Ecco la sorpresa per te.")

        t = np.linspace(0, 2 * np.pi, 100)
        x = 16 * np.sin(t) ** 3
        y = (
            13 * np.cos(t)
            - 5 * np.cos(2 * t)
            - 2 * np.cos(3 * t)
            - np.cos(4 * t)
        )

        fig, ax = plt.subplots(figsize=(6, 6))
        fig.patch.set_facecolor("#0e1117")
        ax.set_facecolor("#0e1117")
        ax.plot(x, y, color="#ff4d6d", linewidth=2, linestyle="--", alpha=0.7)
        ax.scatter(x, y, color="#ff758f", s=50, edgecolor="white", zorder=3)
        ax.set_title(
            "Ti amo ❤️", fontsize=18, color="#ff4d6d", pad=20, fontweight="bold"
        )
        ax.axis("equal")
        ax.axis("off")

        st.pyplot(fig)
    else:
        st.error("Ops, risposta sbagliata! Riprova 💔")