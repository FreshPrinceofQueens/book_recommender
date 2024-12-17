from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "book_recommender"
AUTHOR_USER_NAME = "FreshPrinceofQueens"
SRC_REPO = "src"
LIFT_OF_REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name = SRC_REPO,
    version = "0.0.1",
    author = AUTHOR_USER_NAME,
    description = ("A small package for a book recommender system"),
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FreshPrinceofQueens/book_recommender",
    author_email="tayooduyemi1@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIFT_OF_REQUIREMENTS
)
