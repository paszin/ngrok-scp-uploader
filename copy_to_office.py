import subprocess
import shlex
import os

from pathlib import Path

import os
import datetime

port = sys.argv[1]

def get_modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def get_r_file(filepath, basepath):
    return str(filepath.absolute()).replace(str(basepath.absolute()), "")[1:]

def get_r_filepath(filepath, basepath):
    return str(Path(str(filepath.absolute()).replace(str(basepath.absolute()), "")[1:]).parent)

def get_last_upload_timestamp():
    ts = None
    if Path(".copyToOffice").exists():
        with open(".copyToOffice") as f:
            ts_str = f.read()
            ts = datetime.datetime.strptime(ts_str, '%Y-%m-%d %H:%M:%S.%f')
    return ts

def write_last_upload_timestamp():
    with open(".copyToOffice", "w") as f:
        f.write(str(datetime.datetime.now()))


copy_command = "sshpass -p \"enter here\" scp -P" + port + " %s thullex@0.tcp.ngrok.io:~/remote/location/%s"

path = Path(".")

if get_last_upload_timestamp():
    timedelta = datetime.datetime.now() - get_last_upload_timestamp()
else:
    timedelta = datetime.timedelta(minutes=20)

for f in path.glob("**/*.py"):
    if (datetime.datetime.now() - get_modification_date(f) < timedelta):
        print(get_r_file(f, path))
        print(datetime.datetime.now() - get_modification_date(f))
        command = copy_command %(get_r_file(f, path), get_r_filepath(f, path))
        print(command)
        #print(command.split(" "))
        #subprocess.call(shlex.split(command), shell=True)
        os.system(command)

write_last_upload_timestamp()
