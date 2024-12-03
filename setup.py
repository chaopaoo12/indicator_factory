from setuptools import setup, find_packages


with open() as f:
    required = f.read().splitlines()


setup(
    name="indicator_factory",
    version="1.0",
    author="chaopaoo12",
    author_email="chaopaoo12@hotmail.com",
    description="indicator_factory",

    # 项目主页

    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages(),
    data_files=["requirements.txt"],
    install_requires=required,
)
