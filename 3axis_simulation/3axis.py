import math
from math import cos ,sin, acos ,pi, radians, degrees
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import animation # 動畫
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(figsize=(10,10))
#ax = Axes3D(fig)
#ax = plt.subplot(211, aspect='equal')
ax = fig.gca(projection='3d') #得到當前的軸
ax.set_aspect('equal')#設置軸縮放比例，即y單位與x單位的比率。


r2d = 1/180*pi

JointAngle = [0,0,0]
Od = [0,0,0]
pos = [ [None] * 3 for i in range(4) ]
ax = plt.subplot(111, projection='3d')  #創建一個三维的繪圖

def Time(Od):# 計數器
	Od += Cnt
	return Od
# animate
def animate(i):
	#fig.update()
	Time(Od)  #跑一次幀計數一次
	x = kinematics_change(pos,Od,JointAngle)[:,0]
	y = kinematics_change(pos,Od,JointAngle)[:,1]
	z = kinematics_change(pos,Od,JointAngle)[:,2]
	# plot_animate, = ax.plot(x,y,z,"o-",color="#00aa00", ms=4, mew=0.5,label='aaa') # 'b*'表示藍色*狀線，label是指定義圖例
	
	ax.clear()
	ax.set_zlabel('Z')  # 座標軸    
	ax.set_ylabel('Y')
	ax.set_xlabel('X')
    
    
	ax.set_xlim3d(-20, 20,emit=True, auto=False)
	ax.set_ylim3d(-20, 20,emit=True, auto=False)
	ax.set_zlim3d(-20, 20,emit=True, auto=False)
	ax.plot(x,y,z,"o-",color="#00aa00", ms=4, mew=0.5,label='aaa') # 'b*'表示藍色*狀線，label是指定義圖例
# init_plot
def init():
	kinematics(pos,Od,JointAngle)
	x = kinematics(pos,Od,JointAngle)[:,0]
	y = kinematics(pos,Od,JointAngle)[:,1]
	z = kinematics(pos,Od,JointAngle)[:,2]
	# plot_init, = ax.plot(x,y,z,"o-",color="#00aa00", ms=4, mew=0.5,label='aaa') # 'b*'表示藍色*狀線，label是指定義圖例
	ax.clear()
	ax.plot(x,y,z,"o-",color="#00aa00", ms=4, mew=0.5,label='aaa') # 'b*'表示藍色*狀線，label是指定義圖例
# 正運動學 函式
def Tran_List(JointAngle,stop):
    
	DH=np.array([[0,90,10,JointAngle[0]+90],[10,0,0,JointAngle[1]],[10,90,0,JointAngle[2]]])
	Tranoriginal=np.eye(4)
    
	for i in range(0,stop):
		tran=np.array([[round(cos(DH[i][3]*r2d),8) ,-round(sin(DH[i][3]*r2d),8)*round(cos(DH[i][1]*r2d),8) ,round(sin(DH[i][3]*r2d),8)*round(sin(DH[i][1]*r2d),8) ,DH[i][0]*round(cos(DH[i][3]*r2d),8)],
			[round(sin(DH[i][3]*r2d),8) ,round(cos(DH[i][3]*r2d),8)*round(cos(DH[i][1]*r2d),8)      ,-round(cos(DH[i][3]*r2d),8)*round(sin(DH[i][1]*r2d),8)   ,DH[i][0]*round(sin(DH[i][3]*r2d),8)],
			[0             ,round(sin(DH[i][1]*r2d),8)        ,round(cos(DH[i][1]*r2d),8)                ,DH[i][2]],
			[0              ,0                              ,0                              ,1]])
        
		Tranoriginal=np.dot(Tranoriginal,tran)
		Tran=Tranoriginal
  
	return(Tran)

# 正運動學 函式

	
def direct_Kinematics(JointAngle):
	Tran1 = Tran_List(JointAngle,1)
	Tran2 = Tran_List(JointAngle,2)
	Tran3 = Tran_List(JointAngle,3)
    	
	pos =np.array([ [0,0,0],
           [Tran1[0][3],Tran1[1][3],Tran1[2][3]],
          [Tran2[0][3],Tran2[1][3],Tran2[2][3]],
          [Tran3[0][3],Tran3[1][3],Tran3[2][3]]])
	
	return pos

# 逆運動學 函式
def inver_Kinematics(JointAngle,Od):

	Link=np.array([10,10,10])

	JointAngle[0] =-math.atan2(Od[0], Od[1])
	
	D = np.linalg.norm(Od-[0,0,Link[0]])
	
	JointAngle[2] = acos((Link[1]**2 + Link[2]**2 - D**2) / (2*Link[1]*Link[2])) - pi
	
	JointAngle[1] = math.atan2(Od[2]-Link[0],(Od[0]**2+Od[1]**2)**0.5) - math.atan2(Link[2]*math.sin(JointAngle[2]),Link[1]+Link[2]*math.cos(JointAngle[2]))
	
	JointAngle = [x*180/math.pi for x in JointAngle]#JointAngle[]=JointAngle[]*180/math.pi

	return JointAngle

