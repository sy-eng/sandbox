import math
import transforms3d
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Quaternion

# euler.zは0 - PI/2,それ以外は0 - PIか。euler.zがPI/2+PInは特異点
def quat_to_rpy(qx, qy, qz, qw):
    # Z-Y-X (yaw-pitch-roll,前側から適用する。) に対応する標準式
    sinRoll_cosPitch = 2.0 * (qw * qx + qy * qz)
    cosRoll_cosPitch = 1.0 - 2.0 * (qx * qx + qy * qy)
    roll = math.atan2(sinRoll_cosPitch, cosRoll_cosPitch)

    sinPitch = 2.0 * (qw * qy - qz * qx)
    if abs(sinPitch) >= 1.0:
        pitch = math.copysign(math.pi / 2.0, sinPitch)
    else:
        pitch = math.asin(sinPitch)

    sinYaw_cosPitch = 2.0 * (qw * qz + qx * qy)
    cosYaw_cosPitch = 1.0 - 2.0 * (qy * qy + qz * qz)
    yaw = math.atan2(sinYaw_cosPitch, cosYaw_cosPitch)

    return roll, pitch, yaw  # [x:roll, y:pitch, z:yaw]

def conversionCheck(euler):
	print("euler : ", euler)
#	q = transforms3d.euler.TBZYX().euler2quat(euler.x, euler.y, euler.z)
	q = transforms3d.euler.euler2quat(euler.x, euler.y, euler.z)
	print(q)
	print(quat_to_rpy(q[1], q[2], q[3], q[0]))
#	print(transforms3d.euler.TBZYX().quat2euler(q))
	print(transforms3d.euler.quat2euler(q))
#	print(type(transforms3d.euler.TBZYX().quat2euler(q)))
	
# 3番めの引数(yaw)から回す。3番め、2番め(pitch)、1番め(roll)の順番に回す。
data = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0], 
	[1.0, 1.0, 0.0], [1.0, 0.0, 1.0], [1.0, 1.0, 1.0], [0.0, 1.0, 1.0],]

eulers = [Vector3(x = d[0], y = d[1], z = d[2]) for d in data]
for e in eulers:
	conversionCheck(e)
	
def testFunc():
	return (1.0, 2.0, 3.0)
	
[x, y, z] = testFunc()
print(x, y, z)

quat = Quaternion(w = 1.0, x = 2.0, y = 3.0, z = 4.0)
print(quat)
