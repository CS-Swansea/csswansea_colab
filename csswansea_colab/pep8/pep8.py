import os, tempfile, shutil
import csswansea_colab
from csswansea_colab.utils import execute_command, execute_interactive_command

def configure(verbose=False, execute_tests=True):
  print()
  print('installing pep8 from source')
  execute_command(f'mkdir -p /content/pep8', verbose=verbose)
  shutil.rmtree('/content/pep8/')
  execute_command(f'unzip {os.path.dirname(__file__)}/pep8.zip -d /content/', verbose=verbose)
  execute_command(f'make -C /content/pep8/', verbose=verbose)
  
  print()
  print('updating path env variable')
  os.environ['PATH'] += ':/content/pep8/'  

  print()
  print('updating-alternatives to use pep8')
  execute_command(f'update-alternatives --install /usr/bin/asem8 asem8 /content/pep8/asem8 1', verbose=verbose)
  execute_command(f'update-alternatives --install /usr/bin/pep8  pep8  /content/pep8/pep8  1', verbose=verbose)

  print()
  print('building pep8os')
  execute_command(f'asem8 /content/pep8/pep8os.pep', verbose=verbose)
  
  print()
  print('pep8 version')
  execute_command(f'asem8 -v', verbose=True)
  execute_interactive_command(f'pep8 -v', ['q'], verbose=True)

  if execute_tests:
    test(verbose=verbose)

def test(verbose=False):
  print()
  print('executing tests')
    
  tmpdir = tempfile.mkdtemp()
  
  with open(f'{tmpdir}/HelloWorld.pep', 'w') as f:
    f.write("""br main

msg: .ASCII "Hello World.\x00"

main:    STRO msg, d 
         STOP

.END """)

  execute_command(f'asem8 {tmpdir}/HelloWorld.pep', verbose=verbose)
  execute_interactive_command(f'pep8', ['l', f'{tmpdir}/HelloWorld', 'o', 'f', f'{tmpdir}/HelloWorld.out', 'x', 'q'], verbose=False)

  with open(f'{tmpdir}/HelloWorld.out', 'r') as f:
    result = f.read()

  if 'Hello World.' not in result:
    raise Exception('pep8 HelloWorld test did not produce the expected output...')
  else:
    print('Tests passed.')

  shutil.rmtree(tmpdir)