def kinematics(pos,Od,JointAngle):
	# 逆運動學
	inver_Kinematics(JointAngle,Od)
	
	#print(JointAngle)	
# 正運動學 
	Tran1 = Tran_List(inver_Kinematics(JointAngle,Od),1)
	Tran2 = Tran_List(inver_Kinematics(JointAngle,Od),2)
	Tran3 = Tran_List(inver_Kinematics(JointAngle,Od),3)
    	
	pos =np.array([ [0,0,0],
           [Tran1[0][3],Tran1[1][3],Tran1[2][3]],
          [Tran2[0][3],Tran2[1][3],Tran2[2][3]],
          [Tran3[0][3],Tran3[1][3],Tran3[2][3]]])
	#print(pos)
	return pos
def kinematics_change(pos,Od,JointAngle):
	# 逆運動學
	#Od += Cnt
	inver_Kinematics(JointAngle,Od)
	
	#print(JointAngle)	
# 正運動學 
	Tran1 = Tran_List(inver_Kinematics(JointAngle,Od),1)
	Tran2 = Tran_List(inver_Kinematics(JointAngle,Od),2)
	Tran3 = Tran_List(inver_Kinematics(JointAngle,Od),3)
    	
	pos =np.array([ [0,0,0],
           [Tran1[0][3],Tran1[1][3],Tran1[2][3]],
          [Tran2[0][3],Tran2[1][3],Tran2[2][3]],
          [Tran3[0][3],Tran3[1][3],Tran3[2][3]]])
	#print(pos)
	return pos
# 選擇輸入求各軸角度或末端點位
a_input=int(input('求末端點位(輸入1)  各軸角度(輸入2)  點到點動畫(輸入3):'))
if a_input==1:
	print('請輸入末端點位置：')
	Od = np.array([float(x) for x in input().split()])
	print(Od)

	kinematics(pos,Od,JointAngle)# 經正逆運動學 繪圖求角度 與末端點

	x = kinematics(pos,Od,JointAngle)[:,0]
	y = kinematics(pos,Od,JointAngle)[:,1]
	z = kinematics(pos,Od,JointAngle)[:,2]
	print(inver_Kinematics(JointAngle,Od)) #show pos
	print(kinematics(pos,Od,JointAngle)) #show angle
	ax.plot(x,y,z,"o-",color="#00aa00", ms=4, mew=0.5,label='aaa') # 'b*'表示藍色*狀線，label是指定義圖例

	ax.set_zlabel('Z')  # 座標軸
	ax.set_ylabel('Y')
	ax.set_xlabel('X')
	plt.title('t3axis_pos') # 設置標題
	plt.legend() # 顯示上面定義的圖例

	plt.show()
elif a_input==2:
	print('請輸入各軸角度(三軸)：')
	JointAngle = np.array([float(x) for x in input().split()])
    
	direct_Kinematics(JointAngle)
	print(direct_Kinematics(JointAngle))
	
	x = direct_Kinematics(JointAngle)[:,0]
	y = direct_Kinematics(JointAngle)[:,1]
	z = direct_Kinematics(JointAngle)[:,2]
	ax.plot(x,y,z,"o-",color="#00aa00", ms=4, mew=0.5,label='aaa') # 'b*'表示藍色*狀線，label是指定義圖例

	ax.set_zlabel('Z')  # 座標軸
	ax.set_ylabel('Y')
	ax.set_xlabel('X')
	plt.title('3axis_3joints') # 設置標題
	plt.legend() # 顯示上面定義的圖例

	plt.show()
# 繪製動畫 輸入兩點
elif a_input==3:
	print('請輸入起始末端點位置：')
	Od = np.array([float(x) for x in input().split()])
	print(Od)
	print('請輸入終點末端點位置：')
	O_end = np.array([float(x) for x in input().split()])
	num = 100
	Cnt = (O_end - Od)/num

	ani = animation.FuncAnimation(fig, #進行動畫繪製的figure
                              func = animate, #自定義動畫函數，即傳入剛定義的函數animate
                              frames=100, #動畫長度，一次循環包含的幀數
                              init_func=init, #自定義開始幀，即傳入剛定義的函數init
                              interval=10, #更新頻率，以ms計
                              repeat=False)
	
    
	ax.set_xlim3d(-20, 20,emit=True, auto=False)
	ax.set_ylim3d(-20, 20,emit=True, auto=False)
	ax.set_zlim3d(-20, 20,emit=True, auto=False)
	ax.set_zlabel('Z')  # 座標軸
	ax.set_ylabel('Y')
	ax.set_xlabel('X')
	plt.title('3axis_animation') # 設置標題
	plt.legend() # 顯示上面定義的圖例

	#ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264']) #產出動畫影片
	plt.show()
else:
 	print('See you next time')
