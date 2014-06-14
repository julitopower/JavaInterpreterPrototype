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
import javarepl as repl

def clear_screen():
    print chr(27) + "[2J"

def display_welcome_msg():
    print """
>====================================================
> Welcome to the Java interactive interpreter
> Version 0.1
> By Julio Delgado (julio.delgadomangas@gmail.com)
>====================================================
>
>"""

def start_repl():
    global body, imports
    while True:
        line = str(raw_input("> "))
        if line.startswith("print "):
            line = line.replace("print ","")
            line = ("System.out.println(%s)")%(line)
        if line == "reset":
            body = ""
            imports = ""
            continue
        if line == "exit":
            break
        line += ";\n"
        if line.startswith("import"):
            imports.append(line)
        else:
            body.append(line)
        repl.write_java_file("".join(body), "".join(imports))
        if repl.compile("/tmp/Executable.java") == 1:
            body.pop()
            continue
        repl.execute("Executable")
    
body = []
imports = []

if __name__ == "__main__":
    clear_screen()
    display_welcome_msg()
    start_repl()
