from setuptools import setup

setup(name='csswansea_colab',
      version='1.0',
      description='Resources for Configuring Programming Environments in Google Colab',
      author='Dr Joss Whittle',
      author_email='j.o.whittle@swansea.ac.uk',
      packages=[
          'csswansea_colab', 
          'csswansea_colab.utils', 
          'csswansea_colab.java',
          'csswansea_colab.prolog',
          'csswansea_colab.haskell',
      ], 
      install_requires=[],
      scripts=[]
)
