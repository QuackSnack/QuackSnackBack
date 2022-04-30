# Description

This project contains the backend of a web-application that propose the typical services of any food chain. This project is purely educational.

Click here to see the [frontend](https://github.com/GregoryHue/srfcFront)

# Setup

This setup was made on a Debian 11 distro, using the Windows 11 WSL.

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