def configure(verbose=False):
  import os
  from csswansea.utils import execute_command
  
  print()
  print('installing java')
  install_output = execute_command(f'apt-get install -y openjdk-8-jdk-headless')
  if verbose:
    print(install_output)

  print()
  print('setting JAVA_HOME env variable')
  JAVA_HOME = '/usr/lib/jvm/java-8-openjdk-amd64'
  os.environ['JAVA_HOME'] = JAVA_HOME                             
  
  print()
  print('updating-alternatives to use java version')
  print(execute_command(f'update-alternatives --set java    {JAVA_HOME}/jre/bin/java'))
  print(execute_command(f'update-alternatives --set javac   {JAVA_HOME}/bin/javac'   ))
  print(execute_command(f'update-alternatives --set javadoc {JAVA_HOME}/bin/javadoc' ))
  
  print()
  print('java version')
  print(execute_command(f'java -version'))
  print('javac version')
  print(execute_command(f'javac -version'))
