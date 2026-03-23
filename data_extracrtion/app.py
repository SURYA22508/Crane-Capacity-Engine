import pandas as pd
import streamlit as st
import numpy as np
import pickle

st.set_page_config(layout="wide")

data = pd.read_csv("upto1000.csv")
data1 = pd.read_csv("upto2000 (2).csv")
data2 = pd.read_csv("upto2201.csv")

data = pd.concat([data, data1,data2], ignore_index=True)

st.title("Crane Load Chart Configuration Selector")
col1, col2 = st.columns(2)

# -------------------------------
# LEFT SIDE FILTERS
# -------------------------------
with col1:

    filtered_df = data.copy()

    selection_columns = [
        'Standard',
        'head_configure',
        'Main_Boom_Length m',
        'Boom_Angle_deg',
        'Angle_Jib_to_Main_Boom_deg',
        'Jib_Length m',
        'SL_Mast_Length m',
        'SL_Mast_Radius m',
        'Superlift_Radius m',
        'Counterweight t',
        'Superlift_Counterweight t',
        'Central_Ballast t'
    ]

    for col in selection_columns:

        unique_values = filtered_df[col].unique().tolist()

        options = []
        for val in unique_values:
            if pd.isna(val):
                options.append("NULL")
            else:
                options.append(val)

        options = sorted(options, key=lambda x: str(x))
        if col.split(" ")[-1]=='m':
            selected =st.selectbox(f"{col[:-2]} in meters",options, key=col)
        elif col.split(" ")[-1] == 't':
            selected = st.selectbox(f"{col[:-2]} in tones",options,key=col)
        elif col=='Boom_Angle_deg':
            selected = st.selectbox(f"Angle_Main_Boom",options,key=col)
        else:
            selected = st.selectbox(f"{col}", options, key=col)

        if selected == "NULL":
            filtered_df = filtered_df[filtered_df[col].isna()]
        else:
            filtered_df = filtered_df[filtered_df[col] == selected]

# -------------------------------
# RIGHT SIDE OUTPUT
# -------------------------------
# -------------------------------
# RIGHT SIDE OUTPUT
# -------------------------------
with col2:

    st.subheader("Filtered Result")

    if filtered_df.empty:
        st.error("No configuration found ❌")
        st.stop()

    st.success("Configuration Found ✅")

    page_numbers = filtered_df['Page_Number'].tolist()

    # -------------------------------
    # Load dic safely
    # -------------------------------
    with open('dic.pkl', 'rb') as file:
        dic = pickle.load(file)
    
    with open('dic-1k-2k.pkl','rb') as file:
        dic1=pickle.load(file)
    
    with open('dic-2k-22k.pkl','rb') as file:
        dic2=pickle.load(file)
    
    dic=dic | dic1
    dic = dic | dic2
    # -------------------------------
    # Collect all available capacity columns
    # -------------------------------
    all_capacity_columns = []

    for pn in page_numbers:
        if pn in dic:
            all_capacity_columns.extend(list(dic[pn].columns)[1:])

    if not all_capacity_columns:
        st.warning("No capacity columns found.")
        st.stop()

    all_capacity_columns = sorted(list(set(all_capacity_columns)))

    headoption = st.selectbox(
        "Select Capacity Column",
        all_capacity_columns
    )

    # -------------------------------
    # Find correct page
    # -------------------------------
    selected_page = None

    for pn in page_numbers:
        if pn in dic and headoption in dic[pn].columns:
            selected_page = pn
            break

    if selected_page is None:
        st.error("Selected capacity column not found in pages.")
        st.stop()

    # -------------------------------
    # Select Radius
    # -------------------------------
    radius_list = dic[selected_page]['Radius'].tolist()

    radiusoption = st.selectbox(
        "Select Radius",
        radius_list
    )

    # -------------------------------
    # Filter Capacity Table
    # -------------------------------
    value = dic[selected_page].loc[
        dic[selected_page]['Radius'] == radiusoption,
        headoption
    ].values
    print(value)
    if value[0] == "" or pd.isna(value[0]):
        st.write(f"Capacity Table (Page {selected_page}) - It can't handle")
    else:
        st.write(f"Capacity Table (Page {selected_page}) - {value[0]} tonnes")