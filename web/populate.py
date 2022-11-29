#!/usr/bin/python3
from web.models.user import User
from web.models.channel import Channel
from web.models.node import Node
from web.models.location import Location
from web.models.schedule import Schedule
from web.models import storage

storage.delete_all()
#create users user_1 - user_10
mapping = ['One', 'Two', 'Three', 'Four', 'Five',
           'Six', 'Seven', 'Eight', 'Nine', 'Ten']
users = []
for n in range(10):
    exec("user{} = User('user_{}', 'User {}')".format(n+1,n+1, mapping[n]))
    users.append(eval("user{}".format(n+1)))

storage.save()

#create locations room_1 - room_10
locs = []
for user in users:
    for n in range(10):
        exec("locs_{}_{} = Location('{}_Room_{}', user.id)".format(user.username, n+1, user.username, n+1))
        locs.append(eval("locs_{}_{}".format(user.username, n+1)))
storage.save()

#Create 3 nodes for each location
nodes = []
for loc in locs:
    for n in range(3):
        exec("nodes_{}_{} = Node('{}_00{}', loc.id)".format(loc.name, n+1, loc.name, n+1))
        nodes.append(eval("nodes_{}_{}".format(loc.name, n+1)))
storage.save()

# Create 5 channels for each node
