import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Photosynthesis Animation", page_icon="🌿", layout="wide")

st.title("🌿 Photosynthesis Animation")
st.write("A simple interactive animation showing how a real plant uses sunlight, carbon dioxide, and water to produce glucose and oxygen.")

speed = st.slider("Animation speed", 4, 16, 9)
show_labels = st.checkbox("Show labels", value=True)

labels_display = "block" if show_labels else "none"

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
  body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(#dff6ff, #eaf9e3);
  }}
  .scene {{
    position: relative;
    width: 100%;
    height: 690px;
    overflow: hidden;
    border-radius: 22px;
    background: linear-gradient(#cdefff 0%, #e8f8ff 48%, #d9f2c7 49%, #a6d678 100%);
    box-shadow: inset 0 0 30px rgba(0,0,0,0.08);
  }}
  .sun {{
    position: absolute;
    top: 35px;
    left: 55px;
    width: 115px;
    height: 115px;
    border-radius: 50%;
    background: radial-gradient(circle, #fff7a8 20%, #ffd84d 65%, #ffb300 100%);
    box-shadow: 0 0 45px #ffd84d;
    animation: pulse 2.2s infinite alternate;
  }}
  @keyframes pulse {{ from {{ transform: scale(1); }} to {{ transform: scale(1.08); }} }}

  .plant-photo {{
    position: absolute;
    left: 50%;
    top: 115px;
    transform: translateX(-50%);
    width: 430px;
    height: 500px;
    object-fit: contain;
    filter: drop-shadow(0 16px 18px rgba(0,0,0,0.25));
    z-index: 4;
  }}
  .soil {{
    position: absolute;
    bottom: 36px;
    left: 50%;
    transform: translateX(-50%);
    width: 600px;
    height: 95px;
    border-radius: 50%;
    background: radial-gradient(ellipse at center, #7b4a24 0%, #4d2f18 80%);
    z-index: 2;
  }}

  svg {{ position:absolute; inset:0; z-index:5; pointer-events:none; }}
  .arrow {{
    fill: none;
    stroke-width: 5;
    stroke-linecap: round;
    stroke-dasharray: 14 12;
    animation: dash {speed}s linear infinite;
  }}
  @keyframes dash {{ to {{ stroke-dashoffset: -260; }} }}

  .sunlight {{ stroke: #ffba08; }}
  .co2 {{ stroke: #3a86ff; }}
  .water {{ stroke: #00a6fb; }}
  .oxygen {{ stroke: #06d6a0; }}
  .glucose {{ stroke: #ef476f; }}

  .label {{
    display: {labels_display};
    position: absolute;
    padding: 9px 13px;
    border-radius: 14px;
    background: rgba(255,255,255,0.92);
    font-weight: bold;
    font-size: 18px;
    box-shadow: 0 5px 12px rgba(0,0,0,0.13);
    z-index: 8;
    white-space: nowrap;
  }}
  .l-sun {{ top: 155px; left: 100px; color:#b97900; }}
  .l-co2 {{ top: 270px; right: 85px; color:#1d5fbf; }}
  .l-water {{ bottom: 105px; left: 170px; color:#0077b6; }}
  .l-oxygen {{ top: 140px; right: 155px; color:#058c6f; }}
  .l-glucose {{ bottom: 145px; right: 150px; color:#c9184a; }}

  .formula {{
    position: absolute;
    left: 50%;
    bottom: 13px;
    transform: translateX(-50%);
    background: rgba(255,255,255,0.95);
    padding: 13px 20px;
    border-radius: 18px;
    font-size: 22px;
    font-weight: bold;
    z-index: 10;
    box-shadow: 0 6px 16px rgba(0,0,0,0.16);
  }}
  .note {{
    position: absolute;
    left: 28px;
    bottom: 112px;
    width: 260px;
    background: rgba(255,255,255,0.88);
    padding: 14px;
    border-radius: 16px;
    font-size: 16px;
    line-height: 1.4;
    z-index: 9;
  }}
</style>
</head>
<body>
<div class="scene">
  <div class="sun"></div>
  <div class="soil"></div>

  <!-- Real plant photo from Wikimedia Commons -->
  <img class="plant-photo" src="assets/plant.png" alt="Real plant">

  <svg viewBox="0 0 1200 690" preserveAspectRatio="none">
    <defs>
      <marker id="arrowSun" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#ffba08"/></marker>
      <marker id="arrowCO2" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#3a86ff"/></marker>
      <marker id="arrowWater" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#00a6fb"/></marker>
      <marker id="arrowOxy" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#06d6a0"/></marker>
      <marker id="arrowGlu" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#ef476f"/></marker>
    </defs>

    <!-- Non-overlapping routes -->
    <path class="arrow sunlight" marker-end="url(#arrowSun)" d="M135 110 C260 135, 335 170, 455 245" />
    <path class="arrow co2" marker-end="url(#arrowCO2)" d="M1080 300 C960 275, 850 262, 720 292" />
    <path class="arrow water" marker-end="url(#arrowWater)" d="M240 585 C350 550, 430 520, 540 475" />
    <path class="arrow oxygen" marker-end="url(#arrowOxy)" d="M705 205 C820 140, 930 115, 1060 105" />
    <path class="arrow glucose" marker-end="url(#arrowGlu)" d="M690 450 C810 475, 930 520, 1035 585" />
  </svg>

  <div class="label l-sun">☀️ Sunlight in</div>
  <div class="label l-co2">CO₂ enters leaves</div>
  <div class="label l-water">💧 Water from roots</div>
  <div class="label l-oxygen">O₂ released</div>
  <div class="label l-glucose">Glucose made</div>

  <div class="note"><b>Key idea:</b><br>Leaves use chlorophyll to capture light energy. The plant changes water and carbon dioxide into glucose, then releases oxygen.</div>
  <div class="formula">6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂</div>
</div>
</body>
</html>
"""

components.html(html_code, height=720, scrolling=False)

st.subheader("How to deploy on GitHub + Streamlit")
st.markdown("""
1. Create a new GitHub repository.
2. Upload `app.py` and `requirements.txt`.
3. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
4. Choose your GitHub repository.
5. Set the main file path to `app.py`.
6. Click **Deploy**.
""")
