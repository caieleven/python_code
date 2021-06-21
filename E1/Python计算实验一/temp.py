from polygon import *

if __name__ == '__main__':
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.001
    for i in range(60):
        rt(bob,102)
        fd(bob,100)
        lt(bob,60)
        fd(bob,100)
        rt(bob,132)
    wait_for_user()
    
