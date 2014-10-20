#!/bin/bash
sudo apt-get update
sudo apt-get install python-pip -y
sudo apt-get install git -y
sudo apt-get install libpq-dev python-dev -y
sudo apt-get install libmemcached-dev -y
sudo apt-get install libevent-dev -y
sudo apt-get install postgresql postgresql-contrib -y
sudo -u postgres psql <<-'EOF'
	\password postgres
	cryptopals
	cryptopals
EOF
trap 0
sudo -u postgres createuser cryptopals <<-'EOF'
	cryptopals
	cryptopals
EOF
trap 0
sudo -u postgres psql <<-'EOF'
	create database cryptopals;
	ALTER USER cryptopals WITH PASSWORD 'cryptopals';
	GRANT ALL PRIVILEGES ON DATABASE cryptopals TO cryptopals;
EOF
trap 0
cd /vagrant
pwd
# echo 'export WORKON_HOME=/home/vagrant/Envs' > /home/ubuntu/.profile
# echo 'source /usr/local/bin/virtualenvwrapper.sh' > /home/ubuntu/.profile
export WORKON_HOME=/vagrant/Envs
mkdir -p $WORKON_HOME
pip install virtualenv virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv cryptopals
workon cryptopals
echo $VIRTUAL_ENV
pip install psycopg2
pip install -r /vagrant/requirements.txt
export SECRET_KEY="8974hnetdkenad90d239(039289r0wfndwidoknsncoNDNd"
export POSTGRES_PASSWORD="cryptopals"
export POSTGRES_USER="cryptopals"
cd cryptopals
cat manage.py
pwd
pip freeze
./manage.py syncdb
./manage.py migrate
cd ~
echo "export WORKON_HOME=/vagrant/Envs" >> ~/.profile
echo "export POSTGRES_USER='cryptopals'" >> ~/.profile
echo "export POSTGRES_PASSWORD='cryptopals'" >> ~/.profile
cat ~/.profile
pwd