# PhoenixV2

## Installation

at root create you environment with
```bash
virtualenv [envname]
```
then run your env
```bash
source [envname]/bin/activate
```
* install django requirement
```bash
pip install -r requirements.txt
```
* go to theme folder this is a tailwind configuration folder
```bash
cd theme/static_src
```
* update npm package 
* =========== only update npm in [theme/static_src] folder ===========
```bash
npm i
npm upgrade
```

## Start dev

```bash
source [yourenv]/bin/activate
python manage.py runserver 
python manage.py tailwind start
```
##


