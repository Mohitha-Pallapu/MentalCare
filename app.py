import streamlit as st
import plotly.graph_objects as go

# Page Config

st.set_page_config(
    page_title="Mental Health Risk Checker",
    page_icon="🧠",
    layout="centered"
)

# Title

st.title("🧠 Mental Health Risk Analyzer")

st.info("🔒 Your responses are anonymous and not stored.")


# Helper — Colored Divider

def colored_divider(color):
    st.markdown(
        f"""
        <hr style="
            border: none;
            height: 4px;
            background-color: {color};
            margin: 25px 0;
            border-radius: 10px;
        ">
        """,
        unsafe_allow_html=True
    )


# Personal Info

st.subheader("👤 Personal Information")

age = st.slider("Age", 18, 60, 20)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)


# Lifestyle

st.subheader("😴 Lifestyle")

sleep_hours = st.slider(
    "Average Sleep Duration (hours)",
    0, 12, 7
)

study_hours = st.slider(
    "Daily Study / Work Hours",
    0, 16, 6
)

# Stress Factors

st.subheader("⚠ Stress Factors")

academic_pressure = st.selectbox(
    "Academic / Work Pressure",
    ["Low", "Medium", "High"]
)

financial_stress = st.selectbox(
    "Financial Stress",
    ["Low", "Medium", "High"]
)

family_history = st.selectbox(
    "Family history of mental illness?",
    ["No", "Yes"]
)

# Risk Calculation

def calculate_risk():
    score = 0
    reasons = []

    # Sleep
    if sleep_hours < 5:
        score += 3
        reasons.append("Very low sleep duration")
    elif sleep_hours < 6:
        score += 2
        reasons.append("Low sleep duration")

    # Pressure
    if academic_pressure == "Medium":
        score += 2
        reasons.append("Moderate work pressure")
    elif academic_pressure == "High":
        score += 4
        reasons.append("High work pressure")

    # Work hours
    if study_hours > 10:
        score += 3
        reasons.append("Very long work hours")
    elif study_hours > 8:
        score += 2
        reasons.append("Long work hours")

    # Financial stress
    if financial_stress == "Medium":
        score += 2
        reasons.append("Financial stress")
    elif financial_stress == "High":
        score += 4
        reasons.append("High financial stress")

    # Family history
    if family_history == "Yes":
        score += 3
        reasons.append("Family history of mental illness")

    # Age factor
    if age < 25:
        score += 1

    risk_prob = min(score / 15, 1)

    return risk_prob, reasons


# Analyze Button

if st.button("🔍 Analyze My Mental Health Risk", use_container_width=True):

    risk_prob, reasons = calculate_risk()

    # Risk Level Color + Label

    if risk_prob < 0.3:
        color = "#00C853"   # GREEN
        label = "🟢 LOW RISK"
    elif risk_prob < 0.6:
        color = "#FFA000"   # AMBER / ORANGE
        label = "🟡 MODERATE RISK"
    else:
        color = "#D50000"   # RED
        label = "🔴 HIGH RISK"

    # Divider

    colored_divider(color)

    # Gauge Chart

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_prob * 100,
        title={'text': "Risk Score (%)"},
        gauge={
            'axis': {'range': [0, 100]},

            # ⭐ FILLED ARC COLOR — changes with risk
            'bar': {'color': color},

            # ⭐ Light background zones
            'steps': [
                {'range': [0, 30], 'color': "#E8F5E9"},
                {'range': [30, 60], 'color': "#FFF8E1"},
                {'range': [60, 100], 'color': "#FFEBEE"}
            ],
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    # Risk Badge

    st.markdown(
        f"""
        <div style="
            background-color: {color};
            padding: 14px;
            border-radius: 12px;
            text-align: center;
            font-weight: bold;
            font-size: 20px;
            color: white;
            margin: 10px 0;
        ">
            {label}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Explainable Factors

    st.subheader("📊 What influenced your result")

    if reasons:
        for r in reasons:
            st.write(f"• {r}")
    else:
        st.write("No major risk factors detected.")

    # Personalized Recommendations

    st.subheader("💡 Recommendations")

    if risk_prob < 0.3:
        st.write("✔ Maintain your current healthy lifestyle.")
        st.write("✔ Continue good sleep and stress management.")

    elif risk_prob < 0.6:
        st.write("✔ Improve sleep quality and work-life balance.")
        st.write("✔ Practice relaxation techniques.")
        st.write("✔ Talk to trusted people if feeling stressed.")

    else:
        st.write("✔ Consider speaking with a mental health professional.")
        st.write("✔ Reduce workload if possible.")
        st.write("✔ Seek social support.")
        st.write("✔ If in distress, contact local helplines.")
