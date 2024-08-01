from setuptools import setup, find_packages

setup(
    name='sparse_autoencoder',
    version='0.0.1',
    url='https://github.com/MaksymDel/sparse_autoencoder.git',
    packages=find_packages(),    
    install_requires=['transformer_lens >= 1.9.1', 'torch >= 2.1.0', 'blobfile >= 2.0.2'],
)