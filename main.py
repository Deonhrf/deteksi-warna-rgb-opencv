# import library yang digunankan 
import cv2
import numpy as np
import tkinter as tk # library untuk GUI
from tkinter import Label, Frame # komponen untuk GUI untuk menampilkan teks dan area
from PIL import Image, ImageTk # library yang digunakan untuk konversi gambar ke format tkinter





# Kondisi program berjalan 
run = True
color_label = None
deteksi_warna = 0

# Jantung program 
def inti_program() :
  global run, color_label, deteksi_warna

  ret, frame = vid.read()
  if not ret or frame is None:
      print("Error: No frame captured.")
      return

  # Memisahkan channel warna
  b = frame[:, :, 0]
  g = frame[:, :, 1]
  r = frame[:, :, 2]

    # Menghitung rata-rata nilai warna
  b_mean = np.mean(b)
  g_mean = np.mean(g)
  r_mean = np.mean(r)

    # Menentukan warna paling dominan
  if b_mean > g_mean and b_mean > r_mean:
      color = "Blue"
      rgb_text = f"RGB: (255, 0, 0)"
  elif g_mean > r_mean and g_mean > b_mean:
      color = "Green"
      rgb_text = f"RGB: (0, 255, 0)"
  else:
      color = "Red"
      rgb_text = f"RGB: (0, 0, 255)"

    # DIPERBAIKI: Logic deteksi lebih jelas
  if color != color_label:
      deteksi_warna += 1
      color_label = color

    # Mengonversi frame dari BGR ke RGB
  img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  img = Image.fromarray(img)
  img = img.resize((640, 480), Image.Resampling.LANCZOS)
  img = ImageTk.PhotoImage(img)

  # Menampilkan gambar dalam label
  img_label.config(image=img)
  img_label.image = img

  # Menampilkan warna dalam label
  label.config(text=color, bg=color.lower())

      
    # Update label informasi
  info_detail_label.config(text=f"Deteksi: {deteksi_warna} | {rgb_text}")
    
  root.after(10, inti_program)

def tutup_kamera() : 
    global run 
    run = False 
    try : 
        vid.release() # Menutup kamera
        cv2.destroyAllWindows() # keluar dari openCv
    except Exception as e :
        print("Kamera Mati")
    finally :
        root.destroy() # Keluar GUI

def keluar(input_user) : 
    global run
    try :
        if input_user.keysym.lower() == 'q':
            run = False
            tutup_kamera()
    except Exception as e : 
        pass
    

# GUI UTAMA 
root = tk.Tk()
root.title('Deteksi Warna RGB')
root.geometry('500x400')
root.resizable(False, False) # GuI tidak dapat diubah user
root.config(bg='black')


# Kode input user
root.bind('<q>', keluar)
root.bind('<Q>', keluar)


# Mengaktifikan kamera
vid = cv2.VideoCapture(0)


# header
header = Frame(root, bg='white', height=50)
header.pack(fill='x', padx=20, pady=8)

# Pada bagian teks didalam header
title_label = Label(header, text='System Pendekteksi Warna', font=('Halvetica', 20, 'bold'),
                   bg='white', fg='black')
title_label.pack(side='top', padx=10, pady=10)

# Label untuk menampilkan warna
label = Label(root, text="Color", font=("Helvetica", 20, "bold"), 
                   bg="white", height=2, fg="black")
label.pack(fill="x", padx=5, pady=3)

# Frame untuk video dengan border
video_frame = Frame(root, bg="#000000", relief="ridge", borderwidth=3)
video_frame.pack(fill="both", expand=True, padx=5, pady=5)

img_label = Label(video_frame, bg="black")
img_label.pack(fill="both", expand=True, padx=2, pady=2)

info_frame = Frame(root, bg="#3a3a3a", height=40)
info_frame.pack(fill="x", padx=5, pady=3)

info_detail_label = Label(info_frame, text="Deteksi: 0 | RGB: (0, 0, 0)", 
                         font=("Helvetica", 11), bg="#3a3a3a", fg="#00ff00")
info_detail_label.pack(side="left", padx=10, pady=8)

# Frame footer dengan instruksi
footer_frame = Frame(root, bg="#1a1a1a", height=40)
footer_frame.pack(fill="x", padx=5, pady=3)

info_label = Label(footer_frame, text="⌨️ Tekan 'Q' untuk berhenti", 
                  font=("Helvetica", 10), bg="#1a1a1a", fg="#ffff00")
info_label.pack(side="left", padx=10, pady=8)

# Start program 
inti_program()

# Menjalankan GUI
root.mainloop() 