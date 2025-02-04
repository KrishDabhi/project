from setuptools import find_packages, setup

setup(
    names='mcqgenerator',
    version='0.0.1',
    author='Krish Dabhi',
    author_email='helloshopping7354@gmail.com',
    install_requires=["os","langchain","streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)