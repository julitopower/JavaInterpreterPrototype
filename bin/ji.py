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
import sys
import subprocess

CLASS_PATTERN = """
%s

public class Executable {
    public static void main(String args[]) {
%s
    }
}
"""

def __wrap_into_valid_class(fstream):
    body = ""
    imports = ""  
    for line in fstream.readlines():
        if(line.startswith("import")):
            imports += line
            continue
           
        body += "        " + line
    body = (CLASS_PATTERN)%(imports, body)
    print body
    with(open("/tmp/Executable.java", "w+")) as f:
        f.write(body)

def __compile(filename):
    args = ("javac", filename)
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print output

def __execute(clazz):
    args = ("java", "-cp","/tmp", clazz);
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print output    

def run(filename):
    with(open(filename)) as f:
        __wrap_into_valid_class(f)
        __compile("/tmp/Executable.java")
        __execute("Executable")

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print "An input file must be provided"
        exit(0)
    filename = sys.argv[1]
    print "Executing file " + filename
    run(filename);
