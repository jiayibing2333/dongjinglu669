from setuptools import setup, find_packages

setup(
    name="dongjinglu669",
    version="0.0.1",
    keywords=["markdown", "Plastic-Metal"],
    description="To generate markdown-formatted lab reports.",
    long_description="Light-weight tool to generate markdown-formatted lab reports. For python.",
    license="MIT",

    url="https://github.com/jiayibing2333/dongjinglu669",
    author="Ferdinand Sukhoi",
    author_email="ferdinandsukhoi@outlook.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["pypandoc"]
)
