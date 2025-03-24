import streamlit as st
import pandas as pd

# Örnek DataFrame
df = pd.DataFrame({
    "Ad": ["Ali", "Ayşe", "Mehmet"],
    "Saat": ["01:30:00", "02:00:00", "00:45:00"]
})

# Excel'e çevir
@st.cache_data
def convert_df_to_excel(df):
    from io import BytesIO
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Rapor')
    return output.getvalue()

excel_data = convert_df_to_excel(df)

# İndirme butonu
st.download_button(
    label="📥 Excel Olarak İndir",
    data=excel_data,
    file_name="rapor.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
