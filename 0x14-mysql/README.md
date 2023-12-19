# Configuring MySql 5.7* on your servers

Installing mysql server and client
### Uninstall any versions on your server

``` sudo apt-get remove --purge mysql* ```
``` sudo apt-get autoremove ```
``` sudo apt-get autoclean ```

### Install mysql
`sudo apt-key add signature.key
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
sudo apt-get update
sudo apt-cache policy mysql-server
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* `