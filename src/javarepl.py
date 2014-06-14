# The MIT License (MIT)
# 
# Copyright (c) 2014 Julio Delgado
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess

CLASS_PATTERN = """
%s

public class Executable {
    public static void main(String args[]) {
%s
    }
}
"""

def wrap_into_valid_class(fstream):
    body=""
    imports = ""  
    for line in fstream.readlines():
        if(line.startswith("import")):
            imports += line
            continue
           
        body += "        " + line
    write_java_file(body, imports)

def write_java_file(body="", imports=""):
    body = (CLASS_PATTERN)%(imports, body)
    with(open("/tmp/Executable.java", "w+")) as f:
        f.write(body)

def compile(filename):
    args = ("javac", filename)
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print output
    return popen.returncode

def execute(clazz):
    args = ("java", "-cp","/tmp", clazz);
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print output
    return popen.returncode

