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
![Bagan-request-client](https://github.com/maskrio/snap_buy/blob/main/screenshots/Bagan-request-client.png)


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
seperti, authentication, manajemen pengguna, ORM, admin panel,
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

1. Menambahkan template `base.html` pada `root` sebagai kerangka views. 
2. Mebuat id pada model di `models.py` menjadi `models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)` untuk keamanan id.
3. Membuat `main/forms.py` untuk menerima entry. 
4. Membuat template forms pada main `create_product_entry.html` dan membuat fungsi baru pada `main/views.py` untuk memproses request membuat product entry.
5. Membuat fungsi yang akan mengembalikan data, `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`. 
6. Mengatur rute pada `main/urls.py` yang akan mengatur requests.

---
### Screenshot postman
#### show json
![show_json](https://github.com/maskrio/snap_buy/blob/main/screenshots/show_json.png)

#### show xml
![show_xml](https://github.com/maskrio/snap_buy/blob/main/screenshots/show_xml.png)

#### Show json by id
![show_json_by_id](https://github.com/maskrio/snap_buy/blob/main/screenshots/show_json_by_id.png)

#### show xml by id
![show_by_id_xml](https://github.com/maskrio/snap_buy/blob/main/screenshots/show_xml_by_id.png)

## TUGAS 4

### Django `UserCreationForm`

 Django `UserCreationForm` adalah form bawaan Django untuk membuat pengguna baru. Form ini sudah menyediakan fitur dasar username dan password, disertai validasi password.

 Kelebihan Django `UserCreationForm` adalah, sebagai berikut :
 1. Mudah digunakan, 
 2. Validasi password langsung, 
 3. Bisa langsung digunakan dengan fitur authentication django lainnya, seperti login, 
 4. Bisa menambahkan field sesuai kebutuhan.

 Kekurangan Django `UserCreationForm` adalah, sebagai berikut : 
 1. `UserCreationForm` hanya menyediakan field dasar(username, password), field lainnya harus ditambahkan secara manual, 
 2. Desain Form sederhana, perlu penyesuaian tampilan UI agar lebih user-friendly,
 3. Menggunakan `username` sebagai identifier, sehingga perlu penyesuaian apabila ingin membuat email atau yang lain sebagai identifier,
 4. Tidak mendukung authentication sosial media, seperti facebook atau google, sehingga harus ada integrasi secara manual.

 Django `UserCreationForm` mudah dipakai, namun ada keterbatasan yang dimilikinya, sehingga perlu adanya penyesuaian tambahan.

###  `HttpResponseRedirect()` dan `redirect()`

`HttpResponseRedirect()` dan `redirect()` keduanya digunakan untuk mengalihkan ke URL lain. Keduanya merupakan fungsi yang disediakan Django, namun ada sedikit perbedaan diantaranya. `redirect()` lebih fleksibel dari `HttpResponseRedirect()`, karena `HttpResponseRedirect()` harus diisi oleh URL sebagai argumennya

```
def login_page(request) :
    return HttpResponseRedirect('/profile/login/)
```

sedangkan `redirect()` tidak harus mengisinya dengan url saja, melainkan bisa langsung diisi dengan nama view atau objek, dan django akan mengonversinya menjadi url

```
def login_page(request) :
    return redirect('/profile/login/')
```
```
def login_page(request) :
    return redirect('login')
```


### Menghubungkan model `Product` dengan `User`

1. Pada `main/models.py`, lakukan import user dan inisialisasi user dan membuat relation dengan model Product menyimpan user sebagai ForeignKey dari User.
```py
...
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```
2. Menghubungkan entry form dengan user.
```
def create_product_entry(request) :
    form = ProductEntryForm(request.POST or None) 
    
    if form.is_valid() and request.method == "POST" :
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form} 
    return render(request, "create_product_entry.html", context) 
```

Dengan 2 langkah diatas, telah membuat hubungan antara entry form dengan user. Entry form bisa dibuat banyak untuk 1 user tertentu. Relasi ini adalah relasi many-to-one. Entry form pada `product_entry.user` diinisialisasi oleh `request.user` untuk menandakan object entry ini dimiliki oleh user yang sedang login.

Terakhir, lakukan migrasi
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Authentication vs Authorization

Authentication adalah proses memverifikasi identitas pengguna. Authentication memastikan bahwa pengguna benar-benar adalah pengguna tersebut, bukan orang lain yang ingin menjadi pengguna tersebut. Caranya adalah melewati proses login, agar pengguna yang tahu passwordnya saja yang dapat menjadi pengguna tersebut. Proses login ini akan dibandingkan dengan kredensial pada basis data untuk mencocokan pengguna dengan yang telah terdaftar di sistem. 

Authorization adalah proses memeriksa akses pengguna terhadap platform setelah identtitas diverifikasi(**telah melewati Authentication**). Authorization menentukan apa yang boleh dan tidak boleh dilakukan/diakses oleh pengguna tersebut. Contohnya seperti perbedaan user dengan admin, admin memiliki akses yang lebih banyak guna mengontrol jalannya platform, sedangkan user tidak diperbolehkan mengontrol platform.

Keduanya penting karena **authentication** memastikan aplikasi hanya berinteraksi dengan pengguna yang sah dan **Authorization** melindungi sumber daya dan data sensitif dengan hanya memberikan hak akses kepada pengguna tertentu.

Django mengimplementasi Authentication dengan cara menyimpan data user yang dapat diakses dengan `request.user` lalu kita cukup menggunakan fungsi `login()`
```py
form = AuthenticationForm(data=request.POST)
if form.is_valid():
    user = form.get_user()
    login(request, user)
```

Authorization di Django diimplementasikan melalui izin dan groups. Contoh perizinan seperti `@login_required`, memastikan pengguna sudah login atau yang lainnya seperti `@permission_required`, memastikan pengguna memiliki izin. Contoh group adalah seperti menerapkan `is_staff` atau grouping lainnya.

### Django mengingat pengguna yang telah login

Django mengingat pengguna yang telah login melalui session dan cookies. Caranya adalah seperti:
1. Session id disimpan di cookie,
2. Session data di server, dicocokan untuk verifikasi,
3. Cookie authentication, yang ketika logout akan dihapus,
4. Django middleware yang secara otomatis menambahkan dan mengelola sesi tiap kali pengguna mengirim permintaan.

### Kegunaan lain cookies

Kegunaan lain cookies adalah sebagai berikut:
1. Menyimpan preferensi pengguna, seperti pengaturan font, tema warna, bahasa, dan lain-lain, 
2. Melacak aktivitas pengguna,
3. Menyimpan data sementara, seperti last login.

### Apakah semua cookies aman digunakan?

Tidak semua cookies aman. Oleh karena itu, penting untuk memahami risiko serta cara memastikan keamanan cookies. Cookies yang sensitif seperti sessionID harus ditandai Secure untuk memastikan cookie dikirim dengan HTTPS yang terenkripsi. Jika Cookie sensitif tidak diproteksi dengan baik, maka cookie tidak aman untuk digunakan.

### Implementasi Step-by-step

#### Mengimplementasikan fungsi registrasi, login, dan logout.
1. Menambahkan `@login_required` pada fungsi `show_main()` di `main/views.py`
2. Menambahkan fungsi login, register, dan logout pada `main/views.py`
```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
  
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
3. Menambahkan routing pada `main/urls.py`
```py
...
from main.views import login_user, logout_user, register
...
urlpatterns = [
    ...
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
]
```

4. Membuat template di `main/templates` yaitu `login.html` dan `register.html`.

5. Lalu saya Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

#### Menghubungkan model `Product` dengan `User` 

1. Pada `main/models.py`, lakukan import user dan inisialisasi user dan membuat relation dengan model Product menyimpan user sebagai ForeignKey dari User.
```py
...
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```
2. Menghubungkan entry form dengan user.
```
def create_product_entry(request) :
    form = ProductEntryForm(request.POST or None) 
    
    if form.is_valid() and request.method == "POST" :
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form} 
    return render(request, "create_product_entry.html", context) 
```

Dengan 2 langkah diatas, telah membuat hubungan antara entry form dengan user. Entry form bisa dibuat banyak untuk 1 user tertentu. Relasi ini adalah relasi many-to-one. Entry form pada `product_entry.user` diinisialisasi oleh `request.user` untuk menandakan object entry ini dimiliki oleh user yang sedang login.

Terakhir, lakukan migrasi
```
python3 manage.py makemigrations
python3 manage.py migrate
```

#### Menampilkan detail informasi pengguna seperti username
untuk menampilkan detail data pengguna, kita perlu mengakses objek `request.user` (user yang sedang login) dan mengakses data yang diinginkan seperti `username`.
```py
...
    context = {
    'name': request.user.username,
    }
...
```

#### Menerapkan cookies
1. Simpan cookie yang diinginkan (last login)
```py
...
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
  
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
...
```
2. Jika ingin ditampilkan, ambil cookienya.
```py
def show_main(request):
    product_entries = Product.objects.all()
    
    context = {
        'npm' : '2306152342',
        'name': request.user.username,
        'class': 'PBP E',
        'product_entries': product_entries,
        'last_login': request.COOKIES['last_login'],
    }
```
3. Tambahkan saja pada template
```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```


---
## Tugas 5

### Urutan pengambilan CSS selector

Bila suatu elemen HTML dipengaruhi beberapa selector, maka prioritas selector yang lebih rendah tidak akan memengaruhi selector css yang lebih tinggi. Berikut adalah urutas selector css dari tertinggi ke rendah.

#### Inline CSS
```html
<p style="color: red;">Ini teks merah.</p>
```
#### ID selector
```css
#myId {
    color: blue;
}
```

#### Class, Attribute, dan Pseudo-class Selector
```css
.myClass {
    color: green;
}
```
#### Element dan Pseudo-element Selector
```css
p {
    color: black;
}
```

#### Universal Selector
```css
* {
    margin: 0;
}
```

### Pentingnya Responsive Design
Responsive design adalah konsep yang memungkinkan tampilan situs web beradaptasi dengan berbagai ukuran layar dan perangkat. Konsep ini sangat penting karena memberikan pengalaman User yang lebih baik, pengguna lebih fleksibel untuk bisa membuka situs web dari *smartphone*, PC, tablet, maupun perangkat lainnya.

### Margin, Border, Padding

Strukturnya adalah seperti ini

```
+-------------------------+
|         Margin          |   <-- Margin
|  +-------------------+  |
|  |      Border       |  |   <-- Border
|  |  +-------------+  |  |
|  |  |   Padding   |  |  |   <-- Padding
|  |  |  +-------+  |  |  |
|  |  |  |Content|  |  |  |   <-- Content
|  |  |  +-------+  |  |  |
|  |  |             |  |  |
|  |  +-------------+  |  |
|  |                   |  |
|  +-------------------+  |
|                         |
+-------------------------+
```

Cara untuk mengimplementasikannya adalah seperti ini
``` css
div {
    margin: 20px;         /* Jarak di luar border */
    padding: 15px;        /* Jarak antara konten dan border */
    border: 2px solid red; /* Border dengan ketebalan 2px dan warna merah */
}
```

### Flexbox dan Grid Layout
Flexbox adalah model tata letak **satu dimensi** yang diracang untuk mengatur elemen-elemen dalam baris atau kolom yang fleksibel. Flexbox memudahkan pengaturan jarak antar elemen, alignment, serta pembagian ruang secara proposional. Flexbox memudahkan agar dapat menyesuaikan ukurannya secara otomatis berdasarkan ruang yang ada.

Grid layout juga adalah model tata letak **dua dimensi** yang memungkinkan pengaturan elemen secara horizontal dan vertikal. Dengan grid, kita dapat mengatur tata letak yang lebih kompleks dan terstruktur dengan pengaturan baris kolom yang mudah.

**Flexbox** ideal untuk tata letak satu dimensi, misalnya menyusun elemen dalam baris atau kolom dengan alignment yang fleksibel. 

**Grid Layout** lebih cocok untuk tata letak dua dimensi yang lebih kompleks, di mana Anda perlu mendefinisikan kolom dan baris dengan presisi.


### Implementasi Step-by-step

1. Menambahkan fungsi `edit_product` dan `delete_product` pada `main/views.py`
2. Menambahkan routing pada `urls.py`
3. Menambahkan `navbar.html` pada `templates`
4. Menambahkan script CDN tailwind ke `templates/base.html`
5. Menambahkan statis `global.css` di `static/css`
6. Mengatur ulang seluruh tampilan pada `main/templates`
7. Menambahkan `card_info.html`, `card_product.html`, dan `edit_product.html` ke `main/templates`
