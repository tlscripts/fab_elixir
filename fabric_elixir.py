from fabric.tasks import *
from fabric.api import *
from fabric.contrib.files import *
from fabric.contrib.project import *


with open('list_of_hosts.txt') as f:
    env.hosts = [x for x in f]  # in list_of_hosts.txt file add list of host I.P's on each line, no trailing blank lines
# env.hosts = ['']  # For a single host/IP add IP address or hostname and uncomment this line

env.user = '' #SSH user name
env.password = '' #SSH password
env.no_agent = True
env.key_filename = '' #If using SSH keys, fill in the path to your ssh private key

@parallel
def install_elixir():
    sudo('wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && sudo dpkg -i erlang-solutions_1.0_all.deb')
    sudo('apt update')
    sudo('apt install -y esl-erlang')
    sudo('apt install -y elixir')

execute(install_elixir)


