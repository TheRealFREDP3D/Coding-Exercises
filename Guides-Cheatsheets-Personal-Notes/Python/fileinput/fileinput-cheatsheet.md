To pipe a file to a program in Python, you can use the `fileinput` module along with the `sys.stdin` stream. Here's an example:

```python
import fileinput
import sys

# Iterate over lines from file(s) or stdin
for line in fileinput.input():
    # Process the line
    processed_line = line.upper()
    
    # Write the processed line to stdout
    sys.stdout.write(processed_line)
```

To run this script and pipe a file `input.txt` to it:

```
python script.py < input.txt
```

This will read the contents of `input.txt` line by line, convert each line to uppercase using the `line.upper()` method, and write the processed line to `sys.stdout`. 

The `fileinput.input()` function automatically reads from `sys.stdin` if no files are provided as arguments. If file paths are provided, it will read from those files instead.

Alternatively, you can explicitly pass the `-` argument to `fileinput.input()` to read from `sys.stdin`:

```python
import fileinput

for line in fileinput.input(['-']):
    processed_line = line.upper()
    print(processed_line, end='')
```

And then pipe the file:

```
cat input.txt | python script.py
```

This approach allows you to process input from a file or from another command's output by piping it to your Python script. [1][2]

If you need to pipe both input and output, you can use the `/dev/stdin` and `/dev/stdout` file paths:

```python
import sys

with open('/dev/stdin', 'r') as input_file, open('/dev/stdout', 'w') as output_file:
    for line in input_file:
        processed_line = line.upper()
        output_file.write(processed_line)
```

And then pipe both input and output:

```
cat input.txt | python script.py > output.txt
```

This will read from `/dev/stdin` (which is connected to the input pipe), process the lines, and write the output to `/dev/stdout` (which is connected to the output pipe or file). [3][4]

Citations:
[1] https://ssushant.in/posts/writing-pipe-able-python-scripts/
[2] https://www.reddit.com/r/bash/comments/roub2h/pipe_into_python_variable/
[3] https://docs.python.org/3/library/pipes.html
[4] https://unix.stackexchange.com/questions/609207/redirecting-input-from-a-file-to-a-python-script-fails-but-works-with-pipe
[5] https://peteris.rocks/blog/pipes-as-input-output-files/