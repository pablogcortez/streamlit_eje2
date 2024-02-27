import streamlit as st
import pandas as pd
import numpy as np


def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Cargar archivo - Mi Aplicación",
        page_icon=":bar_chart:",
        layout="wide"
    )

    # Título de la página
    st.title("Cargar archivo en Streamlit")

    # Widget para cargar el archivo
    uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])

    # Separador
    st.markdown("---")

    if uploaded_file is not None:
        # Leer el archivo en un DataFrame de Pandas
        df = pd.read_csv(uploaded_file)

        # Convertir la columna de fecha a tipo datetime
        df["FECHA"] = pd.to_datetime(df["FECHA"])

        ## Mostrar el DataFrame
        # st.write("Contenido del archivo:")
        # st.dataframe(df)

        # Filtro por fecha
        st.sidebar.subheader("Filtrar por Fecha")
        start_date = pd.to_datetime(st.sidebar.date_input("Fecha de inicio", min(df["FECHA"])))
        end_date = pd.to_datetime(st.sidebar.date_input("Fecha de fin", max(df["FECHA"])))

        # Filtrar los datos según el rango de fechas seleccionado
        filtered_df = df[(df["FECHA"] >= start_date) & (df["FECHA"] <= end_date)]

        # Mostrar los datos filtrados
        st.write("Datos filtrados por fecha:")
        st.dataframe(filtered_df)

        # Gráfico de barras
        st.subheader("Gráfico de Barras - ACUMULADA PROMEDIO")
        st.bar_chart(filtered_df["ACUMULADA PROMEDIO"])


if __name__ == "__main__":
    main()