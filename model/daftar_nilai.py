kontak = {}


def  tambah_kontak ( nama , nim , tugas , uts , uas ):
    akhir =  round (( float (tugas) *  0.3 ) + ( float (uts) *  0.35 ) + ( float (uas) *  0.35 ), 2 )
    kontak [nama] = nama, nim, tugas, uts, uas, akhir


def  edit_kontak ( nama ):
    jika nama dalam kontak.keys ():
        del kontak [nama]
        print ( " \ n ═══Masukan Data Pembaruan═══ " )
        dari view.input_nilai inputan impor
        inputan ()
    lain :
        cetak ( " ________________________ " )
        print ( " | Data {} tidak ditemukan | " .format (nama))
        cetak ( " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ " )
        cetak ( "     (A) dd (E) dit (D) elete (S) earch (L) ist (Q) uit    " )


def  cari ( nama ):
    jika nama dalam kontak.keys ():
        cetak ( " \ n ╔═════════════════╦══════════════════╦═══════ ╦═══════╦═══════╦═══════╗ " )
        cetak ( " ║ NAMA ║ NIM ║ TUGAS ║ UTS ║ UAS ║ AKHIR ║ " )
        cetak ( " ╠═════════════════╬══════════════════╬═══════╬═ ══════╬═══════╬═══════╣ " )
        mencetak ( " ║ {0 : 15 } ║ {1 : 16 } ║ {2 : 5 } ║ {3 : 5 } ║ {4 : 5 } ║ {5 : 5 } ║ " .format (nama, Kontak [nama di] [ 1 ], kontak [nama] [ 2 ], kontak [nama] [ 3 ], kontak [nama] [ 4 ], kontak [nama] [ 5 ])))
        cetak ( " ╚═════════════════╩══════════════════╩═══════╩═ ══════╩═══════╩═══════╝ " )
    lain :
        cetak ( " ________________________ " )
        print ( " | Data {} tidak ditemukan | " .format (nama))
        cetak ( " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ " )


def  delet ( nama ):
    jika nama dalam kontak.keys ():
        del kontak [nama]
        mengembalikan  True
    lain :
        cetak ( " ________________________ " )
        print ( " | Data {} tidak ditemukan | " .format (nama))
        cetak ( " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ " )
        mengembalikan  False

