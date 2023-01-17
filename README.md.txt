# Brute Force Attack Tools with python

It is necessary to modify the script and add choose correctly the Global variables:
main_url = "URL of the login page"
error_message = "Enter Wrong Password Error Message"
username = "Enter the username to try"

Also, it is possible to choose the Header and the Body parameters. You can use a tool such as Burpsuite to know which parameters are send to the server and replicate the request.
## Simple Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requests.

```bash
pip install requests
```

## Run command

```bash
python3 bruteforce.py
```
## Contributing
Pull requests are welcome. For more changes, please open an issue first to discuss what you would like to change.
