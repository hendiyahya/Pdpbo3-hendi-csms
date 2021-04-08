# Saya Hendi Yahya mengerjakan evaluasi Tugas Praktikum 3 dalam mata kuliah
# Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak
# melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

#import TKINTER
from tkinter import *

#import Combo Box
from tkinter.ttk import Combobox

#Import Message Box
from tkinter import messagebox

#Import class mahasiswa
from mahasiswa import Mahasiswa

#Penampung Data
datamhs = []

root = Tk()
root.title("TP3 Hendi - College Student Management System")

#Frame Keterangan Aplikasi
def about():
    top = Toplevel()
    top.title("About")

    d_frame = LabelFrame(top, text="Tentang Aplikasi", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="CSMS - College Student Management System \n\n \
    Aplikasi ini berfungsi untuk menginput data mahasiswa dan melihat data yang telah dimasukkan.\
    \n\n Dibuat Oleh Hendi Yahya - 1902370\n", anchor="w").grid(row=0, column=0, sticky="w")
    d_exit = Button(d_frame, text="Kembali Ke Menu Utama", command=top.destroy)
    d_exit.grid(row=1, column=0)

#Keluar Aplikasi
def keluar():
    pesan = messagebox.askquestion('Konfirmasi', 'Keluar dari Aplikasi ?')
    if pesan == 'yes':
        root.destroy()
    elif pesan == 'no':
        pass




#Menambah Data
def tambahData():
    top = Toplevel()
    top.title("Form Tambah Data")

    d_pad = LabelFrame(top, padx=30, pady=30)
    d_pad.grid(row=1, column=0)

    d_frame = LabelFrame(d_pad, text="Tambah Data", padx=30, pady=30)
    d_frame.grid(row=1, column=0)

    Label(d_frame, text="Nama :" , anchor="w", width=15).grid(row=0, column=0)
    nama = Entry(d_frame, borderwidth=5)
    nama.grid(row=0, column=1,sticky="W")

    Label(d_frame, text="NIM :" , anchor="w", width=15).grid(row=1, column=0)
    nim = Entry(d_frame, borderwidth=5)
    nim.grid(row=1, column=1,sticky="W")

    Label(d_frame, text="Jenis Kelamin :" , anchor="w", width=15).grid(row=2, column=0)
    #Radio Button
    jk = StringVar()
    jk.set("Laki-Laki")
    r1 = Radiobutton(d_frame, text="Laki-Laki", value="Laki-Laki", variable=jk)
    r2 = Radiobutton(d_frame, text="Perempuan", value="Perempuan", variable=jk)
    r1.grid(row=2,column=1,sticky="W")
    r2.grid(row=3,column=1,sticky="W")
    #ambil dengan i.get()

    Label(d_frame, text="Fakultas :" , anchor="w", width=15).grid(row=4, column=0)
    #ComboBox
    fa = StringVar()
    datafak = ("FIP","FPIPS","FPBS","FPSD","FPMIPA","FPTK","FPOK","FPEB","K.D CIBIRU","K.D SUMEDANG","K.D TASIKMALAYA","K.D PURWAKARTA","K.D SERANG")
    cb = Combobox(d_frame, values=datafak)
    cb.set("Pilih Fakultas")
    cb.grid(row=4, column=1)

    Label(d_frame, text="Keaktifan :" , anchor="w", width=15).grid(row=5, column=0)
    #CheckBox
    chkValue1 = BooleanVar() 
    k1 = Checkbutton(d_frame, text = "UKM",var=chkValue1,onvalue=1,offvalue=0)
    k1.grid(row=5, column=1, sticky="W")
    
    chkValue2 = BooleanVar()  
    k2 = Checkbutton(d_frame, text = "BEM",var=chkValue2,onvalue=1,offvalue=0)
    k2.grid(row=6, column=1, sticky="W")
    
    chkValue3 = BooleanVar() 
    k3 = Checkbutton(d_frame, text = "Paguyuban",var=chkValue3,onvalue=1,offvalue=0)
    k3.grid(row=7, column=1, sticky="W")

    def validasi():
        if (nama.get()!="" and nim.get()!="" and cb.get()!="Pilih Fakultas") :
            save()
        else:
            messagebox.showinfo('Mohon Maaf', 'Data Belum Terisi Dengan Benar')

    def save():
        datamhs.append(Mahasiswa(nama.get(),nim.get(),jk.get(),cb.get(),chkValue1.get(),chkValue2.get(),chkValue3.get()))
        messagebox.showinfo('Selamat', 'Data Berhasil Tersimpan!')
        top.destroy()

    b_save = Button(d_frame, text="Simpan", command=validasi)
    b_save.grid(row=8, column=1,sticky="W")

