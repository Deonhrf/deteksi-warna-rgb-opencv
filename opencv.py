# -----------------------------------------------------------------
# Berikut adalah code dasara untuk mengakses kamera dengan opencv
# -----------------------------------------------------------------


# import library yang digunankan 
import cv2
import numpy as np
import tkinter as tk # library untuk GUI
from tkinter import Label, Frame # komponen untuk GUI untuk menampilkan teks dan area
from PIL import Image, ImageTk # library yang digunakan untuk konversi gambar ke format tkinter

vid = cv2.VideoCapture(0) 

if not vid.isOpened() : 
  print('Eror')
  exit()

else :
  print('Sukses')

while True :
  ret,frame = vid.read() # membaca frame kamera
  cv2.imshow('frame', frame)

  # Tombol keluar dari program
  if cv2.waitKey(1) & 0xFF == ord('q') : 
    break


print("Program Keluar - Selesai")
vid.release() 
cv2.destroyAllWindows()