# TicketViewerAPI

An API for displaying the tickets by connecting to Zendesk API

# Development environment and Dependencies

Programming Language: Python 2.7.12 
Development environment: Ubuntu 16.04 Xenial
Libraries used: Python Requests and Python Tabulate

# Installations

A. Python 

Python is readily available on Ubuntu releases, If not it can be downloaded and installed on Linux through command line,

1. Install Required Packages

Use the following command to install prerequisites for Python before installing it.

sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

2. Download the required python version 

version=2.7.13
cd ~/Downloads/
wget https://www.python.org/ftp/python/$version/Python-$version.tgz

3. Extract the downloaded package.

tar -xvf Python-$version.tgz
cd Python-$version

4. Compile Python Source

./configure
make
sudo checkinstall

The same can be found in the link [https://askubuntu.com/questions/101591/how-do-i-install-the-latest-python-2-7-x-or-3-x-on-ubuntu]

You can also follow the steps listed on [http://docs.python-guide.org/en/latest/starting/install/osx/] for Mac and [http://docs.python-guide.org/en/latest/starting/install/win/] for Windows users.

You might as well install pip, if you don't have it installed already

You can the following command on Mac to install pip,

sudo easy_install pip

And for Ubuntu,

sudo apt-get install python-pip

B. Libraries

Requests Library is used for handling the HTTP requests and Tabulate library is used for displaying the ticket details in an orderly manner

You can simply do it by uing the foillowing command

1. pip install requests

2. pip install tabulate

You can also find further documentation on installing python packages in the links [https://docs.python.org/2/installing/], [https://pypi.python.org/pypi/requests] and  [https://pypi.python.org/pypi/tabulate].


# Running the API

You can simply run the following command on command line to run the API.

python ticketViewer.py


You can also change the URL and authentication details in the 'ticketViewer.py' file to connect and display tickets from a different 

# Testing

You can simply run the following command to test the API

python testAPI.py

