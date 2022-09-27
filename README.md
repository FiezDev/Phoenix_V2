# PhoenixV2

## Installation

* at root
* creat you environment with
```bash
virtualenv [envname]
```
* or use P38
```bash
source P38/bin/activate
```
* install django requirement
```bash
pip install -r requirements.txt
```
* go to theme folder this is a tailwind configuration folder
```bash
cd theme/static_src
```
* update npm package ===========only update npm in this folder
```bash
cd theme/static_src
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


