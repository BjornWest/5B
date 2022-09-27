from random import randint
def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon")
    print()
    print("         a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return None

def open():
    return 0
def closed():
    return 1
def is_open(target):
    if target==open():
        return True
    else:
        return False
def is_closed(target):
    if is_open(target):
        return False
    return True
def new_targets():
    goals = [open(),open(),open(),open(),open()]
    return goals
def close_target(targets,target):
    targets[target] = closed()
    return targets
def hits(targets):
    hits = 0
    for x in targets:
        if  is_closed(targets[x]):
            hits+= 1
    return hits
def target_to_string(target):
    if is_open(target):
        return "* "
    if is_closed(target):
        return "0 "
def targets_to_string(targets):
    out = ""
    for x in targets:
        out+=target_to_string(x)
    return out
def view_targets(targets):
    print(targets_to_string(targets))
def random_hit():
    if randint(0,1) == 0:
        return False
    return True
def shoot(targets,target):
    if random_hit():
        if is_open(targets[target]):
            print("Hit on open target")
            close_target(targets,target)
        else:
            print("Hit on closed target")
    else: 
        print("Miss")
a = new_targets()
b= new_targets()
shoot(b,1)
shoot(b,1)
shoot(b,2)
shoot(b,3)
view_targets(b)
print(hits(b))



