'''
Setup
'''
from setuptools import setup, find_packages

setup(
    name='pacote_teste',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],  # Lista de dependências
    author='Rodney',
    author_email='rodneyg.ribeiro@gmail.com',
    description='Programa básico somente para teste',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RodneyRibeiro/Dio-Desafios/tree/Desafios_Dio/pacote_teste',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

#EOF
