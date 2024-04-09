## 0x02. i18n

### Resources

0. [Flask-Babel](https://web.archive.org/web/20201111174034/https://flask-babel.tkte.ch/)
1. [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
2. [pytz](https://pypi.org/project/pytz/)

### Tasks
0. Basic Flask app
1. Basic Babel setup
2. Get locale from request
3. Parametrize templates

Create a babel.cfg file containing

```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

Then initialize your translations with

 ```pybabel extract -F babel.cfg -o messages.pot .```

 and your two dictionaries with

```pybabel init -i messages.pot -d translations -l en```
```pybabel init -i messages.pot -d translations -l fr```

4. Force locale with URL parameter
```http://127.0.0.1:5000/?locale=fr```

5. Mock logging in


```
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```
Visiting ```http://127.0.0.1:5000/?login_as=2``` in your browser

6. Use user locale
7. Infer appropriate time zone
8. Display the current time

### RUN THE APP
```./0-run``` 