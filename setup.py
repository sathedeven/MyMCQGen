from setuptools import find_packages,setup

setup(
    name='mcqgen',
    version='0.0.1',
    author='dev s',
    author_email='sathedev@hotmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)