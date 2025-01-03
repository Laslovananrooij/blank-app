import pandas as pd
import streamlit as st
from utils import flatten_images


# Check if there are changes in the editor
def update(data):
    background_file = "/workspaces/blank-app/Images/background/"+ data['background'].values[0] +".png"
    planet_file = "/workspaces/blank-app/Images/Planets/"+ data['planet'].values[0] +".png"

    flatten_images("Out.png",[background_file, planet_file])

    st.image("Out.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)
    st.session_state["df_value"] = edited_df


data = pd.DataFrame(
    {
        "background": [
            "Empty"
        ],
        "planet": [
            "Jupiter"
        ],
    }
)

st.title("Image adder")

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.data = data

# Callback function to update data
def update_data(edited_df):
    st.session_state.df = edited_df

edited_df = st.data_editor(
    data,
    column_config={
        "background": st.column_config.SelectboxColumn(
            label='background',
            help="The background of the image",
            width="medium",
            options=[
                "Empty",
                "Stars",
            ],
            required=True,
        ),
        "planet": st.column_config.SelectboxColumn(
            label='planet',
            help="Planet to choose",
            width="medium",
            options=[
                "Jupiter",
                "Neptune",
                "Saturnus",
                "Uranus",
            ],
            required=True,

        )
     
        },
    hide_index = True,
)

update(edited_df)