from tensorflow.keras.models import load_model
import numpy as np
import cv2
import mediapipe as mp
from tensorflow.keras.preprocessing.image import load_img,img_to_array


degerler_list=[]
counter = 0 
stage = None
cap = cv2.VideoCapture(0)


model= load_model("best_model.h5")
print("modeli yükledim")
## Setup mediapipe instance
degerler_list=[] 

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

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
siyah  = cv2.imread("siyah.png")
siyah=cv2.resize(siyah,(320,240))
cizim_sayac=0
tespit="bulunamadı"
tahmin=""
say=0
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor image to RGB
        frame = cv2.resize(frame,(640,480))

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image.flags.writeable = False

        try:

        # Make detection
            results = pose.process(image)
        
            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
            try:
                landmarks = results.pose_landmarks.landmark


            except:
                pass
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) )

        
        
            pose_row = np.array([[landmark.x,landmark.y] for landmark in landmarks]).flatten()
            pose_row_list = pose_row.tolist()
            say +=1
            if say==10:
                say=0
                x_eksen=[]
                y_eksen=[]




                x_eksen.clear()
                y_eksen.clear()
                #Kordinatları alıp x ve y değerlerini listeye atılıyor
                

                #pose_row da olan kordinatları x ve y olarak ayırma işlemi bölümü
                for i in range(66):


                    if i%2==0:

                        x=int(300*(float(pose_row_list[i])))
                        x_eksen.append(x)
                    else:

                        y=int(220*(float(pose_row_list[i])))
                        y_eksen.append(y)





                for i in range(33):

                    #Kafa Kısmı

                    try:
                        if i==0:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[1],y_eksen[1]), (0,150,150), 4)
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[4],y_eksen[4]), (0,150,150), 4)     
                        
                        elif i==1:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[2],y_eksen[2]), (0,150,150), 4)
                        elif i==2:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[3],y_eksen[3]), (0,150,150), 4)
                        elif i==3:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[7],y_eksen[7]), (0,150,150), 4)
                        elif i==4:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[5],y_eksen[5]), (0,150,150), 4)
                        elif i==5:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[6],y_eksen[6]), (0,150,150), 4)
                        elif i==6:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[8],y_eksen[8]), (0,150,150), 4)
                        elif i==9:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[10],y_eksen[10]), (0,150,150), 4)                     
                        elif i==11:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[12],y_eksen[12]), (global_colors[1][0],global_colors[1][1], global_colors[1][2]), 4)

                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[13],y_eksen[13]), (global_colors[2][0],global_colors[2][1], global_colors[2][2]), 4)
                            
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[23],y_eksen[23]), (global_colors[5][0],global_colors[5][1], global_colors[5][2]), 4)    
                        elif i==12:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[14],y_eksen[14]), (global_colors[2][0],global_colors[2][1], global_colors[2][2]), 4)
                            if global_colors[2][1]<=0:
                                if global_colors[2][1]>=0 and global_colors[2][2]>=0:
                                    global_colors[2][1] -= 20
                                    global_colors[2][2] -= 20
                            global_colors[2][1] -=30


                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[24],y_eksen[24]), (global_colors[5][0],global_colors[5][1], global_colors[5][2]), 4)
                            #global_colors[5]=[255,255,81]#bitiş 210 210 0

                            if global_colors[5][2] == 1:
                                global_colors[5][0] -= 20
                                global_colors[5][1] -= 20

                            if global_colors[5][2] > 1:
                                global_colors[5][2] -= 20
                        elif i==14:

                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[16],y_eksen[16]), (global_colors[3][0],global_colors[3][1], global_colors[3][2]), 4)                     
                        #eller
                        elif i==16:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[22],y_eksen[22]), (0, 255, 0), 4)
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[20],y_eksen[20]), (0, 255, 0), 4)
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[18],y_eksen[18]), (0, 255, 0), 4)
                            siyah = cv2.line(siyah, (x_eksen[20],y_eksen[20]), (x_eksen[18],y_eksen[18]), (0, 255, 0), 4)
                        
                        elif i==13:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[15],y_eksen[15]), (global_colors[3][0],global_colors[3][1], global_colors[3][2]), 4)
                        
                            #3 => 13-15 14-16
                            #[255,45,45]#bitiş 150 0 0
                            if global_colors[3][1] > 15:
                                global_colors[3][1] -= 14
                                global_colors[3][2] -= 14
                            else:
                                global_colors[3][0] -= 30
                    
                        #eller
                        elif i==15:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[21],y_eksen[21]), (0, 255, 0), 4)
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[19],y_eksen[19]), (0, 255, 0), 4)
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[17],y_eksen[17]), (0, 255, 0), 4)
                            siyah = cv2.line(siyah, (x_eksen[19],y_eksen[19]), (x_eksen[17],y_eksen[17]), (0, 255, 0), 4)         
                
                        # kalça 
                        elif i==24:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[23],y_eksen[23]), (global_colors[1][0],global_colors[1][1], global_colors[1][2]), 4)
                            cizim_sayac +=1
                            global_colors[1][0]-=30
                            global_colors[1][1]-=30
                            global_colors[1][2]-=30
                            
                        #25 le karşılıklı
                        elif i==26:                
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[24],y_eksen[24]), (global_colors[6][0],global_colors[6][1], global_colors[6][2]), 4)
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[28],y_eksen[28]), (global_colors[7][0],global_colors[7][1], global_colors[7][2]), 4)          
                        
                        elif i==28:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[32],y_eksen[32]), (45, 45, 45), 4)
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[30],y_eksen[30]), (45, 45, 45), 4)
                    
                        elif i==30:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[32],y_eksen[32]), (45, 45, 45), 4)
                        
                        elif i==25:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[23],y_eksen[23]), (global_colors[6][0],global_colors[6][1], global_colors[6][2]), 4)
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[27],y_eksen[27]), (global_colors[7][0],global_colors[7][1], global_colors[7][2]), 4)
                            
                            
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
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[29],y_eksen[29]), (45, 45, 45), 4)
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[31],y_eksen[31]), (45, 45, 45), 4)
                        elif i==29:
                            siyah = cv2.line(siyah, (x_eksen[i],y_eksen[i]), (x_eksen[31],y_eksen[31]), (45, 45, 45), 4)

                    except:
                        pass
                print(cizim_sayac)
                if cizim_sayac==6:
                    cizim_sayac=0
                    cv2.imwrite("data2"+"/"+"2"+".jpg",siyah)
                    print("*********************************kayıt etti*********************************")
                    global_colors[2]=[255,180,220]#bitiş 236 0 118
                    global_colors[3]=[255,45,45]#bitiş 150 0 0
                    global_colors[4]=[125,249,255]#bitiş 0 189 196
                    global_colors[5]=[255,255,81]#bitiş 210 210 0
                    global_colors[6]=[110,255,110]#bitiş 0 113 0
                    global_colors[7]=[255,158,62]#bitiş 221 111 0
                    global_colors[8]=[66,66,255]#bitiş 0 0 145
                    siyah = cv2.imread("siyah.png")
                    siyah=cv2.resize(siyah,(320,240))
                    say=0
                    img = load_img("data2/2.jpg",grayscale=False,color_mode="rgb", target_size=(224, 224))
                    x = img_to_array(img)

                    tespit = model.predict_classes(x.reshape((1,224,224,3)),batch_size=16,verbose=0)

                                
        except:
            pass


        if tespit[0][0] == 1:
            tahmin="YASLI"
        elif tespit[0][0] == 0:
            tahmin="GENC"

        cv2.rectangle(image,(20,0),(590,65),(255,255,0),2)
        cv2.line(image,(320,0),(320,65),(255,255,0),2)
        cv2.line(image,(450,0),(450,65),(255,255,0),2)


        cv2.putText(image, "Yas Gurubu", (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(image, str(tahmin), (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('test', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()