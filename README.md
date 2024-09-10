Tautan PWS : yose-yehezkiel-snapbuy2.pbp.cs.ui.ac.id

## Implementation Step-by-step

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
![Bagan-request-client](https://i.ibb.co.com/C1v8LYK/Bagan-request-client.png)


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
seperti, autentikasi, manajemen pengguna, ORM, admin panel, dan
sistem routing sehingga dapat memudahkan pengembang, terutama pemula.

---

### Django disebut ORM

Django disebut ORM(Object-Relational Mapping) karena dapat menghubungkan objek-objek sehingga memudahkan pengembang untuk bekerja dengan basis data menggunakan konsep object. Django memudahkan untuk mengelola relasi antar objek, juga memudahkan untuk membuat dan memodifikasi skema basisdata menggunakan migrasi.
