from setuptools import setup, find_packages

setup(
    name='gradcam_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tensorflow==2.10.0',
        'numpy==1.23.4',
        'opencv-python==4.6.0',
        'matplotlib==3.5.1'
    ],
    description='A project for Grad-CAM visualizations in neural networks',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
)