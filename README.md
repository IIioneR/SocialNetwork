## About 

When writing this test project I configured / used boilerplate that I become accustumed to at work, and added a few personal preferences.


    1. Having `DB` running as a separate entity
    2. Cool `Makefile`
    3. isort, flake8 etc.. ( via `make format`)
    4. Adminer ( I like it, because it's light and simple)
    ...

## How to start 

> Consider views the video that I made with a brief overview of the project: _https://www.youtube.com/watch?v=kLRmfCUYGgY&feature=youtu.be&ab_channel=%D0%9F%D0%B8%D0%BE%D0%BD%D0%B5%D1%80_

> You can change/configure the `env` variables in `./scripts/env.sh`
Start `db` and `adminer`: with

```bash
$ pip install -r requirements/dev.txt
```


```bash
$ make start_db
```

It will run `Docker` containers described in `./stack.yml`

```bash
$ make run 
```
The server should run on http://127.0.0.1:8000/ 

> To apply `autopep8` and `flake8` run:  
```bash
$ make format
```

