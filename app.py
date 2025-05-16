import streamlit as st

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

st.title("📊 Management Fee Calculator")

model = st.selectbox("Select Model Type", ["City-sited", "City-unsited", "Suburban"])
property_type = st.selectbox("Select Property Type", ["sited", "portfolio"])
unit_count = st.number_input("Enter Unit Count", min_value=1, value=10)

if st.button("Calculate Management Fee"):
    try:
        fee = calculate_management_fee(model, property_type, unit_count)
        st.success(f"✅ Target Management Fee: ${fee:,.2f}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
