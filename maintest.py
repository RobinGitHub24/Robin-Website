import streamlit as st
from PIL import Image
import time

# ----- Seiteneinstellungen -----
st.set_page_config(page_title="Über mich", page_icon="👋", layout="centered")

# ----- Header / Profilbild -----
st.title("Robin Schäfer")



bild = Image.open("titelbild.jpg") 
st.image(bild, width=150)

# ----- Über mich -----
st.subheader(" Über mich")

st.markdown("""


Ich studiere aktuell Wirtschaftsinformatik und verknüpfe damit meine Begeisterung für IT mit einem fundierten betriebswirtschaftlichen Verständnis.
Als Werkstudent bei der Wolfgang Steubing AG sammle ich praktische Erfahrungen im Finanzsektor und bringe mein Wissen direkt in reale Projekte ein. 
In meiner Rolle bin ich vor allem an der Schnittstelle zwischen IT und Geschäftsprozessen tätig, wo ich meine technische Expertise gezielt mit betriebswirtschaftlichem Denken verbinde.

""")

# ----- Kontaktbereich -----

st.markdown("---")  # Trennerlinie

st.header("📫 Kontakt & Anfragen")
st.write("Du möchtest mit mir in Kontakt treten oder hast eine Anfrage? Ich freue mich auf deine Nachricht!")

st.write("📧 **E-Mail:** robin.schaefer1@outlook.de")
st.markdown("🔗 **LinkedIn:** [Robin Schäfer](https://linkedin.com/in/robin-schäfer-55b185296)")

