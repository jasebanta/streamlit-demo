import streamlit as st
import pandas as pd
import sys, os
print("Current working directory:", os.getcwd())
print("Python path:", sys.path)
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from backend.data import SampleData


st.set_page_config(
    layout="wide"
)
st.title("Consent Management Visual")

st.divider() #--------------------------------------------
@st.cache_data
def generate_synthetic_data():
    sd = SampleData(10)
    df_demo = sd.df_demo
    df_health = sd.df_health
    return (df_demo, df_health)

with st.expander("Oganization 1 Data"):
    st.write("Synthetic Demogrpahic Data")
    df_demo, df_health = generate_synthetic_data()
    edited_demo = st.data_editor(df_demo, key="org1_demo")

    st.write("Synthetic Health Data")
    edited_health = st.data_editor(df_health, key="org1_health")

with st.expander("Oganization 2 Data"):
    st.write("Synthetic Demogrpahic Data")
    df_demo, df_health = generate_synthetic_data()
    edited_demo = st.data_editor(df_demo, key="org2_demo")

    st.write("Synthetic Health Data")
    edited_health = st.data_editor(df_health, key="org2_health")

st.divider() #--------------------------------------------

st.header("Organization 1 Consent")

# Define categories and items with their pill options
categories = {
    "Demographic Data": {
        "person_id": ["Value", "Masked"],
        "first_name": ["Value", "Masked"],
        "last_name": ["Value", "Masked"],
        "dob": ["Value", "Masked"],
        "ssn": ["Value", "Masked"],
        "gender": ["Value", "Masked"],
        "ethnicity": ["Value", "Masked"],
        "phone": ["Value", "Masked"],
        "email": ["Value", "Masked"],
        "record_created_dt": ["Value", "Masked"],
        "consent": ["Value", "Masked"]
    },
    "Health Data": {
        "person_id": ["Value", "Masked"], 
        "allergy": ["Value", "Masked"], 
        "substance_abuse": ["Value", "Masked"], 
        "blood_pressure": ["Value", "Masked"], 
        "cholesterol": ["Value", "Masked"], 
        "heart_disease": ["Value", "Masked"], 
        "diabetes": ["Value", "Masked"], 
        "bmi": ["Value", "Masked"], 
        "smoker": ["Value", "Masked"], 
        "exercise_freq": ["Value", "Masked"], 
        "sleep_hours": ["Value", "Masked"]
    }
}

partners = ["Organization 1", "Organization 2", "partner 3"]

# Initialize session state for each category
org = ["org1" "org2"]
for category, items in categories.items():
    if f"selected_{category}" not in st.session_state:
        st.session_state[f"selected_{category}"] = {item: False for item in items}
    if f"select_all_{category}" not in st.session_state:
        st.session_state[f"select_all_{category}"] = False
    if f"pills_{category}" not in st.session_state:
        st.session_state[f"pills_{category}"] = {item: [] for item in items}
    if f"multi_{category}" not in st.session_state:
        st.session_state[f"multi_{category}"] = {item: [] for item in items}

# Callback to handle "Select All" toggle
def toggle_select_all(category):
    all_selected = not st.session_state[f"select_all_{category}"]
    st.session_state[f"select_all_{category}"] = all_selected
    for item in categories[category]:
        st.session_state[f"selected_{category}"][item] = all_selected

for category, items in categories.items():
    with st.expander(category, expanded=False):
        # "Select All" checkbox
        select_all = st.checkbox(
            f"Select All {category}",
            value=st.session_state[f"select_all_{category}"],
            key=f"select_all_checkbox_{category}",
            on_change=toggle_select_all,
            args=(category,)
        )

        # Individual item checkboxes with pills appearing immediately
        for item in items:
            cols = st.columns([0.2, 0.2, 0.6])  # Indent the pills
            with cols[0]:  # Checkbox column
                st.session_state[f"selected_{category}"][item] = st.checkbox(
                    item,
                    value=st.session_state[f"selected_{category}"][item],
                    key=f"{category}_{item}"
                )
            if st.session_state[f"selected_{category}"][item]:  # Show pills only if selected
                with cols[1]:  # Indented pills column
                    st.session_state[f"pills_{category}"][item] = st.pills(
                        label=f"Select {item} types",
                        options=categories[category][item],
                        selection_mode="single",
                        default=categories[category][item][0],
                        key=f"pills_{category}_{item}"
                    )
                    with cols[2]:
                        st.session_state[f"multi_{category}"][item] = st.multiselect(
                            label=f"Select {item} to share with",
                            options=partners,
                            default=partners,
                            key=f"multi_{category}_{item}"
                        )

# Display selected items
selected_items = {
    category: {
        item: {
            "masking": st.session_state[f"pills_{category}"][item],  # Masking choice
            "shared_with": st.session_state[f"multi_{category}"][item]  # Selected partners
        }
        for item, selected in st.session_state[f"selected_{category}"].items() if selected
    }
    for category in categories
}
st.divider() #--------------------------------------------
st.header("Organization 2 Consent")

st.divider() #--------------------------------------------
st.header("Consent Storage")
# Show selected items
st.write("Organization consent values to be stored in a NoSQL db using key-value and document data model.")
cs = st.columns([0.5, 0.5])
with cs[0]:
    st.write("Org 1 consent record:")
    st.json(selected_items)
with cs[1]:
    st.write("Org 2 consent record:")
st.divider() #--------------------------------------------
st.header("End User View")

# Filtered DataFrame for End User View
def filter_and_mask_data(df, category_name):
    """Filters dataframe to include only selected fields and applies masking if needed."""
    selected_fields = selected_items.get(category_name, {})

    if not selected_fields:  # If nothing was selected, return an empty DataFrame with same columns
        return pd.DataFrame(columns=df.columns)

    filtered_df = df.copy()

    for col in df.columns:
        if col in selected_fields:
            # Check if the column should be masked
            if "Masked" in selected_fields[col]:
                filtered_df[col] = "######"  # Mask values
        else:
            filtered_df.drop(columns=[col], inplace=True)  # Drop unselected columns

    return filtered_df


# Apply the filtering and masking for demographic data
df_demo_filtered = filter_and_mask_data(edited_demo, "Demographic Data")

# Ensure only rows where 'consent' == True in df_demo
if "consent" in edited_demo.columns:
    df_demo_filtered = df_demo_filtered[edited_demo["consent"] == True]

# Apply filtering for health data, linking with person_id from df_demo
df_health_filtered = filter_and_mask_data(edited_health, "Health Data")

if "consent" in edited_health.columns:
    df_health_filtered = df_health_filtered[edited_health["consent"] == True]

# Display the transformed views
with st.expander("Oganization 1 Data"):
    st.write("### Demographic Data (End User View)")
    st.dataframe(df_demo_filtered)

    st.write("### Health Data (End User View)")
    st.dataframe(df_health_filtered)

# Add individual consent flow
