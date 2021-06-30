
######################
CONSTRAIN = True
######################

import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,0.2]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])

loopId = p.loadURDF("four_bar_loop/urdf/four_bar_loop.urdf",[0,0.2,0.2], cubeStartOrientation,useFixedBase=1)


if CONSTRAIN == True:
    p.createConstraint(loopId, 2, loopId, -1, p.JOINT_POINT2POINT, [0, 0, 0], [0.225, 0, 0], [-0.2, 0, 0])

for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()
