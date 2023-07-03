from setuptools import setup, find_packages 


setup(
    name="openai_wrapper",
    packages=find_packages(include=["openai_wrapper", "openai_wrapper.api_ressources"]),
    version="0.0.1",
    description="A wrapper for the OpenAI API",
    author="AliBen",
    license="MIT",
)