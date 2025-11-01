import streamlit as st
import time
import os
from CodeModel import generate_code

st.set_page_config(page_title="CodeGenie", page_icon="🧠")

# Sidebar: Guide Section
st.sidebar.title("📚 CodeGenie Guide")
st.sidebar.markdown("""
### 💡 How to Use:
1. Enter a coding prompt in the box.
2. Click on **'Generate Code'**.
3. Wait a few seconds for the code to be generated.

### 🛠 Supported Languages:
- Python
- Java
- C
- C++

### 🧪 Example Prompts:
- `Write a Python function to check for prime numbers`
- `Create a Java class for a student record`
- `Write a C program to sort an array`
- `Generate C++ code for a basic calculator`
""")

# Main Title
st.title("🧠 CodeGenie: AI-Powered Code Generator")
st.markdown("Turn your ideas into code using an AI model!")

# Prompt input
prompt = st.text_area("🔤 Enter your code prompt:", height=200, placeholder="e.g. Write a Python function to check for prime numbers")

# Generate button
if st.button("🚀 Generate Code"):
    if prompt.strip() == "":
        st.warning("⚠️ Please enter a valid prompt.")
    else:
        with st.spinner("Generating code... please wait"):
            try:
                output, start, end = generate_code(prompt)
                st.success(f"✅ Code generated in {end - start:.2f} seconds")
                st.code(output, language="python")
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

# Shutdown button
if st.button("🛑 Shutdown App"):
    st.warning("Shutting down the Streamlit server...")
    os.system("pkill -f streamlit")
