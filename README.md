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

Then, edit `demo.py` to open your file instead of the demo. Originally, it says:

```
import myth, output;myth.compile("in.mth", "out.py", myth.debug, output.py)
```

Change `in.mth` to whatever your filename is, and set `out.py` to whatever you want your output file to be named. In the case of this demo, my code in `main.py` looks like this:

```
import myth, output;myth.compile("hellomythworld.mth", "hellomythworld.py", myth.debug, output.py)
```
Then, go back to the command prompt / bash and run the following command:
```
python youroutputfilenamehere.py
```

You output should look something like this:

```
Hello, Myth world!
```
