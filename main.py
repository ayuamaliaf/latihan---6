ari view.view_nilai import nyari, cetak, header, notoption
dari view.input_nilai impor inputan, edit, delett
tajuk ()
sementara  Benar :

    c =  input ( " \ n Pilih Opsi: " )

    # PROGRAM KELUAR
    if c.lower () ==  ' q ' :
        print ( " .: TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI :. " )
        ext =  input ( " \ n Tekan ENTER untuk keluar " )
        jika ext ==  ' ' :
            istirahat
        lain :
            istirahat

    # CETAK DATA
    elif c.lower () ==  ' l ' :
        cetak ()

    # DATA MENAMBAH
    elif c.lower () ==  ' a ' :
        inputan ()

    # EDIT DATA
    elif c.lower () ==  ' e ' :
        edit ()

    # DATA MENCARI
    elif c.lower () ==  ' s ' :
        nyari ()

    # DATA HAPUS
    elif c.lower () ==  ' d ' :
        delett ()

    lain :
        notoption ()