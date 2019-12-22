def  inputan ():
    dari model.daftar_nilai impor tambah_kontak
    sementara ( Benar ):
        nama =  input ( " NAMA: " )
        jika nama ==  ' ' :
            print ( ' Nama tidak boleh kosong ' )
        lain :
            istirahat
    sementara ( Benar ):
        coba :
            nim =  int ( input ( " NIM: " ))
            jika nim ==  ' ' :
                print ( ' tambah Nim dengan Angka ' )
        kecuali  ValueError :
            print ( ' tambah Nim dengan Angka ' )
        lain :
            istirahat
    sementara ( Benar ):
        coba :
            tugas =  int ( input ( " TUGAS: " ))
            jika tugas ==  ' ' :
                print ( ' tambahkan TUGAS dengan Angka ' )
        kecuali  ValueError :
            print ( ' tambahkan TUGAS dengan Angka ' )
        lain :
            istirahat
    sementara ( Benar ):
        coba :
            uts =  int ( input ( " UTS: " ))
            jika uts ==  ' ' :
                print ( ' tulis UTS dengan Angka ' )
        kecuali  ValueError :
            print ( ' tulis UTS dengan Angka ' )
        lain :
            istirahat
    sementara ( Benar ):
        coba :
            uas =  int ( input ( " UAS: " ))
            jika uas ==  ' ' :
                p ( ' diterbitkan UAS dengan Angka ' )
        kecuali  ValueError :
            print ( ' masukkan UAS dengan Angka ' )
        lain :
            istirahat
    tambah_kontak (nama, nim, tugas, uts, uas)
    cetak ( " \ n     (A) dd (E) dit (D) hilangkan (S) earch (L) ist (Q) uit    " )


def  edit ():
    dari model.daftar_nilai impor edit_kontak
    edit_kontak ( nama = input ( " dipindahkan nama untuk mengedit data: " ))


def  delett ():
    dari model.daftar_nilai impor delet
    menghapus ( nama = input ( " disimpan nama untuk mengunduh data: " ))
    cetak ( " \ n     (A) dd (E) dit (D) hilangkan (S) earch (L) ist (Q) uit    " )


def  carive ():
    dari model.daftar_nilai cari impor
    cari ( nama = input ( " diterbitkan nama yang di cari: " ))
