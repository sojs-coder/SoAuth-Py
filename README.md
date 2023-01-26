# SoAuth Py

Python middleware for SoAuth.

See [https://soauth.sojs.repl.co](https://soauth.sojs.repl.co)


## Installation

```
pip install soauth
```

## Usage

Import the module into your project:

```py
from soauth import soauth
```

Then, use it as middlewarefor your express app:

```py
app = Flask(__name__)
app.before_request(soauth)
```


This will run the soauth function before every request, checking for the so-auth cookie and validating the user. If the cookie is present and valid, the user data will be stored in the session under `session['so_auth']['user']`. If the cookie is not present or is invalid, `session['so_auth']['user']` will be set to `False`.