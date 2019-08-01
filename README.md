## Fabric file to install Elixir on multiple hosts simultaneously (or single host) inside your dev or production Linux environment.

As most of you know I love Python's Fabric tool.
Just fill out your SSH credentials or path to SSH private key and that should about do it.
My curiosity of Elixir got the better of me. Figure I should automate it since I won't rememeber any of these shell commands
I think Jerry also wanted learn about Elixir as well.
This is for you. 
The comments in the code should be self explanatory.
If you don't want to simultaneously run this on multiple hosts, comment out those two lines above env.hosts
* Alternatively you could just provide 1 host in the list_of_hosts.txt file (leave out trailing blank lines)

Notes:
* Pip install fabric and fabric2
* Tested on ubuntu 18.041
* Tested on Python 3.68