#Tampilkan Data
def tampilkanData():
    tampil = Toplevel()
    tampil.title = ("Data")

    dframe = Frame(tampil)
    Label(dframe, text="Nama", width= 20).pack(side=LEFT,  expand=YES)
    Label(dframe, text="NIM", width= 20).pack(side=LEFT,  expand=YES)
    Label(dframe, text="Jenis Kelamin", width= 20).pack(side=LEFT,expand=YES)
    Label(dframe, text="Fakultas", width= 20).pack(side=LEFT,expand=YES)
    Label(dframe, text="Keaktifan UKM", width= 20).pack(side=LEFT,expand=YES)
    Label(dframe, text="Keaktifan BEM", width= 20).pack(side=LEFT,expand=YES)
    Label(dframe, text="Keaktifan Paguyuban", width= 20).pack(side=LEFT,expand=YES)
    dframe.pack()

    for i in datamhs:
        isi = Frame(tampil)
        Label(isi, text=i.nama, width= 20).pack(side=LEFT,  expand=YES)
        Label(isi, text=i.nim, width= 20).pack(side=LEFT,  expand=YES)
        Label(isi, text=i.jk, width= 20).pack(side=LEFT,expand=YES)
        Label(isi, text=i.fakultas, width= 20).pack(side=LEFT,expand=YES)
        if i.keaktifan1 == 1:
            Label(isi, text="Ya", width= 20).pack(side=LEFT,expand=YES)
        else:
            Label(isi, text="Tidak", width= 20).pack(side=LEFT,expand=YES)
        if i.keaktifan2 == 1:
            Label(isi, text="Ya", width= 20).pack(side=LEFT,expand=YES)
        else:
            Label(isi, text="Tidak", width= 20).pack(side=LEFT,expand=YES)
        if i.keaktifan3 == 1:
            Label(isi, text="Ya", width= 20).pack(side=LEFT,expand=YES)
        else:
            Label(isi, text="Tidak", width= 20).pack(side=LEFT,expand=YES)
        isi.pack()
#Hapus Data
def hapusData():
    datamhs.clear()
    messagebox.showinfo('Selamat', 'Data Berhasil Dihapus!')


#Halaman Utama
frame = Label(root, text="College Student Management System", font=("Arial Black",20))
frame.pack(padx=10, pady=10)

frame = Label(root, text="Aplikasi ini berfungsi untuk menginput data mahasiswa dan \
melihat data yang telah dimasukkan")
frame.pack(padx=10, pady=10)

b_add = Button(text="Tambah Data", command=tambahData, width=30, fg="white", bg="#00FF00", font=("Arial",16,'bold'))
b_add.pack(padx=10, pady=5)
b_show = Button(text="Tampilkan Data", command=tampilkanData, width=30, fg="white", bg="#0000FF", font=("Arial",16,'bold'))
b_show.pack(padx=10, pady=5)
b_del = Button(text="Hapus Data", command=hapusData, width=30, fg="white", bg="#FF0000", font=("Arial",16,'bold'))
b_del.pack(padx=10, pady=5)

opts = Label(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

b_exit = Button(opts, text="Tentang Aplikasi", command=about)
b_exit.grid(row=0, column=0, padx=10, pady=10)

b_exit = Button(opts, text="Keluar", command=keluar)
b_exit.grid(row=0, column=1, padx=10, pady=10)





root.mainloop()