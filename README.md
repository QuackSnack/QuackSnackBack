# Description

This project contains the backend of a web-application called **FoodDistribution** that propose the typical services of any food chain. This project and the web-application is made purely as an educationnal purpose.

Click here to see the [frontend](https://github.com/GregoryHue/FoodDistributionFront).

# Setup

This setup was made on a Debian 11 distro, using the Windows 11 WSL. The project is placed in `/home/user/dev/FoodDistributionBack`.

## By using a shell (installs both project)

To facilitate the setup and project management, a shell is proposed in both projects. Pull this project, get in the folder `/home/user/dev/FoodDistributionBack` and use the command :

```
source fd-shell.sh; fd-install
```

This will install the shell in your `~/.bashrc` file. The shell includes the following commands :


* `fd-install` : install the shell in `~/.bashrc`.
* `fd-remove` : remove the shell in `~/.bashrc`.
* `fd-project` : pull and setup the frontend or the backend or both.
* `fd-front` : start or build the frontend of the application.
* `fd-back` : start the backend of the application or migrate the database.
* `fd-both` : start the frontend and backend in two new terminals.

For a quick installation, use :

```
fd-project both && fd-back migrate && fd-both start
```

This should pull and setup both projects, then start them.

If you wish to remove the shell, use this command from any folder :

```
fd-remove
```

You may need to relog into your session so that it takes effect.

## By installing dependencies manually (installs only the current project)

Update your packages :

```
sudo apt update && sudo apt upgrade
```

Install all the dependencies :

```
sudo apt install python3 python3-pip postgresql postgresql-contrib
```

If you're using WSL, you probably need to restart the Postgresql service : 

```
sudo service postregsql restart
```

Install Django :

```
python3 -m pip install Django
```

Versions :
* Python 3.9.2
* Django-admin 4.0.4

# Structure

The structure of the project needs to respect the following :

```
main/
    subfolders/
    subfiles.ext
.gitignore
LICENSE
LICENSE.md
fd-shell.sh
```