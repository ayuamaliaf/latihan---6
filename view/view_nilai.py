dari model.daftar_nilai impor kontak

 header def ():
    cetak ( " ╔══════════════════════════════════════════════ ═══════════════════════════╗ " )
    cetak ( " ╠════════════════════ PROGRAM DATA MAHASISWA DATA INPUT ══════════════════════ ═╣ " )
    cetak ( " ╠═══════════╦════════════╦════════════╦════════ ═════╦══════════╦══════════╣ " )
    cetak ( " ║ (A) dd ║ (E) dit ║ (D) hapus ║ (S) earch ║ (L) ist ║ (Q) uit ║ " )
    cetak ( " ╚═══════════╩════════════╩════════════╩════════ ═════╩══════════╩══════════╝ " )


def  notoption ():
    cetak ( " __________________________ " ))
    print ( " | Pilih opsi yang tersedia | " )
    cetak ( " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ " )
    cetak ( "     (A) dd (E) dit (D) elete (S) earch (L) ist (Q) uit    " )


def  cetak ():
    cetak ( " \ n ╔════════════════════════════════════════════ ═════════════════════════════╗ " )
    print ( " ╠═════════════════════════ DAFTAR DATA MAHASISWA ══════════════════ ═══════╣ " )
    cetak ( " ╠════╦═════════════════╦══════════════════╦════ ═══╦═══════╦═══════╦═══════╣ " )
    cetak ( " ║ TIDAK ║ NAMA ║ NIM ║ TUGAS ║ UTS ║ UAS ║ AKHIR ║ " )
    cetak ( " ╠════╬═════════════════╬══════════════════╬════ ═══╬═══════╬═══════╬═══════╣ " )
    tidak =  1
    untuk tabel di kontak.values ​​():
        cetak ( " ║ {0 : 3 } ║ {1 : 15 } ║ {2 : 16 } ║ {3 : 5 } ║ {4 : 5 } ║ {5 : 5 } ║ {6 : 5 } ║ "
              .format (no, tabel [ 0 ], tabel [ 1 ], tabel [ 2 ], tabel [ 3 ], tabel [ 4 ], tabel [ 5 ]))
        no + =  1
    cetak ( " ╚════╩═════════════════╩══════════════════╩════ ═══╩═══════╩═══════╩═══════╝ " )
    cetak ( " \ n     (A) dd (E) dit (D) hilangkan (S) earch (L) ist (Q) uit    " )


def  nyari ():
    dari view.input_nilai impor carive
    karies ()
    cetak ( "     (A) dd (E) dit (D) elete (S) earch (L) ist (Q) uit    " )