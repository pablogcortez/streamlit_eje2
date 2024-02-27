import streamlit as st
import pandas as pd

# Función para verificar las credenciales
def verificar_credenciales(username, password):
    # Cargar el archivo Excel desde GitHub
    df_credenciales = pd.read_excel("https://raw.githubusercontent.com/tu_usuario/tu_repositorio/tu_rama/credenciales.xlsx")
    
    # Verificar si las credenciales coinciden
    if (df_credenciales["Username"] == username) & (df_credenciales["Password"] == password)).any():
        return True
    else:
        return False

# Función principal
def main():
    # Título de la página
    st.title("Inicio de Sesión")

    # Obtener credenciales del usuario
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    # Botón de inicio de sesión
    if st.button("Iniciar Sesión"):
        if verificar_credenciales(username, password):
            st.success("Inicio de sesión exitoso!")
            # Ejecutar el código principal si las credenciales son correctas
            run_main_app()
        else:
            st.error("Credenciales incorrectas. Por favor, inténtalo de nuevo.")

# Código principal de la aplicación
def run_main_app():
    # Configuración de la página
    st.set_page_config(
        page_title="Cargar archivo - Mi Aplicación",
        page_icon=":bar_chart:",
        layout="wide"
    )

    # Resto del código principal...
    # (Aquí iría tu código original)
    # ...

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
