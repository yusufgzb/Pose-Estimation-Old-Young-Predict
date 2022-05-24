import cv2
import numpy as np
import pandas as pd

df=pd.read_csv("butunNoktalar1.csv")
print(df.shape[0])
image  = cv2.imread("beyaz.png")
image=cv2.resize(image,(800,680))

col_atlama=4
satir_atlama=0
x_eksen=[]
y_eksen=[]


global_colors=[]

for i in range(9):
    global_colors.append([])
#global_colors[0]=[,,]
global_colors[1]=[180,180,180]#bitiş 0 0 0
global_colors[2]=[255,180,220]#bitiş 236 0 118
global_colors[3]=[255,45,45]#bitiş 150 0 0
global_colors[4]=[125,249,255]#bitiş 0 189 196
global_colors[5]=[255,255,81]#bitiş 210 210 0
global_colors[6]=[110,255,110]#bitiş 0 113 0
global_colors[7]=[255,158,62]#bitiş 221 111 0
global_colors[8]=[66,66,255]#bitiş 0 0 145

"""
0 => 1-0-4
1 => 4-5-6-8-1-2-3-7
1 => 23-24 Kalça
2 => 11-13 12-14
3 => 13-15 14-16
4 => 15-16-17-18-19-20-21-22 #eller
5 => 11-23 12-24
6 => 23-25 24-26
7 => 26-28 25-27
8 => 27-28-29-30-31-32
"""
satir_atlama_sinir=48
while satir_atlama<df.shape[0]:
    x_eksen.clear()
    y_eksen.clear()
    #Kordinatları alıp x ve y değerlerini listeye atılıyor
    if df["img_name"][satir_atlama] == df["img_name"][satir_atlama+1]:

        for i in range(33):
            if df["img_name"][satir_atlama] == df["img_name"][satir_atlama+1]:


                corr=df.iloc[satir_atlama:satir_atlama+1,col_atlama-2:col_atlama].values

                x=int(480*(float(corr[0][0])))
                y=int(640*(float(corr[0][1])))
                x_eksen.append(x)
                y_eksen.append(y)
                col_atlama +=2
            else:
                continue

            #image = cv2.circle(image , (x,y), 6, (0, 0, 255), -1)
        satir_atlama=satir_atlama + 8
        col_atlama = 4

        i=0

        for i in range(33):

            #Kafa Kısmı

            try:
                if i==0:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[1],y_eksen[1]), (0,150,150), 4)
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[4],y_eksen[4]), (0,150,150), 4)     
                
                elif i==1:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[2],y_eksen[2]), (0,150,150), 4)
                elif i==2:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[3],y_eksen[3]), (0,150,150), 4)
                elif i==3:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[7],y_eksen[7]), (0,150,150), 4)
                elif i==4:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[5],y_eksen[5]), (0,150,150), 4)
                elif i==5:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[6],y_eksen[6]), (0,150,150), 4)
                elif i==6:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[8],y_eksen[8]), (0,150,150), 4)
                elif i==9:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[10],y_eksen[10]), (0,150,150), 4)                     
                elif i==11:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[12],y_eksen[12]), (global_colors[1][0],global_colors[1][1], global_colors[1][2]), 4)

                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[13],y_eksen[13]), (global_colors[2][0],global_colors[2][1], global_colors[2][2]), 4)
                    
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[23],y_eksen[23]), (global_colors[5][0],global_colors[5][1], global_colors[5][2]), 4)    
                elif i==12:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[14],y_eksen[14]), (global_colors[2][0],global_colors[2][1], global_colors[2][2]), 4)
                    if global_colors[2][1]<=0:
                        if global_colors[2][1]>=0 and global_colors[2][2]>=0:
                            global_colors[2][1] -= 20
                            global_colors[2][2] -= 20
                    global_colors[2][1] -=30


                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[24],y_eksen[24]), (global_colors[5][0],global_colors[5][1], global_colors[5][2]), 4)
                    #global_colors[5]=[255,255,81]#bitiş 210 210 0

                    if global_colors[5][2] == 1:
                        global_colors[5][0] -= 20
                        global_colors[5][1] -= 20

                    if global_colors[5][2] > 1:
                        global_colors[5][2] -= 20
                elif i==14:

                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[16],y_eksen[16]), (global_colors[3][0],global_colors[3][1], global_colors[3][2]), 4)                     
                #eller
                elif i==16:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[22],y_eksen[22]), (0, 255, 0), 4)
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[20],y_eksen[20]), (0, 255, 0), 4)
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[18],y_eksen[18]), (0, 255, 0), 4)
                    image = cv2.line(image, (x_eksen[20],y_eksen[20]), (x_eksen[18],y_eksen[18]), (0, 255, 0), 4)
                
                elif i==13:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[15],y_eksen[15]), (global_colors[3][0],global_colors[3][1], global_colors[3][2]), 4)
                
                    #3 => 13-15 14-16
                    #[255,45,45]#bitiş 150 0 0
                    if global_colors[3][1] > 15:
                        global_colors[3][1] -= 14
                        global_colors[3][2] -= 14
                    else:
                        global_colors[3][0] -= 30
            
                #eller
                elif i==15:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[21],y_eksen[21]), (0, 255, 0), 4)
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[19],y_eksen[19]), (0, 255, 0), 4)
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[17],y_eksen[17]), (0, 255, 0), 4)
                    image = cv2.line(image, (x_eksen[19],y_eksen[19]), (x_eksen[17],y_eksen[17]), (0, 255, 0), 4)         
        
                # kalça 
                elif i==24:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[23],y_eksen[23]), (global_colors[1][0],global_colors[1][1], global_colors[1][2]), 4)

                    global_colors[1][0]-=30
                    global_colors[1][1]-=30
                    global_colors[1][2]-=30
                    
                #25 le karşılıklı
                elif i==26:                
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[24],y_eksen[24]), (global_colors[6][0],global_colors[6][1], global_colors[6][2]), 4)
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[28],y_eksen[28]), (global_colors[7][0],global_colors[7][1], global_colors[7][2]), 4)          
                
                elif i==28:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[32],y_eksen[32]), (45, 45, 45), 4)
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[30],y_eksen[30]), (45, 45, 45), 4)
            
                elif i==30:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[32],y_eksen[32]), (45, 45, 45), 4)
                
                elif i==25:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[23],y_eksen[23]), (global_colors[6][0],global_colors[6][1], global_colors[6][2]), 4)
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[27],y_eksen[27]), (global_colors[7][0],global_colors[7][1], global_colors[7][2]), 4)
                    
                    
                    if global_colors[6][1] > 135 :
                        global_colors[6][1] -= 30

                    if global_colors[6][1]==135:
                        global_colors[6][0] -= 50
                        global_colors[6][2] -= 50



                    if global_colors[7][2] >= 30:
                            global_colors[7][2] -= 30

                    if global_colors[7][2]==2:
                        global_colors[7][1] -= 10
                        global_colors[7][0] -= 10

                #Ayak
                elif i==27:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[29],y_eksen[29]), (45, 45, 45), 4)
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[31],y_eksen[31]), (45, 45, 45), 4)
                elif i==29:
                    image = cv2.line(image, (x_eksen[i],y_eksen[i]), (x_eksen[31],y_eksen[31]), (45, 45, 45), 4)

            except:
                pass
            print(satir_atlama)
        if satir_atlama >=satir_atlama_sinir:
            cv2.imwrite("data2"+"/"+df['class'][satir_atlama]+"/"+str(satir_atlama)+".jpg",image)
            global_colors[2]=[255,180,220]#bitiş 236 0 118
            global_colors[3]=[255,45,45]#bitiş 150 0 0
            global_colors[4]=[125,249,255]#bitiş 0 189 196
            global_colors[5]=[255,255,81]#bitiş 210 210 0
            global_colors[6]=[110,255,110]#bitiş 0 113 0
            global_colors[7]=[255,158,62]#bitiş 221 111 0
            global_colors[8]=[66,66,255]#bitiş 0 0 145
            image = cv2.imread("beyaz.png")
            image = cv2.resize(image,(800,680))
            satir_atlama_sinir +=48
    else:
        continue

#image = cv2.line(image, (43,34), (65,100), (0,0,255), 8)



cv2.imshow("img,",image )

cv2.waitKey()
cv2.destrowyAllWindows()

