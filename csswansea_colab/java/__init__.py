import os, tempfile, shutil
from csswansea_colab.utils import execute_command

def test():
  tmpdir = tempfile.mkdtemp()
  
  with open(f'{tmpdir}/HelloWorld.java', 'w') as f:
    f.write("""
        public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello World.");
            }
        }
    """)

  print(execute_command(f'javac {tmpdir}/HelloWorld.java && java {tmpdir}/HelloWorld'))

  shutil.rmtree(tmpdir)