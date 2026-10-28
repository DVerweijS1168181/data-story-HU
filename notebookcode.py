import streamlit as st

def app():
	st.title("Raw Jupyter Notebook Code")

	# Path to your Jupyter Notebook file
	file_path = "HU/Streamlit_HeartAttack/cardiovascular_diseases.ipynb"  # Adjust this to the correct file path

	# Read and display the raw JSON content of the notebook
	try:
		with open(file_path, "rb") as file:
			st.download_button(
				label="Download Jupyter Notebook",
				data=file,
				file_name="cardiovascular_diseases.ipynb",
				mime="application/x-ipynb+json"
			)

		with open(file_path, "r", encoding="utf-8") as file:
			code = file.read()

		st.code(code, language="json")  # Display it as JSON, since notebooks are stored in JSON format

	except FileNotFoundError:
		st.error(f"The file '{file_path}' could not be found.")