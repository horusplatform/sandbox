import sys
from io import StringIO

stdout = StringIO() 
stderr = StringIO()

code = f"""print('hello')"""

sys.stdout = stdout
sys.stderr = stderr

command = 'print(123)'
#code = """print ("Hello World")"""
code = f"""{command}"""

exec(code)

sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

print (stdout.getvalue())
print (stderr.getvalue())
print('aqui')

