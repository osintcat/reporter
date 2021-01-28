# Reporter
Simple script to organize information.
## Installation
```bash
sudo apt update -y && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/osintcat/reporter/
cd reporter
pip3 install -r requirements.txt
```
## Usage
Example of first table.

```bash
$ python3 reporter.py 1
Type data in
eg name: John Doe
press CTRL-D to save


Name: John Doe
Age: 30
DOB: 9/10/1993
╒══════╤═══════════╕
│ Name │ John Doe  │
├──────┼───────────┤
│ Age  │ 30        │
├──────┼───────────┤
│ DOB  │ 9/10/1993 │
╘══════╧═══════════╛
would you like to save the output to a file?(y/n): y
filename: out.txt
output saved to: out.txt

```

Example of the second table.

$ python3 reporter.py 2
format:header0,header1,header2
eg. Social Network,Usernames
headers:Social Network, Usernames
Type data in
eg name: John Doe
press CTRL-D to save

instagram: osintcat
╒══════════════════╤══════════════╕
│ Social Network   │  Usernames   │
╞══════════════════╪══════════════╡
│ instagram        │ osintcat     │
╘══════════════════╧══════════════╛
would you like to save the output to a file?(y/n): y
filename: out.txt
output saved to: out.txt
```
