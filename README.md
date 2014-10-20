cryptopals
==========

Contribute to the development of the [cryptopals.org](http://cryptopals.org).

[cryptopals.org](http://www.cryptopals.org) helps people find friends to send encrypted email to, so they can practice the discipline and contribute to cultures of privacy. It is a friendly effort to support and expand the base of ordinary email encryptors.

It is a side-project, so I am seeking development assistance to make it serve people better. If you have any ideas, suggestions or pull requests inspired by the basic feature wish-list to-do below, please get involved!

The site is a simple, Django-based fork of (https://github.com/pydanny/cookiecutter-django)[https://github.com/pydanny/cookiecutter-django]. Proficient Django users would make light work of the wish list. I include the README from that project (below) as well as information specific to the cryptopals fork.

[More info on the project](http://matt.microsplash.org/2014/02/07/cryptopals/)


### Installation and setup ###


- [install virtualbox](https://www.virtualbox.org)
- [install vagrant](http://www.vagrantup.com/) (easy VM machine config) 

```
#!bash

git clone https://mguy@bitbucket.org/mguy/cryptopals-public.git
cd cryptopals-public
vagrant up --provision
vagrant ssh


cd /vagrant/cryptopals
export WORKON_HOME=/vagrant/Envs
export POSTGRES_PASSWORD="cryptopals"
export POSTGRES_USER="cryptopals"
# SECRET_KEY dev use only
export SECRET_KEY="8974hnetdkenad90d239(039289r0wfndwidoknsncoNDNd"
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
workon cryptopals
./manage.py runserver 0.0.0.0:8080
```

Now access site in your host browser at [http://localhost:1235](http://localhost:1235). Code base available to work on at host machine cryptopals-dev/vagrant/cryptopals-public.


### Who do I talk to? ###

[info@cryptopals.org](mailto:info@cryptopals.org)


### Cryptopals to-do (wish list) ###


- Test public key id link to public key server works (i.e. returns page with email and key id on it) or find other solution to ensure public keys are present and functional, as validation before publishing user listing on site.
- 1) Urge and 2) require public key id addition on registration
- Merge user email (`/accounts/email/`), userprofile (`/users/~update/`) and avatar (`/avatar/change/`) forms
- Allow html links in user interests box
- Improve test coverage
- Style tweaks?

- Find a way to unintrusively check that users are responsive to (encrypted) emails from prospective penpals
    - e.g. send encrypted email (including other content) asking if they want to be on the site still and deactivate if no response, where response could be just a designated key word in subject line
- Other improvements and functionality as suggested by you
