# 1. Dev-env, super-easy mode (docker all things)

Step by step

```bash
source dev.sh  # import useful bash functions
devhelp  # like this one ;)
dkbuild  # builds the docker image for this project. The first time Will take a while.
dknpminstall  # I'll explain later!
dkup  # Brings up everything
```

With `dkup` running, open another terminal

```bash
dk bash  # starts bash inside "destiny_project" container
./manage.py migrate  # create database tables and stuff
./manage.py createsuperuser  # creates an application user in the database
```

# 2. Dev-env, normal-easy mode (dockerize nginx + postgres)

```bash
dkpgnginx  # Starts postgres and nginx inside docker
```

With `dkpgnginx` running, start another terminal:

```bash
mkvirtualenv destiny_project -p python3  # creates a python3 virtualenv
pip install -r requirements.txt  # install python dependencies inside virtualenv
export DJANGO_DB_PORT=5431  # That's where our dockerized postgres is listening
./manage.py runserver  # starts django on port 8000
```

## Node Setup

Step by step:

```bash
nvm use 12  # Switch your terminal for node version 9.x
# no need to npm install anything, we already have our node_modules folder
sudo chmod -R o+rw .nuxt/  # I'll explain this later
npm run dev  # Starts nuxt frontend on port 3000
```

You can go ahed and point your browser to http://localhost:3000 to see nuxt running **with mocked apis**

To run nuxt using real APIs just turn set this environment variable API_MOCK=0

```bash
API_MOCK=0 npm run dev  # Starts nuxt frontend on port 3000
```

# 3. Deploy to production

Rent a linux machine on a cloud somewhere. Let's say you'll be using ubuntu on AWS.
Install docker and nginx. Create an empty postgres database destiny_project owned by a user destiny_project.

On your remote machine, create a file ~/destiny_project.env:

```
DJANGO_DB_PASSWORD=<destiny_project's password>
DJANGO_DB_HOST=<database_ip>
DJANGO_DB_NAME=destiny_project
DJANGO_DB_USER=destiny_project
DJANGO_DEBUG=0
```

Have a nginx config serving your domain like:

```
server {
    server_name  destiny_project.example.com;

    location /api {
        proxy_pass http://localhost:8000/api;
    }
    location /admin {
        proxy_pass http://localhost:8000/admin;
    }
    location /static {
        alias /home/ubuntu/dkdata/destiny_project/static;
        add_header Cache-Control public;
        add_header ETag "";
    }
    location / {
        proxy_pass http://localhost:3000/;
    }

    listen 80;
}
```

(Replace "destiny_project.example.com" with your production domain)

On your development environment, edit the `HOST_PROD` variable on `dev.sh` to make it point to your production domain, then run on terminal:

```
source dev.sh
deploy_prod
```

If it works the first time, go have a beer and take the day off :-)
