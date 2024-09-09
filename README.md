Nama : Yose Yehezkiel Maranata

NPM : 2306152342

Kelas : PBP E

Tautan PWS : yose-yehezkiel-snapbuy2.pbp.cs.ui.ac.id

1. Pertanyaan

    Membuat sebuah proyek Django baru
        - membuat repositori baru
        - melakukan set up environtment pada local supaya bisa build project snap_buy 
    Membuat aplikasi dengan nama main
        - menggunakan perintah `python manage.py startapp main`
    Melakukan routing pada proyek agar dapat menjalankan aplikasi main
        - menambahkan main pada `INSTALLED_APPS` pada `settings.py`
        - menambahkan routing pada direktori `snap_buy` pada `urls.py` supaya bisa route ke main
    Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        - membuat direktori `templates` dan membuat main.html 
        - memasukkan nilai variable ke dalam `views.py` di dalam fungsi `show_main` agar ketika fungsi tersebut dipanggil, response yang dikembalikan adalah bersama dengan context yang sudah dimasukkan.
    Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        - menambahkan show_main untuk routing ke views.py
    Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        - membuat project baru pada PWS
        - menambahkan remote pws 
        - push pada pws
2. 

3. 
    git berfungsi dalam banyak hal di dalam pengembangan perangkat lunak
        - kontrol versi, bisa melihat files yang ditambahkan di versi tertentu dan juga bisa di kembalikan apa bila diperlukan
        - kolaborasi tim, lebih mudah bekerja sama karena tim bisa saling melihat pekerjaan rekannya
        - mengharuskan resolving conflicts sehingga apabila di dalam tim, mudah sekali untuk resolve conflicts agar tidak terjadi masalah
4. 
    mungkin karena django sudah memiliki struktur yang jelas dan mudah diaplikasikan untuk pemula. Django juga memiliki banyak fitur seperti, autentikasi, manajemen pengguna, ORM, admin panel, dan sistem routing sehingga dapat memudahkan pengembang.  
5. 
    Django disebut ORM(Object-Relational Mapping) karena dapat menghubungkan objek-objek sehingga memudahkan pengembang untuk bekerja dengan basis data menggunakan konsep object. Django memudahkan untuk mengelola relasi antar objek, juga memudahkan untuk membuat dan memodifikasi skema basisdata menggunakan migrasi.
