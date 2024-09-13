Tautan PWS : yose-yehezkiel-snapbuy.pbp.cs.ui.ac.id

## Tugas 2

### Implementation Step-by-step

#### Membuat project django baru.

1. Membuat directory baru `snap_buy`
```
mkdir snap_buy
cd snap_buy 
```

2. Membuat virtual environtment dan aktivasi. Tujuan dari aktivasi ini supaya *package* dan  tidak bertabrakan dengan versi yang lain pada komputer
```
python3 -m venv env

source env/bin/activate
```

3. Membuat `requirements.txt` dan menambahkan beberapa *dependancies*. File `requirements.txt` saya sebagai berikut:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

4. Installasi *dependancies* dengan `requirements.txt`
```
pip install -r requirements.txt
```

5. Membuat project django baru bernama `snap_buy`
```
django-admin startproject snap_buy .
```

6. Mengganti `ALLOWED_HOSTS` pada `settings.py`, untuk mengizinkan host untuk mengakses aplikasi web. Host yang diizinkan, seperti lokal host, dan site. 

#### Mengatur project django

1. Membuat aplikasi main
```
python manage.py startapp main
```
2. Menambahkan `main` ke `INSTALLED_APPS` di `snap_buy/settings.py`
3. Menambahkan `path('', include('main.urls'))` pada `snap_buy/urls.py` agar `urls.py` bisa mengatur rute menuju aplikasi `main`.
4. Membuat model pada aplikasi `main` dengan nama `Product` dan menambahkan beberapa atribut. Model dibuat di `models.py` untuk menginisiasi model yang diinginkan. 
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
```

5. Melakukan routing pada aplikasi `main` dengan mengatur `main/urls.py`. Pada tugas ini, saya menambahkan fungsi `show_main` pada `main/views.py` dan menambah rute dari `main/urls.py` ke fungsi tersebut.

#### Melakukan deployment PWS
1. Menambahkan `remote` PWS supaya bisa push ke `remote`. 
```
git remote add pws https://pbp.cs.ui.ac.id/yose.yehezkiel/snapbuy2
```

2. Melakukan push ke PWS
```
git push pws main:master
```

3. PWS akan melakukan build dan web dapat diakses melalui tautan.

---

### Bagan *request client*
![Bagan-request-client](https://github.com/maskrio/snap_buy/blob/main/Bagan-request-client.png)


---

### Fungsi Git

Git berfungsi dalam banyak hal di dalam pengembangan perangkat lunak, salah satunya adalah sebagai berikut: 

- Kontrol versi, bisa melihat files yang ditambahkan di versi
tertentu dan juga bisa di kembalikan apa bila diperlukan,
- Kolaborasi tim, lebih mudah bekerja sama karena tim bisa saling
melihat pekerjaan rekannya juga melakukan Branching supaya bisa melakukan pekerjaan di branch masing-masing, dan
- Mengharuskan resolving conflicts sehingga apabila bekerja di dalam tim,
mudah sekali untuk resolve conflicts agar tidak terjadi masalah pada aplikasi.

---

### Alasan Django 

Django sudah memiliki struktur yang jelas dan mudah
diaplikasikan. Django juga sudah memiliki banyak fitur
seperti, autentikasi, manajemen pengguna, ORM, admin panel,
sistem routing, testing, dan lain-lain sehingga tidak perlu membangunnya dari awat dan memudahkan pengembang, terutama pemula.

---

### Model Django disebut ORM

Model Django disebut ORM(Object-Relational Mapping) karena dapat menghubungkan objek-objek sehingga memudahkan pengembang untuk bekerja dengan basis data menggunakan konsep object. Tidak perlu untuk menulis code SQL secara langsung, namun cukup menggunakan objek python untuk berinteraksi dengan basis data. Model Django juga menerapkan dukungan relasi antar model untuk membuat skema basis data yang baik.


## TUGAS 3

### Perlunya data delivery

Data delivery dibutuhkan untuk mengirimkan/menerima data interaksi dari user dan platform. Contohnya user mengirimkan data berupa HTTP get request untuk mendapatkan homepage website, lalu akan dikembalikan response berupa HTTP response untuk menjawab permintaan user tersebut.  Data delivery ini biasanya di dalam format data HTML, XML, JSON.

--- 

### Mengapa JSON lebih populer dibanding XML?

JSON(JavaScript Object Notation) dirancang untuk bekerja sama dengan bahasa pemrograman modern, sehingga JSON lebih mudah diproses oleh sebagian besar bahasa pemrograman tanpa perlu banyak konversi. JSON memiliki struktur sederhana dan mudah dibaca/ditulis oleh manusia atau mesin. JSON hanya terdiri dari object, array dan key-value(semacam map) yang cukup intuitif. 

XML memiliki format yang lebih kompleks dan berbasis tag (mirip dengan html), yang sering kali menghasilkan dokumen besar dan sulit dibaca. Format XML ini yang menyebabkan kompleksitas dalam parsing data, perlu lebih banyak langkah untuk melakukan parsing. Hal ini juga menyebabkan XML lebih lambat untuk di proses.

Intinya JSON lebih sederhana dan lebih mudah dipahami oleh manusia. JSON juga lebih cepat diproses.

---


### Perlunya `is_valid()`

`is_valid()` berguna untuk memvalidasi data form yang dikirim oleh pengguna, memastikan data tipenya sesuai, memastikan data tidak melebihi batasan nilai, menangani error, memastikan tidak ada malicious code, dan lain-lain yang berguna untuk mengatasi hal yang tidak diinginkan karena data yang tidak sesuai dari input user.

---

### Perlunya CSRF Token

CSRF Token pada django digunakan sebagai mekanisme keamanan untuk melindungi platform dari serangan CSRF (Cross-Site Request Forgery). CSRF adalah jenis serangan di mana penyerang mengeksploitasi session user untuk melakukan tindakan yang tidak sah atas nama user tersebut, misalkan mengirimkan form berbahaya tanpa sepengetahuan user tersebut. 

CSRF Token disertakan pada setiap kali user mengunjungi halaman yang memerlukan form (login, sign in). Saat pengguna mengirim form tersebut, token CSRF dikirim bersama form. Kemudian, Django memeriksa apakah token yang diterima cocok dengan token yang disimpan di session user. CSRF divalidasi sebelum diteruskan untuk diproses dan apabila tidak valid, akan mengembalikan response **403 (forbidden)** tanpa diteruskan.
Dengan ini, dapat dipastikan bahwa session user adalah benar-benar user bukan orang lain yang mempunyai session user tersebut.

---

### Implementation step-by-step

#### Membuat `form` untuk menambahkan objek model

1. Menambahkan template `base.html` pada `root`, dan juga template `create_product_entry.html` pada `main`.
