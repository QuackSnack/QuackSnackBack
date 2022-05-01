# Description

This project contains the backend of a web-application called **FoodDistribution** that propose the typical services of any food chain. This project and the web-application is made purely as an educationnal purpose.

Click here to see the [frontend](https://github.com/GregoryHue/FoodDistributionFront).

# Setup

This setup was made on a Debian 11 distro, using the Windows 11 WSL. The project is placed in `/home/user/dev/FoodDistributionBack`.

## Dependencies

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

## Structure

The structure of the project needs to respect the following :

```
main/
    subfolders/
    subfiles.ext
.gitignore
LICENSE
LICENSE.md
```

## Shell

