#Abhishek Palase
# Simple Laptop Troubleshooting Expert System (Streamlit)

import streamlit as st

st.set_page_config(page_title="Laptop Troubleshooter", layout="centered")
st.title("💻 Laptop / Computer Troubleshooting System")
st.write("Select the problem you're facing below:")

# Problem selection
problem = st.radio(
    "Choose a problem:",
    ["Slow Performance", "No Display", "Overheating", "Booting Issue", "WiFi Problem"]
)

# Helper function for Yes/No
def ask(question):
    return st.radio(question, ["Yes", "No"])

# -------- Slow Performance --------
if problem == "Slow Performance":
    st.subheader("🧠 Slow Performance")
    q1 = ask("Is your CPU/Disk usage very high?")
    q2 = ask("Did you install new heavy software recently?")
    q3 = ask("Are you using a Hard Disk (HDD) instead of SSD?")
    if st.button("Get Verdict"):
        st.subheader("🔍 Result")
        if (q1, q2, q3) == ("Yes", "No", "Yes"):
            st.error("Cause: Slow HDD.\n\nSolution: Upgrade to SSD for better speed.")
        elif (q1, q2, q3) == ("Yes", "Yes", "No"):
            st.warning("Cause: Heavy background software.\n\nSolution: Close unwanted apps and disable startup programs.")
        else:
            st.info("Cause: System clutter or malware.\n\nSolution: Run virus scan and clean temporary files.")

# -------- No Display --------
elif problem == "No Display":
    st.subheader("🖥️ No Display")
    q1 = ask("Does the laptop power on (lights/fans start)?")
    q2 = ask("Do you hear any beeps on startup?")
    q3 = ask("Does an external monitor show display?")
    if st.button("Get Verdict"):
        st.subheader("🔍 Result")
        if (q1, q2, q3) == ("No", "No", "No"):
            st.error("Cause: Power issue.\n\nSolution: Check charger, battery, and power cable.")
        elif (q1, q2, q3) == ("Yes", "Yes", "No"):
            st.warning("Cause: RAM or motherboard issue.\n\nSolution: Reseat RAM or contact service center.")
        else:
            st.info("Cause: Screen or cable fault.\n\nSolution: Repair or replace internal display.")

# -------- Overheating --------
elif problem == "Overheating":
    st.subheader("🔥 Overheating")
    q1 = ask("Is the fan running loudly or constantly?")
    q2 = ask("Do you use the laptop on soft surfaces?")
    q3 = ask("Have you cleaned air vents or fan recently?")
    if st.button("Get Verdict"):
        st.subheader("🔍 Result")
        if (q1, q2, q3) == ("Yes", "Yes", "No"):
            st.error("Cause: Blocked airflow and dust.\n\nSolution: Clean vents and use on a flat surface.")
        elif (q1, q2, q3) == ("Yes", "No", "No"):
            st.warning("Cause: Poor cooling.\n\nSolution: Reapply thermal paste or service cooling fan.")
        else:
            st.info("Cause: Mild heat.\n\nSolution: Keep vents clear and ensure proper airflow.")

# -------- Booting Issue --------
elif problem == "Booting Issue":
    st.subheader("⚙️ Booting Issue")
    q1 = ask("Does your laptop reach the BIOS screen?")
    q2 = ask("Do you see the Windows logo or OS loading?")
    q3 = ask("Did you recently update BIOS or OS?")
    if st.button("Get Verdict"):
        st.subheader("🔍 Result")
        if (q1, q2, q3) == ("No", "No", "Yes"):
            st.error("Cause: BIOS corruption.\n\nSolution: Perform BIOS recovery or rollback update.")
        elif (q1, q2, q3) == ("Yes", "No", "No"):
            st.warning("Cause: Corrupted OS.\n\nSolution: Run startup repair or reinstall OS.")
        else:
            st.info("Cause: Slow boot settings.\n\nSolution: Disable extra startup apps.")

# -------- WiFi Problem --------
elif problem == "WiFi Problem":
    st.subheader("📶 WiFi Problem")
    q1 = ask("Can other devices connect to the same WiFi network?")
    q2 = ask("Does your laptop detect WiFi networks?")
    q3 = ask("Have you updated WiFi drivers recently?")
    if st.button("Get Verdict"):
        st.subheader("🔍 Result")
        if (q1, q2, q3) == ("No", "Yes", "Yes"):
            st.error("Cause: Router/network issue.\n\nSolution: Restart router and check ISP.")
        elif (q1, q2, q3) == ("Yes", "No", "No"):
            st.warning("Cause: WiFi adapter problem.\n\nSolution: Update or reinstall drivers.")
        else:
            st.info("Cause: Network configuration issue.\n\nSolution: Reset WiFi settings and reconnect.")

st.markdown("---")
st.caption("Made by Abhishek Palase")
