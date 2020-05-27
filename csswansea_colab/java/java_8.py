import os
import csswansea_colab
from csswansea_colab.utils import execute_command

test = csswansea_colab.java.test
  
def configure(verbose=False, execute_tests=True):
  print()
  print('installing java')
  execute_command(f'apt-get install -y openjdk-8-jdk-headless', verbose=verbose)
  
  print()
  print('setting JAVA_HOME env variable')
  JAVA_HOME = '/usr/lib/jvm/java-8-openjdk-amd64'
  os.environ['JAVA_HOME'] = JAVA_HOME                             
  
  print()
  print('updating-alternatives to use java version')
  execute_command(f'update-alternatives --set java    {JAVA_HOME}/jre/bin/java', verbose=verbose)
  execute_command(f'update-alternatives --set javac   {JAVA_HOME}/bin/javac'   , verbose=verbose)
  execute_command(f'update-alternatives --set javadoc {JAVA_HOME}/bin/javadoc' , verbose=verbose)
  
  print()
  print('java version')
  execute_command(f'java -version', verbose=True)
  print('javac version')
  execute_command(f'javac -version', verbose=True)

  if execute_tests:
    test(verbose=verbose)