## 1. Implement the `cat` command - Print file contents

In Linux, there is a very useful command, called `cat`:

```
$ cat file.txt
This is some file
And cat is printing it's contents
```

Implement a Python script, called `cat.py` that takes one argument - a filename and prints the contents of that file to the console.

### Boilerplate:

```python
# cat.py
import sys

def cat(arguments):
    pass


def main():
    pass

if __name__ == '__main__':
    main()
```

### Test Examples

If we have `file.txt` in the same directory with `cat.py`, and `file.txt` content is:

```
Python is an awesome language!
You should try it.
```

This is the result:

```
$ python cat.py file.txt
Python is an awesome language!
You should try it.
```

## 2. Cat multiple files

Implement a Python script, called `cat2.py` that takes multiple arguments - filenames and prints the contents of all files to the console, in the order of the arguments.

**The number of the files that are given as arguments is unknown.**

There should be a newline between every two files that are printed.

### Boilerplate

```python
# cat2.py
import sys


def cat2(arguments):
    pass


def main():
    pass

if __name__ == '__main__':
    main()
```

### Examples

If we have two files - `file1.txt` and `file2.txt` in the same directory with `cat2.py` and:

**file1.txt:**

```
Python is an awesome language!
You should try it.
```

**file2.txt:**

```
Also, you can use Python at a lot of different places!
```

This has to be the result:

```
$ python cat2.py file1.txt file2.txt
Python is an awesome language!
You should try it.

Also, you can use Python at a lot of different places!
```

## 3. Generate file with random integers

Implement a Python script, called `generate_numbers.py` that takes two arguments - a `filename` and a positive integer `n`.

The script should create a file with the `filename` and writes `n` random integers in it, separated by `" "`.

For random integers, you can use:

```python
from random import randint
print(randint(1, 1000))
```

### Boilerplate

```python
# generate_numbers.py
import sys
from random import randint


def generate_numbers(filename, numbers):
    pass


def main():
    pass

if __name__ == '__main__':
    main()
```

### Examples

```
$ python generate_numbers.py numbers.txt 100
$ cat numbers.txt
612 453 555 922 120 840 173 98 994 461 392 739 982 598 610 205 13 604 304 591 830 313 534 47 945 26 975 338 204 51 299 611 699 712 544 868 2 80 472 101 396 744 950 561 378 553 777 248 53 900 209 817 546 12 920 219 38 483 176 566 719 196 240 638 812 630 315 209 774 768 505 268 358 39 783 78 94 293 187 661 743 89 768 549 106 837 687 992 422 30 897 174 844 148 88 472 808 598 341 749
```

## 4. Sum integers from file

Implement a Python script, called `sum_numbers.py` that takes one argument - a `filename` which has integers, separated by `" "`.

The script should print the sum of all integers in that file.

### Examples

If we use the generated file Problem 3:

```
$ python sum_numbers.py numbers.txt
47372
```

## 5. Implement an alternative to du -h command

In Linux, if we want to know the size of a directory, we use the `du` command. For example:

```
$ du -hs /home/rositsazz/code
2,3G  /home/rositsazz/code
```

-   `-h` flag is for "human readable" which means we get the size in gigabytes, not bytes.
-   `-s` flag is for silent. We don't want to print every file that we go through.

In a file called `duhs.py`, implement the logic of `du -hs /some/path`, where `/some/path` is obtained as an argument to the file.

Example usage:

```
$ python duhs.py /home/rositsazz/code
/home/rositsazz/code size is: 2.3G
```

**THIS IS NOT THE SOLUTION WE WANT:**

```python
from subprocess import call
import sys

path = sys.argv[1]

call(["du", "-s", "-h", path])
```

### Hints

-   Check the [`os`](https://docs.python.org/3.7/library/os.html) python module.
-   Many of the methods raise errors. Handle them properly!:

## 6. Count characters, words or lines

Implement a Python script, called `wc.py` that takes two arguments:

-   A command, that can be one of the following : `chars`, `words`, `lines`
-   A filename

The script should output, according to the command, the following:

-   For the command `chars`, the number of characters in the file
-   For the command `words`, the number of words in the file
-   For the command `lines`, the number of lines in the file

### Examples

Lets have the following text:

**story.txt:**

```
Now indulgence dissimilar for his thoroughly has terminated. Agreement offending commanded my an. Change wholly say why eldest period. Are projection put celebrated particular unreserved joy unsatiable its. In then dare good am rose bred or. On am in nearer square wanted.

Of resolve to gravity thought my prepare chamber so. Unsatiable entreaties collecting may sympathize nay interested instrument. If continue building numerous of at relation in margaret. Lasted engage roused mother an am at. Other early while if by do to. Missed living excuse as be. Cause heard fat above first shall for. My smiling to he removal weather on anxious.

Ferrars all spirits his imagine effects amongst neither. It bachelor cheerful of mistaken. Tore has sons put upon wife use bred seen. Its dissimilar invitation ten has discretion unreserved. Had you him humoured jointure ask expenses learning. Blush on in jokes sense do do. Brother hundred he assured reached on up no. On am nearer missed lovers. To it mother extent temper figure better.

```

**Print the chars:**

```
$ python wc.py chars story.txt
1032
```

**Print the words:**

```
$ python wc.py words story.txt
166
```

**Print the lines:**

```
$ python wc.py lines story.txt
5
```

## Reduce file path

A file path in a Unix OS looks like this - `/home/rositsazz/courses/Programming101-Python/week01`

We start from the root - `/` and we navigate to the destination fodler.

But there is a problem - if we have `..` and `.` in our file path, it's not clear where we are going to end up.

-   `..` means to go back one directory
-   `.` means to stay in the same directory
-   we can have more then one `/` between the directories - `/home//code`

So for example : `/home//rositsazz/courses/./Programming101-Python/week01/../` reduces to `/home/rositsazz/courses/Programming101-Python/`.

Implement a function, called `reduce_file_path(path)` which takes a string and returns the reduced version of the path.

-   Every `..` means that we have to go one directory back
-   Every `.` means that we are staying in the same directory
-   Every extra `/` is unnecessary
-   Always remove the last `/`

### Signature

```python
def reduce_file_path(path):
    pass
```

### Test examples

```python
>>> reduce_file_path("/")
"/"
>>> reduce_file_path("/srv/../")
"/"
>>> reduce_file_path("/srv/www/htdocs/wtf/")
"/srv/www/htdocs/wtf"
>>> reduce_file_path("/srv/www/htdocs/wtf")
"/srv/www/htdocs/wtf"
>>> reduce_file_path("/srv/./././././")
"/srv"
>>> reduce_file_path("/etc//wtf/")
"/etc/wtf"
>>> reduce_file_path("/etc/../etc/../etc/../")
"/"
>>> reduce_file_path("//////////////")
"/"
>>> reduce_file_path("/../")
"/"
```
