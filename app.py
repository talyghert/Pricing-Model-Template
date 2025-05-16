import streamlit as st

# ---------- Page Configuration ----------
st.set_page_config(page_title="Management Fee Calculator", page_icon="📊", layout="centered")

# ---------- Helper Functions ----------
def get_base_cost(model_type, property_type):
    model_type = model_type.lower()
    property_type = property_type.lower()

    if model_type == "city-sited":
        return 30
    elif model_type == "city-unsited":
        return 20
    elif model_type == "suburban":
        if property_type == "sited":
            return 20
        elif property_type == "portfolio":
            return 10
        else:
            raise ValueError("Invalid property type for suburban model.")
    else:
        raise ValueError("Invalid model type.")

def calculate_management_fee(model_type, property_type, unit_count):
    base_cost = get_base_cost(model_type, property_type)
    return unit_count * base_cost

# ---------- UI Layout ----------
st.title("📊 Management Fee Calculator")
st.markdown(
    """
    Use this simple tool to estimate the **target management fee** based on:
    - Property type (sited or portfolio)
    - Number of units
    - Pricing model (city or suburban)
    """
)

with st.form("fee_form"):
    st.subheader("📌 Input Details")

    col1, col2 = st.columns(2)
    with col1:
        model = st.selectbox("🏙️ Select Model Type", ["City-sited", "City-unsited", "Suburban"])
    with col2:
        property_type = st.selectbox("🏘️ Select Property Type", ["sited", "portfolio"])

    unit_count = st.number_input("🔢 Enter Unit Count", min_value=1, value=10, step=1)

    submitted = st.form_submit_button("💡 Calculate Management Fee")

# ---------- Result Section ----------
if submitted:
    try:
        fee = calculate_management_fee(model, property_type, unit_count)
        st.success(f"✅ **Target Management Fee**: `${fee:,.2f}`")
        st.caption("Calculation = unit count × base cost")
    except Exception as e:
        st.error(f"❌ Error: {e}")
