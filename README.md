![Quest Logo](https://mythCDN.henrymartin4.repl.co/logo.png)

Still a work in progress, some features may be glitchy

## Getting Started
Start by downloading or cloning the repo.
```
git clone https://github.com/HENRYMARTIN5/Myth.git
```
Next, create a new file. In my case, it will be called `hellomythworld.mth`. 
Add the folowing code to the file:
```
out Hello, Myth world!
```
Then, edit main.py to open your file instead of the demo. On the line where it says:
```
runner.Run("tests.mth")
```
Change `tests.mth` to whatever your filename is. In the case of this demo, my code in main.py looks like this:
```
import compiler
filetype="standard/.mth"
runner = compiler.MythCompiler(filetype)
runner.Run("hellomythworld.mth")
```
Then, go back to the command prompt / bash and run the following command:
```
python main.py
```
You output should look something like this:
```
Initializing Myth Compiler...
Loading compiler for FileType ".MTH Myth source file"
Running program...
```
Then the terminal will clear and show this output:
```
Hello, Myth world!
```
