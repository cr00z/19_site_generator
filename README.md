# Encyclopedia

This script converts articles from [Markdown](https://wikipedia.org/wiki/Markdown) into HTML and makes one a small static site.

Script use [livereload](https://pypi.org/project/livereload/2.6.0/) for tracking changes in the source and automatically rebuilds the site.

Example: https://cr00z.github.io/19_site_generator/www/index.html

# How to Install

Python 3 should be already installed. 

Script use:

* [Markdown](https://pypi.org/project/markdown/3.1/)
* [Jinja2](https://pypi.org/project/jinja2/2.10.1/)
* [livereload](https://pypi.org/project/livereload/2.6.0/)

Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python encyclopedia.py
[I 190428 17:28:06 server:298] Serving on http://127.0.0.1:5500
[I 190428 17:28:06 handlers:59] Start watching changes
[I 190428 17:28:06 handlers:61] Start detecting changes
[I 190428 17:28:10 handlers:132] Browser Connected: http://localhost:5500/

```

# Rebuilding

Use http://localhost:5500/ for browse the site.

If you add new *article.md* at *articles* folder and put its link into *config.json*, the site will be rebuilt automatically. 

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
