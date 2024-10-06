import streamlit as st

# Provide suggestions based on ET and weather data
def provide_suggestions(et_values, temps):
    st.write("### Suggestions for Farmers:")
    
    avg_et = sum(et_values) / len(et_values) if et_values else 0
    avg_temp = sum(temps) / len(temps) if temps else 0

    if avg_et > 50:
        st.write("- **High evapotranspiration detected.** Consider increasing irrigation to replenish soil moisture.")
    else:
        st.write("- **Moderate evapotranspiration levels.** Regular irrigation practices should suffice.")

    if avg_temp > 30:
        st.write("- **High temperatures expected.** Monitor water stress in crops and increase water supply if necessary.")
    else:
        st.write("- **Mild temperatures expected.** Continue regular farming practices but monitor forecast changes.")
