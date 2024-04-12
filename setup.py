# used to install local package in virtual environment
from setuptools import find_packages,setup

setup(
    name = 'MCQ_Generator', #name of package
    version = '0.0.1',
    author = 'pratik pawar',
    author_email = 'pawarpratikmm25@gmail.com',
    install_requirements = ['google-generativeai','langchain_google_genai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages = find_packages()
)