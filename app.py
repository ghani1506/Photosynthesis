import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Ellipse
import numpy as np
import time

st.set_page_config(page_title="Photosynthesis Animation", page_icon="🌿", layout="wide")

st.title("🌿 Photosynthesis Animation")
st.write("A simple interactive animation showing how plants use sunlight, carbon dioxide, and water to make glucose and oxygen.")

# Sidebar controls
st.sidebar.header("Animation Controls")
speed = st.sidebar.slider("Animation speed", 0.02, 0.20, 0.07, 0.01)
show_labels = st.sidebar.checkbox("Show labels", True)
show_equation = st.sidebar.checkbox("Show photosynthesis equation", True)

if show_equation:
    st.info("Photosynthesis equation: 6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂")

col1, col2 = st.columns([3, 1])

with col2:
    st.subheader("What happens?")
    st.markdown(
        """
        1. **Sunlight** is absorbed by leaves.
        2. **Carbon dioxide** enters through tiny pores called stomata.
        3. **Water** travels from roots to leaves.
        4. In the leaf, the plant makes **glucose**.
        5. **Oxygen** is released into the air.
        """
    )

with col1:
    placeholder = st.empty()

    run = st.button("▶️ Play Animation")

    def draw_scene(frame):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.axis("off")

        # Sky and ground
        ax.add_patch(Rectangle((0, 0), 10, 7, alpha=0.08))
        ax.add_patch(Rectangle((0, 0), 10, 1, alpha=0.25))

        # Sun
        sun_x, sun_y = 1.2, 6.0
        ax.add_patch(Circle((sun_x, sun_y), 0.55, alpha=0.75))
        for angle in np.linspace(0, 2 * np.pi, 12, endpoint=False):
            ax.plot(
                [sun_x + 0.75 * np.cos(angle), sun_x + 1.05 * np.cos(angle)],
                [sun_y + 0.75 * np.sin(angle), sun_y + 1.05 * np.sin(angle)],
                linewidth=2,
            )

        # Plant stem
        ax.plot([5, 5], [1, 4], linewidth=8)

        # Leaves
        left_leaf = Ellipse((4.35, 3.6), 1.7, 0.75, angle=25, alpha=0.7)
        right_leaf = Ellipse((5.75, 3.25), 1.9, 0.8, angle=-25, alpha=0.7)
        ax.add_patch(left_leaf)
        ax.add_patch(right_leaf)

        # Roots
        ax.plot([5, 4.4], [1, 0.35], linewidth=3)
        ax.plot([5, 5.6], [1, 0.35], linewidth=3)
        ax.plot([5, 5], [1, 0.25], linewidth=3)

        # Water drops moving upward
        for i in range(5):
            y = 0.45 + ((frame * 0.08 + i * 0.7) % 3.6)
            ax.text(4.75, y, "💧", fontsize=18, ha="center")

        # CO2 bubbles moving toward leaf
        for i in range(4):
            x = 9.2 - ((frame * 0.10 + i * 0.9) % 4.0)
            y = 4.5 - i * 0.35
            ax.text(x, y, "CO₂", fontsize=13, ha="center")
            ax.add_patch(FancyArrowPatch((x - 0.15, y - 0.05), (5.8, 3.5), arrowstyle="->", mutation_scale=12))

        # Sunlight arrows moving to leaf
        for i in range(5):
            offset = ((frame * 0.08 + i * 0.45) % 2.2)
            start = (2.0 + offset, 5.7 - i * 0.25)
            end = (4.4 + offset * 0.15, 3.8 - i * 0.12)
            ax.add_patch(FancyArrowPatch(start, end, arrowstyle="->", mutation_scale=18, linewidth=2))

        # Oxygen released
        for i in range(4):
            y = 3.8 + ((frame * 0.09 + i * 0.6) % 2.4)
            x = 5.5 + i * 0.28
            ax.text(x, y, "O₂", fontsize=13, ha="center")
            ax.add_patch(FancyArrowPatch((5.55, 3.65), (x, y), arrowstyle="->", mutation_scale=12))

        # Glucose product in leaf
        pulse = 14 + int(5 * np.sin(frame * 0.25))
        ax.text(5.0, 3.45, "C₆H₁₂O₆", fontsize=pulse, ha="center", weight="bold")

        if show_labels:
            ax.text(1.2, 5.15, "Sunlight", fontsize=12, ha="center", weight="bold")
            ax.text(8.3, 5.0, "Carbon dioxide enters", fontsize=12, ha="center")
            ax.text(3.5, 0.45, "Water absorbed by roots", fontsize=12, ha="center")
            ax.text(6.9, 6.35, "Oxygen released", fontsize=12, ha="center")
            ax.text(5.0, 2.45, "Glucose made in the leaf", fontsize=12, ha="center")

        return fig

    if run:
        for frame in range(120):
            fig = draw_scene(frame)
            placeholder.pyplot(fig)
            plt.close(fig)
            time.sleep(speed)
    else:
        fig = draw_scene(0)
        placeholder.pyplot(fig)
        plt.close(fig)

st.divider()
st.subheader("Classroom Use")
st.write("Ask students to identify the inputs and outputs of photosynthesis, then explain the role of the leaf, roots, and sunlight.")
