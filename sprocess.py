import subprocess

'''
shell = True
Use a string in the command
Takes env variables
Opens a new terminal
It takes a little bit extra time

shell = False
Use a list as the command
It is not able to take env variables
Same terminal
A little faster
'''
#cmd = "invalid"

cmd = "ls -lrt"
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

cmd = ['ls', '-lrt']
sp = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

rc=sp.wait()
out,err=sp.communicate()

print(f'Return code: {rc}')
print(f'Output as String: \n{out}')
print(f'Output as list: \n{out.splitlines()}')
print(f'Error: \n{err.splitlines()}')



cmd = ["bash", "--version"]
sp = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait()
o,e=sp.communicate()
if rc==0:
    for each_line in o.splitlines():
        if "version" in each_line and "release" in each_line:
            print (f'Bash: {each_line.split()[3].split("(")[0]}')
else:
    print("Command error")




cmd = ["java", "-version"]
sp = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait()
ou,er=sp.communicate()
if rc==0:
    for each_line in er.splitlines():
        if "version" in each_line:
            t = each_line.split()[2].split('"')[1]
            print (f"Java: {t}")
else:
    print("Command error")