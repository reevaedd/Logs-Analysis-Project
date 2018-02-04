## ABOUT THE PROJECT

This project is about creating an internal reporting tool that will use information from a database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, the code in this project will answer questions about the site's user activity.

## INSTALLATION AND USAGE

Beside the README file, there are other two files in this project package.
They are namely, **news.py** and **Example of Program's Output.txt**.

This project makes use of Linux-based virtual machine (VM). It was tested on a virtual-machine running on VirtualBox and configured using the configuration tool Vagrant.

You can download VirtualBox [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and Vagrant [here](https://www.vagrantup.com/downloads.html).

After the installation is done successfully, start the virtual machine by running the command `vagrant up` from the shell prompt.

When `vagrant up` is finished running, you will get your shell prompt back and then run `vagrant ssh` or `winpty vagrant ssh` to log in the Linux VM. Then, `cd` into the `vagrant` directory.

Next, copy the file **news.py** inside the directory `vagrant`.

You also need to download the data used in this project from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), and load the data using the command `psql -d news -f newsdata.sql` after changing current directory to `vagrant`. Thereafter, by running the command `python news.py`, you will obtain the list of:

- the most popular three articles of all time
- the most populer article authors of aLL TIME
- days on which more than 1% of requests lead to errors

## LICENSE

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

