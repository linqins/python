#!/user/bin/python
# _*_ coding:UTF-8 _*_

import cv2
import sys
from PIL import Image

import tkinter
from tkinter import messagebox
top = tkinter.Tk()

#def helloCallBack():
#    messagebox.showinfo("Hell Python","Hell LLQ ")
    


def Open_USB_video(windown_name,camera_idx):
    i = 5
    cv2.namedWindow(windown_name) #设置打开的视频框的名称
    cap = cv2.VideoCapture(camera_idx)  #打开摄像头的ID
    while cap.isOpened():
        ok,frame = cap.read() # 读取一帧数据，该方法返回的两个参数，第一个布尔值
        if not ok :
            break
        
        cv2.imshow(windown_name,frame) #该方法就是实现图像显示
        
        #input = cv2.waitKey(1) & 0xFF
        #if  input == ord('g'): #监听键盘 按 G 保存图片
        #cv2.imwrite("./img/CAP_%d.jpg" % (i),frame)  #保存图片        
        #i = i+ 1
        #print("已保存")
            

        c = cv2.waitKey(1)
        if  c & 0xff == ord('q'): #监听键盘，按q 退出 
            
            break

    cv2.imwrite("./img/CAP_%d.jpg" % (i),frame)  #保存图片        
    print("已保存")
    #释放摄像头，并销毁程序
    cap.release()
    cv2.destroyAllWindows()
    print("已退出")


def Save_video( camrea_idx):
    #reload(sys)
    #sys.setdefaultencoding('utf-8')
    cap = cv2.VideoCapture(camrea_idx)
    cap.set(3,640)
    cap.set(4,480)
    cap.set(1,10)

    fourcc = cv2.cv2.CV_FOURCC('m','p','4','v')

    out = cv2.VideoWriter("./out.avi",fourcc,10,(640,480))
    while True:
        ret,frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame,1)
            a = out.write(frame)
            cv2.imshow("Frame",frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def Open_USB_video1():
    i = 5
    #cv2.namedWindow("LLQ") #设置打开的视频框的名称
    cap = cv2.VideoCapture(0)  #打开摄像头的ID
    while cap.isOpened():
        ok,frame = cap.read() # 读取一帧数据，该方法返回的两个参数，第一个布尔值
        if not ok :
            break
        
        cv2.imshow("windown_name",frame) #该方法就是实现图像显示
        
        #input = cv2.waitKey(1) & 0xFF
        #if  input == ord('g'): #监听键盘 按 G 保存图片
        cv2.imwrite("./img/CAP_%d.jpg" % (i),frame)  #保存图片        
        #i = i+ 1
        print("已保存")
            

        c = cv2.waitKey(1)
        if  c & 0xff == ord('q'): #监听键盘，按q 退出 
            
            break
    
    #释放摄像头，并销毁程序
    cap.release()
    cv2.destroyAllWindows()
    print("已退出")


if __name__ == '__main__':
    #Open_USB_video("Hell Cam",0)
    #Save_video(0)
    B = tkinter.Button(top,text="click",command=Open_USB_video1)
    B.pack()
    top.mainloop()

