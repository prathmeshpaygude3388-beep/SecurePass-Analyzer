import streamlit as st

from attack_engine.strength_analyzer import analyze_password_strength
from attack_engine.breach_detector import check_breach
from attack_engine.crack_time_estimator import estimate_crack_time, format_time
from attack_engine.password_generator import generate_strong_password
from attack_engine.dictionary_attack import dictionary_attack
from attack_engine.brute_force import brute_force_attack


st.title("🔐 Password Security Analyzer")

password = st.text_input("Enter a password to evaluate:", type="password")

if password:

    result = analyze_password_strength(password)

    st.subheader("Security Report")

    st.write(f"**Length:** {result['length']}")
    st.write(f"**Strength:** {result['strength']}")
    # Strength Meter
result = analyze_password_strength(password)
strength = result['strength']

if strength == "WEAK":
    st.progress(0.25)
    st.error("Weak Password")

elif strength == "MODERATE":
    st.progress(0.60)
    st.warning("Moderate Password")

elif strength == "STRONG":
    st.progress(1.0)
    st.success("Strong Password")

# OUTSIDE the block
st.write(f"**Risk Level:** {result['risk_level']}")

    # Breach detection
if check_breach(password):
    st.error("⚠ This password has appeared in known data breaches!")
else:
    st.success("✅ This password was NOT found in known breaches.")

    # Crack time
seconds = estimate_crack_time(password)
st.write(f"**Estimated Crack Time:** {format_time(seconds)}")

    # Recommendations
if result['feedback']:
        st.warning("Recommendations:")
        for tip in result['feedback']:
            st.write(f"- {tip}")
else:
        st.success("Excellent password!")

    # Generator
st.subheader("Suggested Strong Password")
st.code(generate_strong_password(14), language="text")

st.subheader("⚔️ Attack Simulation")

if st.button("Simulate Attack"):

    st.write("Running dictionary attack...")

    dict_result = dictionary_attack(password)
    st.write(dict_result)

    st.write("Running brute force attack simulation...")

    brute_result = brute_force_attack(password, max_length=4)

    if brute_result:
        st.error("Password cracked via brute force!")
        st.write(brute_result)
    else:
        st.success("Brute force attack failed (password too strong).")


