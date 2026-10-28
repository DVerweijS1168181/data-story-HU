import streamlit as st

def app():
	st.title("View the Source Code of the Application")

	# Path to your Streamlit app file
	file_path = "HU/Streamlit_HeartAttack/app.py"  # Adjust this to the correct file path

	# Read the file
	try:
		with open(file_path, "r", encoding="latin1") as file:  # You can also try 'latin1'
			code = file.read()

		# Display the content in Streamlit
		st.code(code, language="python")
	except UnicodeDecodeError:
		st.error("The file encoding is not compatible. Try changing the encoding to 'utf-8' or 'latin1'.")
	except FileNotFoundError:
		st.error("The specified file could not be found.")

