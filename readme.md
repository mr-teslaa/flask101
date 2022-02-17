# Important notes

-   _cd = changing directory_
-   _pwd = print working directory_
-   _ll = list view of directory_
-   _.gitignore = ignore any files from uploading on github_
-   _requirements.txt = this file will containe necessary module for this project. you can have this file by this command `pip freeze > requirements.txt`_

## Step 0: Creating Virtual Environment

```bash
$   python -m venv *environment name*
```

### Warning: never use space on environment name

i.e.

```
$   python -m venv env
```

in this case, `env` will be our virutal environment name

## Step 1: Activating Virtual Environment

for cmd:

```bash
$   env\scripts\activate
```

for bash:

```bash
$   env/scripts/activate
```

## Step 2: Installing Flask

```bash
$   pip install flask
```
