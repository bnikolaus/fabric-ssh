from fabric.api import *

env.user = 'root'

with open("servers.list") as f:
   env.roledefs['list'] = f.readlines()


def distribute_keys():
   """ Distribute keys to servers """
   local("./ssh-copy-id -i ~/.ssh/id_rsa.pub %s@%s" % (env.user, env.host))
