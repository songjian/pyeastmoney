import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyeastmoney",
    version="0.1.0",
    author="sj",
    author_email="724385768@qq.com",
    description="获取东方财富数据。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/songjian/pyeastmoney",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests==2.30.0',
        'pandas==1.3.5',
        'tqdm==4.65.0',
        'beautifulsoup4==4.10.0',
        ],
    python_requires='>=3'
)
