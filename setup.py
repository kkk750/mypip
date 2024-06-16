from setuptools import setup, find_packages

setup(
    name='mypip',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pymupdf==1.24.4'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of the package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kkk750/mypip.git',
    # 其他元数据
)
