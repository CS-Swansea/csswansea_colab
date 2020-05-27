import os, tempfile, shutil
from csswansea_colab.utils import execute_command

def test(verbose=False):
  tmpdir = tempfile.mkdtemp()
  
  with open(f'{tmpdir}/HelloWorld.java', 'w') as f:
    f.write("""
        public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello World.");
            }
        }
    """)

  execute_command(f'javac {tmpdir}/HelloWorld.java -d {tmpdir}', verbose=verbose)
  result = execute_command(f'java -cp {tmpdir} HelloWorld',      verbose=verbose)

  if 'Hello World.' not in result:
    raise Exception('java HelloWorld test did not produce the expected output...')

  shutil.rmtree(tmpdir)