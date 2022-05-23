# Tutorial Flask
`Flask` adalah sebuah web framework yang ditulis dengan bahasa `Python` dan tergolong sebagai jenis `microframework`. Flask berfungsi sebagai kerangka kerja aplikasi dan tampilan dari suatu web. Dengan menggunakan Flask dan bahasa Python, pengembang dapat membuat sebuah web yang terstruktur dan dapat mengatur behaviour suatu web dengan lebih mudah. Flask termasuk pada jenis microframework karena tidak memerlukan suatu alat atau pustaka tertentu dalam penggunaannya.

Berikut ini merupakan tutorial yang akan memandu Pengguna baru dalam membuat aplikasi blog dasar yang disebut `Flask`. Pengguna akan dapat mendaftar, masuk, membuat posting, dan mengedit atau menghapus posting mereka sendiri. Pengguna juga akan dapat mengemas dan menginstal aplikasi di komputer lain.

## Tata Letak Proyek
Buat direktori proyek terlebih dahulu menggunakan perintah :
```
mkdir flask-tutorial
cd flask-tutorial
```

Kemudian menyiapkan `virtual environment` dan menginstall library `Flask` untuk proyek yang ingin dibuat. Di dalam direktori yang telah dibuat, buat virtual environment untuk Flask menggunakan perintah :
``` 
py -3 -m venv venv
```

Setelah membuat virtual environment, aktifkan environment Flask menggunakan perintah :
```
venv\Scripts\activate
```
Tampilan Command Prompt yang kita gunakan akan berubah dan menunjukkan nama virtual environment yang telah diaktifkan

Dalam virtual environment yang telah diaktifkan, gunakan perintah ini untuk menginstall library Flask :
```
pip install Flask
```
Setelah menginstall library Flask, silahkan menguji menggunakan satu file sederhana dengan nama `hello.py` :
```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```
Kemudian set environment variabel FLASK_APP di Command Prompt menggunakan perintah :
```
set FLASK_APP=hello
```
Kemudian run aplikasi Flask dengan :
```
flask run
```
Output akan mencetak pesan konfirmasi dan alamat aplikasi Flask yang telah dibuat. Contohnya :
```
(venv) C:\Users\ASUS\flask-tutorial\flask-tutorial>flask run
 * Serving Flask app 'hello' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

Namun, ketika sebuah proyek semakin besar, menjadi sangat sulit untuk menyimpan semua kode dalam satu file. Proyek Python menggunakan package untuk mengatur kode ke dalam beberapa modul yang dapat diimpor jika diperlukan.

Direktori proyek akan berisi :
- `flask/`, package Python yang berisi kode aplikasi dan file.
- `tests/`, direktori yang berisi modul pengujian.
- `venv/`, virtual environment Python tempat Flask dan dependensi lainnya diinstal.
- File instalasi memberi tahu Python cara menginstal proyek.
- Konfigurasi kontrol versi, seperti `git`. Pengguna harus membiasakan menggunakan beberapa jenis kontrol versi untuk semua proyek, berapa pun ukurannya.
- File proyek lain yang mungkin Pengguna tambahkan di masa mendatang.

Pada akhirnya, tata letak proyek Pengguna akan terlihat seperti ini:
```
/home/user/Projects/flask-tutorial
├── flask/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

## Pengaturan Aplikasi
Aplikasi `Flask` adalah turunan dari kelas Flask. Segala sesuatu tentang aplikasi, seperti konfigurasi dan URL, akan didaftarkan dengan kelas ini.

Cara paling mudah untuk membuat aplikasi Flask adalah dengan membuat `instance global Flask` langsung di bagian atas, seperti bagaimana "Hello, World!" contoh lakukan pada projek sebelumnya. Meskipun ini sederhana dan berguna dalam beberapa kasus, ini dapat menyebabkan beberapa masalah rumit saat proyek berkembang.

Alih-alih membuat `instance Flask` secara global, Pengguna akan membuatnya di dalam suatu fungsi. Fungsi ini dikenal sebagai `application factory`. Setiap konfigurasi, registrasi, dan pengaturan lain yang dibutuhkan aplikasi akan terjadi di dalam fungsi, kemudian aplikasi akan dikembalikan.

Berikut ini salah satu contoh penggunaan fungsi `application factory` :
```python
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```
Perintah `create_app` adalah sebuah fungsi application factory. Di dalam fungsi ini terdapat beberapa perintah yaitu :
1. `app = Flask(__name__, instance_relative_config=True)` digunakan untuk menciptakan instance Flask.
    - `__name__` adalah nama modul Python yang digunakan. Aplikasi perlu mengetahui di mana lokasinya untuk menyiapkan beberapa jalur, dan `__name__` merupakan cara yang nyaman untuk memberitahukannya.
    - `instance_relative_config=True` memberi tahu aplikasi bahwa file konfigurasi relatif terhadap folder instance . Folder instance terletak di luar paket dan dapat menyimpan data lokal yang tidak boleh dikomit ke kontrol versi, seperti rahasia konfigurasi dan file database.

2. `app.config.from_mapping()` digunakan untuk menyetel beberapa konfigurasi default yang akan digunakan aplikasi:
    - `SECRET_KEY` digunakan oleh Flask dan ekstensi untuk menjaga keamanan data. Ini diatur untuk `'dev'` memberikan nilai yang nyaman selama pengembangan, tetapi harus diganti dengan nilai acak saat digunakan.
    - `DATABASE` adalah jalur tempat file database `SQLite` akan disimpan. Itu di bawah `app.instance_path`, yang merupakan jalur yang telah dipilih Flask untuk folder instance.

3. `app.config.from_pyfile()` digunakan untuk menimpa konfigurasi default dengan nilai yang diambil dari file `config.py` di folder instance jika ada. Misalnya, saat menerapkan, ini dapat digunakan untuk mengatur file `SECRET_KEY`.
    - `test_config` juga dapat diteruskan ke factory, dan akan digunakan sebagai pengganti konfigurasi instans. Ini agar pengujian yang akan Pengguna tulis nanti dalam tutorial dapat dikonfigurasi secara independen dari nilai pengembangan apa pun yang telah dikonfigurasikan.

4. `os.makedirs()` digunakan untuk memastikan bahwa `app.instance_path` ada. Flask tidak membuat folder instance secara otomatis, tetapi perlu dibuat karena proyek Pengguna akan membuat file database SQLite di sana.

5. `@app.route()` digunakan untuk membuat rute sederhana sehingga Pengguna dapat melihat aplikasi bekerja sebelum masuk ke tutorial selanjutnya. Ini membuat koneksi antara URL `/hello` dan fungsi yang mengembalikan respons, string dalam kasus ini adalah `'Hello, World!'`.

## Menentukan dan Mengakses Database
Aplikasi akan menggunakan database `SQLite` untuk menyimpan pengguna dan posting. Python hadir dengan dukungan bawaan untuk SQLite dalam modul `sqlite3`. SQLite nyaman karena tidak memerlukan pengaturan server database terpisah dan sudah terintegrasi dengan Python. Namun, jika permintaan bersamaan mencoba menulis ke database pada saat yang sama, permintaan tersebut akan melambat karena setiap penulisan terjadi secara berurutan.

### Hubungkan ke Database
Hal pertama yang harus dilakukan ketika bekerja dengan database `SQLite` adalah membuat koneksi ke database tersebut. Setiap kueri dan operasi dilakukan menggunakan koneksi, yang ditutup setelah pekerjaan selesai. Dalam aplikasi web, koneksi ini biasanya terkait dengan permintaan. Itu dibuat di beberapa titik saat menangani permintaan, dan ditutup sebelum respons dikirim.

Berikut ini merupakan file python yang digunakan untuk mengakses `database` :
```python
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
```
- `g` adalah objek khusus yang unik untuk setiap permintaan. Ini digunakan untuk menyimpan data yang mungkin diakses oleh beberapa fungsi selama permintaan. Koneksi disimpan dan digunakan kembali alih-alih membuat koneksi baru jika `get_db` dipanggil untuk kedua kalinya dalam permintaan yang sama.
- `current_app` adalah objek khusus lain yang menunjuk ke aplikasi `Flask` yang menangani permintaan. Karena Pengguna menggunakan `application factory`, tidak ada objek aplikasi saat menulis sisa kode. `get_db` akan dipanggil ketika aplikasi telah dibuat dan sedang menangani permintaan, sehingga `current_app` dapat digunakan.
- `sqlite3.connect()` membuat koneksi ke file yang ditunjuk oleh `DATABASE` kunci konfigurasi. File ini belum harus ada, dan tidak akan ada sampai Pengguna menginisialisasi database nanti.
- `sqlite3.Row` memberitahu koneksi untuk mengembalikan baris yang berperilaku seperti `dicts`. Hal ini memungkinkan mengakses kolom dengan nama.
- `close_db` memeriksa apakah koneksi dibuat dengan memeriksa apakah `g/db` sudah disetel. Jika koneksi ada, itu ditutup. Lebih jauh ke bawah Pengguna akan memberi tahu aplikasi tentang fungsi `close_db` di application factory sehingga dipanggil setelah setiap permintaan.

### Membuat Tabel
Dalam `SQLite`, data disimpan dalam tabel dan kolom . Ini perlu dibuat sebelum Pengguna dapat menyimpan dan mengambil data. Flask akan menyimpan pengguna di tabel `user`, dan posting di tabel `post`. Buat file dengan perintah SQL untuk membuat tabel kosong :
```sql
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```
Kemudian tambahkan fungsi Python yang akan menjalankan perintah SQL ini ke file `db.py` :
```python
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```
- `open_resource()` digunakan untuk membuka file relatif terhadap paket flask, karena yang berguna bagi Pengguna tidak perlu tahu di mana lokasi itu saat menerapkan aplikasi nanti. `get_db` mengembalikan koneksi database, yang digunakan untuk menjalankan perintah yang dibaca dari file.
- `click.command()` digunakan untuk mendefinisikan perintah `init-db`, kemudian memanggil fungsi `init_db` dan menunjukkan pesan sukses kepada pengguna.

### Daftar dengan Aplikasi
Fungsi `close_db` dan `init_db_command` harus didaftarkan pada instance aplikasi; jika tidak, mereka tidak akan digunakan oleh aplikasi. Namun, karena Pengguna menggunakan fungsi factory, instance tersebut tidak tersedia saat menulis fungsi. Sebagai gantinya, tulis fungsi yang mengambil aplikasi dan melakukan pendaftaran.

Kemudian tambahkan fungsi Python yang akan menjalankan perintah ini ke file `db.py` :
```python
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```
- `app.teardown_appcontext()` digunakan untuk memberitahu Flask untuk memanggil fungsi itu saat membersihkan setelah mengembalikan respons.
- `app.cli.add_command()` digunakan untuk menambahkan perintah baru yang dapat dipanggil dengan perintah flask.

Kemudian import dan panggil fungsi ini dari factory. Tempatkan kode baru di akhir fungsi factory sebelum mengembalikan aplikasi. Tambahkan fungsi Python yang akan menjalankan perintah ini ke file `__init__.py` :
```python
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```

### Inisialisasi File Database
Sekarang setelah `init-db` terdaftar dengan aplikasi, itu dapat dipanggil menggunakan perintah `flask`, mirip dengan perintah `run`.

Jalankan perintah `init-db` pada Command Prompt:
```
flask init-db
```
Sekarang akan ada file `flask.sqlite` di folder instance di proyek Pengguna.

## Blueprint dan Tampilan
Fungsi tampilan adalah kode yang ditulis untuk menanggapi permintaan ke aplikasi. `Flask` menggunakan pola untuk mencocokkan `URL` permintaan yang masuk dengan tampilan yang seharusnya menanganinya. Tampilan mengembalikan data yang diubah Flask menjadi respons keluar. Flask juga bisa pergi ke arah lain dan menghasilkan URL ke tampilan berdasarkan nama dan argumennya.

### Buat Blueprint
`Blueprint` adalah cara untuk mengatur sekelompok tampilan terkait dan kode lainnya. Daripada mendaftarkan tampilan dan kode lain secara langsung dengan aplikasi, mereka sudah terdaftar pada blueprint. Kemudian blueprint didaftarkan dengan aplikasi ketika tersedia di fungsi `factory`.

Berikut ini adalah file Python yang menggunakan fungsi `Blueprint` :
```python
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
```
File ini menciptakan `Blueprint` bernama `auth`. Seperti objek aplikasi, blueprint perlu tahu di mana itu didefinisikan, sehingga ` __name__` diteruskan sebagai argumen kedua. Perintah `url_prefix` akan ditambahkan ke semua URL yang terkait dengan blueprint.

Kemudian import dan daftarkan blueprint dari pabrik menggunakan `app.register_blueprint()`. Tempatkan kode baru di akhir fungsi `factory` sebelum mengembalikan aplikasi. Tambahkan fungsi Python yang akan menjalankan perintah ini ke file `__init__.py` :
```python
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app
```
Otentikasi `Blueprint` akan memiliki tampilan untuk mendaftarkan pengguna baru dan untuk masuk dan keluar.

### Daftar (Register)
Saat pengguna mengunjungi URL `/auth/register`, tampilan `register` akan mengembalikan HTML dengan formulir untuk mereka isi. Ketika mereka mengirimkan formulir, itu akan memvalidasi input mereka dan menampilkan formulir lagi dengan pesan kesalahan atau membuat pengguna baru dan pergi ke halaman login.

Tambahkan fungsi Python yang akan menjalankan perintah ini ke file `auth.py` :
```python
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```
Inilah yang dilakukan tampilan fungsi `register`:
1. `@bp.route` digunakan untuk mengaitkan URL `/register` dengan fungsi tampilan `register`. Ketika `Flask` menerima permintaan ke `/auth/register`, itu akan memanggil tampilan `register` dan menggunakan nilai kembalian sebagai respons.
2. Jika Pengguna mengirimkan formulir, `request.method` akan `POST`. Dalam hal ini, mulailah memvalidasi input.
3. `request.form` adalah tipe khusus dari pemetaan `dict` dan nilai formulir yang dikirimkan. Pengguna akan memasukkan `username` dan `password`.
4. Validasi `username` dan `password` jangan kosong.
5. Jika validasi berhasil, masukkan data pengguna baru ke dalam `database`.
    - `db.execute` digunakan untuk mengambil query `SQL` dengan placeholder `?` untuk input Pengguna apa pun, dan sejumlah nilai untuk menggantikan placeholder. Pustaka database akan menangani pelepasan nilai sehingga Pengguna tidak rentan terhadap `SQL injection attack`.
    - Untuk keamanan, kata sandi tidak boleh disimpan dalam database secara langsung. Sebagai gantinya, `generate_password_hash()` digunakan untuk hash kata sandi dengan aman, dan hash itu disimpan. Karena query ini mengubah data, `db.commit()` perlu dipanggil setelahnya untuk menyimpan perubahan.
    - Sebuah `sqlite3.IntegrityError` akan terjadi jika nama Pengguna sudah ada, yang harus ditampilkan kepada Pengguna sebagai kesalahan validasi lain.
6. Setelah menyimpan Pengguna, mereka diarahkan ke halaman login. `url_for()` digunakan untuk menghasilkan URL untuk tampilan login berdasarkan namanya. Ini lebih baik daripada menulis URL secara langsung karena memungkinkan Pengguna mengubah URL nanti tanpa mengubah semua kode yang tertaut ke sana. `redirect()` menghasilkan respons pengalihan ke URL yang dihasilkan.
7. Jika validasi gagal, kesalahan akan ditampilkan kepada Pengguna. `flash()` akan menyimpan pesan yang dapat diambil saat merender template.
8. Ketika Pengguna awalnya menavigasi ke `auth/register`, atau ada kesalahan validasi, halaman HTML dengan formulir pendaftaran akan ditampilkan. `render_template()` akan merender template yang berisi HTML.

### Masuk (Login)
Tampilan ini mengikuti pola yang sama seperti tampilan `register` di atas.

Tambahkan fungsi Python yang akan menjalankan perintah ini ke file `auth.py` :
```python
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```
Inilah yang dilakukan tampilan fungsi `login`:
1. Pengguna ditanyai terlebih dahulu dan disimpan dalam variabel untuk digunakan nanti.

    `fetchone()` digunakan untuk mengembalikan satu baris dari query. Jika query tidak memberikan hasil, query akan mengembalikan None. Nanti, `fetchall()` akan digunakan, yang mengembalikan daftar semua hasil.

2. `check_password_hash()` hash kata sandi yang dikirimkan dengan cara yang sama seperti hash yang disimpan dan membandingkannya dengan aman. Jika cocok, kata sandi valid.

3. `session` adalah `dict` yang menyimpan data di seluruh permintaan. Ketika validasi berhasil, pengguna `id` disimpan dalam sesi baru. Data disimpan dalam `cookie` yang dikirim ke browser, dan browser kemudian mengirimkannya kembali dengan permintaan berikutnya. `Flask` menandatangani data dengan aman sehingga tidak dapat dirusak.

Setelah `id` Pengguna disimpan di `session`, itu akan tersedia pada permintaan berikutnya. Di awal setiap permintaan, jika pengguna login, informasi mereka harus dimuat dan tersedia untuk tampilan lain.

Tambahkan fungsi Python yang akan menjalankan perintah ini ke file `auth.py` :
```python
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
```
`bp.before_app_request()` digunakan untuk mendaftarkan fungsi yang berjalan sebelum fungsi tampilan, apa pun URL yang diminta. `load_logged_in_user` akan memeriksa apakah `id` Pengguna disimpan di `session` dan mendapatkan data Pengguna itu dari database, menyimpannya di `g.user`, yang berlangsung selama permintaan. Jika tidak ada `id` Pengguna, atau jika `id` tidak ada, `g.user` akan menjadi `None`.

### Keluar (Logout)
Untuk keluar, Pengguna harus menghapus `id` Pengguna dari file `session`. Kemudian `load_logged_in_user` tidak akan memuat Pengguna pada permintaan berikutnya.
```python
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
### Memerlukan Otentikasi di Tampilan Lain
Membuat, mengedit, dan menghapus postingan blog akan membutuhkan Pengguna untuk masuk. Seorang `dekorator` dapat digunakan untuk memeriksa ini untuk setiap tampilan yang diterapkannya.

Tambahkan fungsi Python yang akan menjalankan perintah ini ke file `auth.py` :
```python
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```
`Dekorator` ini digunakan untuk mengembalikan fungsi tampilan baru yang membungkus tampilan asli yang diterapkannya. Fungsi baru memeriksa apakah Pengguna dimuat dan dialihkan ke halaman login sebaliknya. Jika Pengguna dimuat, maka tampilan asli dipanggil dan berlanjut secara normal. Pengguna akan menggunakan `dekorator` ini saat menulis tampilan blog.

### Endpoints dan URL
Fungsi `url_for()` digunakan untuk menghasilkan URL ke tampilan berdasarkan nama dan argumen. Nama yang terkait dengan tampilan juga disebut `endpoint`, dan secara default sama dengan nama fungsi tampilan.

## Template
`Template` adalah file yang berisi data statis serta `placeholder` untuk data dinamis. Sebuah template diberikan dengan data tertentu untuk menghasilkan dokumen akhir. `Flask` menggunakan library template `Jinja` untuk merender template.

Di `Flask`, Jinja dikonfigurasi `autoescape` untuk data apapun yang dirender dalam template `HTML`. Ini berarti aman untuk merender input pengguna; karakter apa pun yang dimasukkan yang dapat mengacaukan HTML, seperti `<` dan `>` akan diloloskan dengan nilai aman yang terlihat sama di browser tetapi tidak menimbulkan efek yang tidak diinginkan.

`Jinja` terlihat dan berperilaku seperti `Python`. Pembatas khusus digunakan untuk membedakan sintaks Jinja dari data statis dalam template. Apa pun antara `{{` dan `}}` adalah ekspresi yang akan menjadi output ke dokumen akhir. `{%` dan `%}` menunjukkan pernyataan aliran kontrol seperti `if` dan `for`. Tidak seperti Python, blok dilambangkan dengan tag awal dan akhir daripada lekukan karena teks statis dalam blok dapat mengubah lekukan.

### Tata Letak Dasar
Setiap halaman dalam aplikasi akan memiliki tata letak dasar yang sama di sekitar body yang berbeda. Alih-alih menulis seluruh struktur `HTML` di setiap template, setiap template akan `extend` template dasar dan menimpa bagian tertentu.

Berikut ini salah satu contoh file `HTML` yang tata letak dasar, file `base.html` :
```html
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>
```
`g` tersedia secara otomatis dalam template. Berdasarkan jika `g.user` diatur (dari `load_logged_in_user`), maka nama Pengguna dan tautan log out ditampilkan, atau tautan untuk register dan login ditampilkan. `url_for()` juga tersedia secara otomatis, dan digunakan untuk menghasilkan URL ke tampilan alih-alih menuliskannya secara manual.

Setelah judul halaman, dan sebelum content, template mengulang setiap pesan yang dikembalikan oleh `get_flashed_messages()`. Pengguna menggunakan tampilan `flash()` untuk menampilkan pesan kesalahan, dan ini adalah kode yang akan menampilkannya.

Ada tiga blok yang ditentukan di sini yang akan diganti di templat lain:
1. `{% block title %}` akan mengubah judul yang ditampilkan di tab browser dan judul jendela.
2. `{% block header %}` mirip dengan `title` tetapi akan mengubah judul yang ditampilkan pada halaman.
3. `{% block content %}` adalah tempat isi setiap halaman pergi, seperti formulir login atau posting blog.

### Register
Berikut ini salah satu contoh file `HTML` penggunaan template pada halaman Register, file `register.html` :
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```
`{% extends 'base.html' %}` digunakan untuk memberitahu `Jinja` bahwa template ini harus menggantikan blok dari template dasar. Semua content yang dirender harus muncul di dalam tag `{% block %}` yang menggantikan blok dari template dasar.

Pola yang berguna yang digunakan di sini adalah `{% block title %}` untuk menempatkan di dalam `{% block header %}`. Ini akan mengatur blok judul dan kemudian menampilkan nilainya ke dalam blok header, sehingga jendela dan halaman berbagi judul yang sama tanpa menulisnya dua kali.

Tag `input` di sini menggunakan atribut `required`. Ini memberitahu browser untuk tidak mengirimkan formulir sampai kolom tersebut diisi.

### Login
Ini identik dengan template daftar kecuali untuk judul dan tombol kirim.

Berikut ini salah satu contoh file `HTML` penggunaan template pada halaman Login, file `login.html` :
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Log In{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Log In">
  </form>
{% endblock %}
```

## Static File
Tampilan `authentication` dan `template` berfungsi, tetapi saat ini terlihat sangat sederhana. Beberapa `CSS` dapat ditambahkan untuk menambahkan style ke tata letak `HTML` yang dibuat. `Style` tidak akan berubah, karena ini adalah `Static file`, bukan template.

`Flask` secara otomatis menambahkan tampilan static yang mengambil jalur relatif ke direktori `flask/static` dan menyajikannya. Template `base.html` sudah memiliki tautan ke file `style.css`:
```html
{{ url_for('static', filename='style.css') }}
```
Selain CSS, jenis file statis lainnya mungkin file dengan fungsi JavaScript, atau gambar logo. Mereka semua ditempatkan di bawah direktori `flask/static` dan direferensikan dengan `.url_for('static', filename='...')`.

Berikut ini salah satu contoh file `CSS` penggunaan style, file `style.css`:
```css
html { font-family: sans-serif; background: #eee; padding: 1rem; }
body { max-width: 960px; margin: 0 auto; background: white; }
h1 { font-family: serif; color: #377ba8; margin: 1rem 0; }
a { color: #377ba8; }
hr { border: none; border-top: 1px solid lightgray; }
nav { background: lightgray; display: flex; align-items: center; padding: 0 0.5rem; }
nav h1 { flex: auto; margin: 0; }
nav h1 a { text-decoration: none; padding: 0.25rem 0.5rem; }
nav ul  { display: flex; list-style: none; margin: 0; padding: 0; }
nav ul li a, nav ul li span, header .action { display: block; padding: 0.5rem; }
.content { padding: 0 1rem 1rem; }
.content > header { border-bottom: 1px solid lightgray; display: flex; align-items: flex-end; }
.content > header h1 { flex: auto; margin: 1rem 0 0.25rem 0; }
.flash { margin: 1em 0; padding: 1em; background: #cae6f6; border: 1px solid #377ba8; }
.post > header { display: flex; align-items: flex-end; font-size: 0.85em; }
.post > header > div:first-of-type { flex: auto; }
.post > header h1 { font-size: 1.5em; margin-bottom: 0; }
.post .about { color: slategray; font-style: italic; }
.post .body { white-space: pre-line; }
.content:last-child { margin-bottom: 0; }
.content form { margin: 1em 0; display: flex; flex-direction: column; }
.content label { font-weight: bold; margin-bottom: 0.5em; }
.content input, .content textarea { margin-bottom: 1em; }
.content textarea { min-height: 12em; resize: vertical; }
input.danger { color: #cc2f2e; }
input[type=submit] { align-self: start; min-width: 10em; }
```

## Blog Blueprint
`Blog` harus mencantumkan semua postingan, dan mengizinkan Pengguna yang login untuk membuat posting, dan mengizinkan Pengguna untuk mengedit atau menghapusnya.

### Blueprint
Berikut ini salah satu contoh file `Python` penggunaan Blog blueprint, file `blog.py`:
```python
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
```
Import dan daftarkan blueprint dari factory menggunakan `app.register_blueprint()`. Tempatkan kode baru di akhir fungsi factory sebelum mengembalikan aplikasi.
```python
def create_app():
    app = ...
    # existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```
Berbeda dengan auth blueprint, `blog blueprint` tidak memiliki file `url_prefix`. Jadi tampilan `index`akan di `/`, buat tampilan di `/create`, dan seterusnya. `Blog` adalah fitur utama Flask, jadi masuk akal jika indeks blog akan menjadi indeks utama.

Namun, titik akhir untuk tampilan index yang ditentukan di bawah ini adalah `blog.index`. Beberapa tampilan autentikasi mengacu pada titik akhir index biasa. `app.add_url_rule()` mengaitkan nama titik akhir `index` dengan url `/` sehingga `url_for('index')` atau `url_for('blog.index')` keduanya akan berfungsi, menghasilkan URL `/` yang sama dengan cara apa pun.

### Index
`Index` akan menampilkan semua postingan, yang terbaru terlebih dahulu. `JOIN` digunakan agar informasi penulis dari tabel `user` tersedia di hasil.

Tambahkan fungsi Python yang akan menjalankan perintah ini ke file `blog.py` :
```python
@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
```

Dan tambahkan satu file `HTML` penggunaan index, file `index.html`:
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Posts{% endblock %}</h1>
  {% if g.user %}
    <a class="action" href="{{ url_for('blog.create') }}">New</a>
  {% endif %}
{% endblock %}

{% block content %}
  {% for post in posts %}
    <article class="post">
      <header>
        <div>
          <h1>{{ post['title'] }}</h1>
          <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
        </div>
        {% if g.user['id'] == post['author_id'] %}
          <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
        {% endif %}
      </header>
      <p class="body">{{ post['body'] }}</p>
    </article>
    {% if not loop.last %}
      <hr>
    {% endif %}
  {% endfor %}
{% endblock %}
```
Saat Pengguna login, blok `header` menambahkan tautan ke tampilan `create`. Saat Pengguna adalah penulis postingan, mereka akan melihat tautan “Edit” ke tampilan `update` postingan tersebut. `loop.last` adalah variabel khusus yang tersedia di dalam `Jinja` untuk fungsi loop. Ini digunakan untuk menampilkan baris setelah setiap posting kecuali yang terakhir, untuk memisahkannya secara visual.

### Create
Tampilan `create` berfungsi sama dengan tampilan auth `register`. Baik formulir ditampilkan, atau data yang diposting divalidasi dan postingan ditambahkan ke database atau kesalahan ditampilkan.

`login_required` dekorator yang Pengguna tulis sebelumnya digunakan pada tampilan `blog`. Seorang Pengguna harus login untuk mengunjungi tampilan ini, jika tidak mereka akan diarahkan ke halaman login.

Tambahkan fungsi Python yang akan menjalankan perintah ini ke file `blog.py` :
```python
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
```

Dan tambahkan satu file `HTML` penggunaan create, file `create.html`:
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}New Post{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title" value="{{ request.form['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
{% endblock %}
```

### Update
Tampilan `update` maupun tampilan `delete` perlu diambil post oleh `id` dan memeriksa apakah pembuatnya cocok dengan Pengguna yang login. Untuk menghindari duplikasi kode, Pengguna dapat menulis fungsi untuk mendapatkan `post` dan memanggilnya dari setiap tampilan.

Tambahkan fungsi Python yang akan menjalankan perintah ini ke file `blog.py` :
```python
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
```
`abort()` akan memunculkan pengecualian khusus yang mengembalikan kode status HTTP. Dibutuhkan pesan opsional untuk ditampilkan dengan kesalahan, jika tidak, pesan default akan digunakan. `404` berarti `Not Found` atau tidak ditemukan, dan `403` berarti `Forbidden` atau terlarang. ( `401` berarti `Unauthorized` atau tidak sah, tetapi Pengguna dapat mengarahkan ulang ke halaman login alih-alih mengembalikan status itu.)

Argumen `check_author` didefinisikan sehingga fungsi dapat digunakan untuk mendapatkan sebuah `post` tanpa memeriksa pembuatnya. Ini akan berguna jika Pengguna menulis tampilan untuk menampilkan kiriman individual pada halaman, di mana Pengguna tidak masalah karena mereka tidak mengubah kiriman.

Tambahkan fungsi Python yang akan menjalankan perintah ini ke file `blog.py` :
```python
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```
Fungsi `update` mengambil argumen, `id`. Itu sesuai dengan `<int:id>` di rute. URL asli akan terlihat seperti `/1/update`. Flask akan menangkap `1`, memastikan itu adalah `int`, dan meneruskannya sebagai argumen `id`. Jika Pengguna tidak menentukan `int`, dan sebaliknya melakukan `<id>`, itu akan menjadi `string`. Untuk menghasilkan URL ke halaman pembaruan, `url_for()` perlu diteruskan agar `id` tahu apa yang harus diisi: `url_for('blog.update', id=post['id'])`. Ini juga ada di file `index.html` di atas.

Tampilan `create` dan tampilan `update` terlihat sangat mirip. Perbedaan utama adalah bahwa tampilan update menggunakan objek post dan query `UPDATE` alih-alih `INSERT` file. Dengan beberapa pemfaktoran ulang yang cerdas, Pengguna dapat menggunakan satu tampilan dan template untuk kedua tindakan.

Dan tambahkan satu file `HTML` penggunaan update, file `update.html`:
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Edit "{{ post['title'] }}"{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title"
      value="{{ request.form['title'] or post['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
  <hr>
  <form action="{{ url_for('blog.delete', id=post['id']) }}" method="post">
    <input class="danger" type="submit" value="Delete" onclick="return confirm('Are you sure?');">
  </form>
{% endblock %}
```
Template ini memiliki dua bentuk. Yang pertama memposting data yang diedit ke halaman saat ini (`/<id>/update`). Formulir lainnya hanya berisi tombol dan menentukan atribut `action` yang memposting ke tampilan hapus. Tombol menggunakan beberapa JavaScript untuk menampilkan dialog konfirmasi sebelum mengirimkan.

Pola `{{ request.form['title'] or post['title'] }}` digunakan untuk memilih data apa yang muncul dalam form. Ketika formulir belum dikirimkan, data asli muncul, tetapi jika data formulir yang tidak valid telah diposting, Pengguna ingin menampilkannya sehingga pengguna dapat memperbaiki kesalahan, jadi `postrequest.form` digunakan sebagai gantinya. `request` adalah variabel lain yang secara otomatis tersedia di template.

### Delete
Tampilan `delete` tidak memiliki template sendiri, tombol delete adalah bagian dari `update.html` dan memposting ke URL `/<id>/delete`. Karena tidak ada template, maka itu hanya akan menangani method `POST` dan kemudian mengarahkan ulang ke tampilan `index`.

Tambahkan fungsi Python yang akan menjalankan perintah ini ke file `blog.py` :
```python
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
```

## Jadikan Proyek Dapat Diinstal
Membuat sebuah proyek yang dapat diinstal berarti Pengguna dapat membuat file `distribution` dan menginstalnya di environment lain, sama seperti Pengguna ketika menginstal `Flask` di environment proyek yang di buat. Ini membuat penerapan proyek sama dengan menginstal library lain, jadi Pengguna menggunakan semua alat `Python` standar untuk mengelola semuanya.

Menginstal juga dilengkapi dengan manfaat lain yang mungkin tidak terlihat, yaitu:
- Saat ini, `Python` dan `Flask` memahami cara menggunakan package flask hanya karena Pengguna dapat menjalankan dari direktori proyek. Menginstal berarti Pengguna dapat mengimpornya dari mana pun Pengguna menjalankannya.
- Pengguna dapat mengelola dependensi proyek seperti halnya paket lain, jadi `pip install yourproject.whl` merupakan perintah untuk menginstal dependensi tersebut.
- Alat pengujian dapat mengisolasi pengujian environment Pengguna dari  pengembangan environment.

### Mendeskripsikan Proyek
Tambahkan satu file `Python` untuk mendeskripsikan proyek yang dibuat, file `setup.py`:
```python
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
```
`packages` memberi tahu Python direktori paket apa (dan file Python yang dikandungnya) untuk disertakan. `find_packages()` menemukan direktori ini secara otomatis sehingga Pengguna tidak perlu mengetiknya. Untuk menyertakan file lain, seperti direktori statis dan template, `include_package_data` sudah diatur. Python membutuhkan file lain bernama `MANIFEST.in` untuk memberi tahu data lain.
```
include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```
Ini memberitahu Python untuk menyalin semua yang ada di `static` dan direktori `template`, dan file `schema.sql`, tetapi untuk mengecualikan semua file bytecode.

### Install Proyek
Gunakan perintah `pip` untuk menginstal proyek yang ada di virtual environment.
```
pip install -e .
```
Ini memberitahu `pip` untuk menemukan `setup.py` di direktori saat ini dan menginstalnya dalam mode yang dapat diedit atau mode `development`. Mode yang dapat diedit berarti, ketika Pengguna membuat perubahan pada kode lokal, makan Pengguna hanya perlu menginstal ulang jika mengubah metadata tentang proyek, seperti dependensinya.

## Test Coverage
Secara khusus, itu tidak menguji bagaimana pengguna berinteraksi dengan aplikasi di browser. Meskipun demikian, cakupan pengujian merupakan alat penting untuk digunakan selama pengembangan.

Pengguna akan menggunakan `pytest` dan `coverage` untuk menguji dan mengukur kode. Instal keduanya menggunakan perintah berikut :
```
$ pip install pytest coverage
```

### Pengaturan dan Perlengkapan
Setiap pengujian akan membuat file database sementara baru dan mengisi beberapa data yang akan digunakan dalam pengujian. Tulis file SQL untuk memasukkan data itu.

Tambahkan satu file `SQL` dengan nama file `data.sql`:
```sql
INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');
```
`Fixture app` akan memanggil factory dan lolos `test_config` untuk mengonfigurasi aplikasi dan database untuk pengujian alih-alih menggunakan konfigurasi pengembangan lokal Pengguna.

Tambahkan satu file `Python` dengan nama file `conftest.py`:
```python
import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```
`tempfile.mkstemp()` digunakan untuk membuat dan membuka file sementara, mengembalikan deskriptor file dan jalur ke sana. Jalur `DATABASE` diganti sehingga mengarah ke jalur sementara ini alih-alih folder `instance`. Setelah mengatur jalur, tabel database dibuat dan data uji dimasukkan. Setelah tes selesai, file sementara ditutup dan dihapus.

`TESTING` memberitahu Flask bahwa aplikasi dalam mode uji. Flask mengubah beberapa perilaku internal sehingga lebih mudah untuk diuji, dan ekstensi lain juga dapat menggunakan tanda untuk mempermudah pengujian.

Fixture client memanggil `app.test_client()` dengan objek aplikasi yang dibuat oleh app fixture. Pengujian akan menggunakan klien untuk membuat permintaan ke aplikasi tanpa menjalankan server.

`runner` fixture mirip dengan client. `app.test_cli_runner()` digunakan untuk membuat runner yang dapat memanggil perintah Klik yang terdaftar dengan aplikasi. `Pytest` menggunakan fixtures dengan mencocokkan nama fungsinya dengan nama argumen dalam fungsi pengujian.

### Factory
Tidak banyak yang bisa diuji tentang `factory` itu sendiri. Sebagian besar kode akan dieksekusi untuk setiap tes, jadi jika ada yang gagal, tes lain akan memperhatikan.

Satu-satunya perilaku yang dapat berubah adalah melewati konfigurasi pengujian. Jika konfigurasi tidak diteruskan, harus ada beberapa konfigurasi default, jika tidak, konfigurasi harus diganti.

Tambahkan satu file `Python` dengan nama file `test_factory.py`:
```python
from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```

### Database
Dalam konteks aplikasi, `get_db` harus mengembalikan koneksi yang sama setiap kali dipanggil. Setelah konteksnya, koneksi harus ditutup.
```python
import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
```

Perintah `init-db` harus memanggil fungsi `init_db` dan mengeluarkan pesan.
```python
def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
```
Tes ini menggunakan Pytest `monkeypatch` fixture untuk mengganti fungsi `init_db` dengan yang mencatat bahwa itu telah dipanggil. `runner` fixture yang Pengguna tulis di atas digunakan untuk memanggil perintah `init-db` dengan nama.

### Authentication
Untuk sebagian besar tampilan, Pengguna harus masuk. Cara termudah untuk melakukan ini dalam pengujian adalah membuat `POST` request ke tampilan `login` dengan klien. Daripada menuliskannya setiap saat, Pengguna dapat menulis kelas dengan method untuk melakukan itu, dan menggunakan fixture untuk memberikannya kepada klien untuk setiap pengujian.

```python
class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
```

Dengan `auth` fixture, Pengguna dapat memanggil `auth.login()` untuk tes masuk sebagai `test` Pengguna, yang dimasukkan sebagai bagian dari data uji di `app` fixture.

Tampilan `register` harus berhasil dirender pada `GET`. Method `POST` dengan data formulir yang valid, itu harus diarahkan ke URL login dan data Pengguna harus ada di database. Data yang tidak valid harus menampilkan pesan kesalahan.

```python
import pytest
from flask import g, session
from flaskr.db import get_db


def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'a'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data
```
`client.get()` membuat `GET` fixture dan mengembalikan objek `Response` yang dikembalikan oleh Flask. Demikian pula, `client.post()` membuat `POST` fixture, mengubah `data` dict menjadi data formulir.

`pytest.mark.parametrize` memberitahu Pytest untuk menjalankan fungsi pengujian yang sama dengan argumen yang berbeda. Pengguna menggunakannya di sini untuk menguji berbagai masukan yang tidak valid dan pesan kesalahan tanpa menulis kode yang sama tiga kali.

```python
def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data
```
Pengujian `logout` adalah kebalikan dari `login`. `session` tidak boleh berisi `user_id` setelah `logout`.
```python
def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session
```

### Blog
Semua tampilan `blog` menggunakan `auth` fixture. Panggilan `auth.login()`dan permintaan berikutnya dari klien akan masuk sebagai `test` Pengguna.

```python
import pytest
from flaskr.db import get_db


def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data
```
Pengguna harus login untuk mengakses `create`, `update`, dan tampilan `delete`. Pengguna yang login harus menjadi penulis kiriman untuk mengakses `update` dan `delete`, jika tidak, status `403 Forbidden` akan dikembalikan. Jika post dengan yang diberikan id tidak ada, `update` dan `delete` harus kembali `404 Not Found`.

```python
@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/delete',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login"


def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403
    # current user doesn't see edit link
    assert b'href="/1/update"' not in client.get('/').data


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/delete',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404
```
Tampilan `create` dan `update` harus merender dan mengembalikan status `200 OK` untuk permintaan `GET`. Ketika data yang valid dikirim dalam permintaan `POST`, `create` harus memasukkan data posting baru ke dalam database, dan `update` harus mengubah data yang ada. Kedua halaman harus menampilkan pesan kesalahan pada data yang tidak valid.

```python
def test_create(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'body': ''})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2


def test_update(client, auth, app):
    auth.login()
    assert client.get('/1/update').status_code == 200
    client.post('/1/update', data={'title': 'updated', 'body': ''})

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post['title'] == 'updated'


@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
))
def test_create_update_validate(client, auth, path):
    auth.login()
    response = client.post(path, data={'title': '', 'body': ''})
    assert b'Title is required.' in response.data
```

Tampilan `delete` harus dialihkan ke URL indeks dan post seharusnya tidak ada lagi di database.

```python
def test_delete(client, auth, app):
    auth.login()
    response = client.post('/1/delete')
    assert response.headers["Location"] == "/"

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None
```

### Tes Menjalankan Aplikasi
Untuk menjalankan tes, gunakan perintah `pytest`. Ini akan menemukan dan menjalankan semua fungsi pengujian yang telah ditulis.
```
$ pytest

========================= test session starts ==========================
```

Untuk mengukur cakupan kode pengujian, gunakan perintah `coverage` untuk menjalankan pytest alih-alih menjalankannya secara langsung.
```
$ coverage run -m pytest
```

Pengguna dapat melihat laporan cakupan sederhana di terminal:
```
$ coverage report

Name                 Stmts   Miss Branch BrPart  Cover
------------------------------------------------------
flasr/__init__.py      21      0      2      0   100%
flasr/auth.py          54      0     22      0   100%
flasr/blog.py          54      0     16      0   100%
flasr/db.py            24      0      4      0   100%
------------------------------------------------------
TOTAL                 153      0     44      0   100%
```

Laporan HTML memungkinkan Pengguna dapat melihat baris mana yang tercakup dalam setiap file menggunakan perintah :
```
$ coverage html
```

## Terapkan ke Produksi
Bagian ini mengasumsikan Pengguna memiliki server yang ingin digunakan untuk menyebarkan aplikasi yang dibuat. Ini memberikan gambaran umum tentang cara membuat file distribusi dan menginstalnya, tetapi tidak akan membahas secara spesifik tentang server atau perangkat lunak apa yang digunakan. Pengguna juga dapat menyiapkan environment baru di komputer development untuk mencoba petunjuk di bawah ini, tetapi mungkin sebaiknya tidak menggunakannya untuk menghosting aplikasi publik yang sebenarnya.

### Build dan Install
Saat Pengguna ingin menyebarkan aplikasi ini di tempat lain, Pengguna harus membangun file distribusi. Standar saat ini untuk distribusi Python adalah format `wheel`, dengan ekstensi `.whl`. Pastikan library wheel diinstal terlebih dahulu:
```
$ pip install wheel
```

Kemudian menjalankan file `setup.py` dengan Python memberi perintah pada command prompt untuk mengeluarkan perintah terkait build. Perintah `bdist_wheel` akan membangun file wheel distribusi.
```
$ python setup.py bdist_wheel
```
Pengguna dapat menemukan file di `dist/flaskr-1.0.0-py3-none-any.whl`. Nama file dalam format {project name}-{version}-{python tag} -{abi tag}-{platform tag}.

Untuk menginstall ke komputer lain, siapkan `virtualenv` baru, lalu instal file dengan ekstensi `pip`. Contohnya seperti berikut ini :
```
$ pip install flaskr-1.0.0-py3-none-any.whl
```
`Pip` akan menginstal proyek beserta dependensinya.

Pengguna perlu menjalankannya `init-db` lagi untuk membuat database di folder `instance`.
```
> set FLASK_APP=flaskr
> flask init-db
```
Ketika `Flask` mendeteksi bahwa itu telah diinstal (tidak dalam mode yang dapat diedit), ia menggunakan direktori yang berbeda untuk folder instance. Pengguna dapat menemukannya di `venv/var/flaskr-instance` sebagai gantinya.

### Konfigurasikan Secret Key
Pengguna berikan nilai default untuk `SECRET_KEY`. Ini harus diubah menjadi beberapa byte acak dalam produksi. Jika tidak, penyerang dapat menggunakan kunci publik `dev` untuk memodifikasi sesi cookie, atau apa pun yang menggunakan kunci rahasia.

Pengguna dapat menggunakan perintah berikut untuk menampilkan kunci rahasia acak:
```
$ python -c 'import secrets; print(secrets.token_hex())'

'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```

Kemudian buat file `config.py` di folder `instance`, yang akan dibaca oleh factory jika ada. Salin nilai yang dihasilkan ke dalamnya.
```
SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```
Pengguna juga dapat mengatur konfigurasi lain yang diperlukan di sini, meskipun `SECRET_KEY` ini adalah satu-satunya yang diperlukan untuk `Flask`.

### Jalankan dengan Server Produksi
Saat menjalankan secara publik alih-alih dalam pengembangan, Pengguna tidak boleh menggunakan server pengembangan bawaan (`flask run`). Server pengembangan disediakan oleh `Werkzeug` untuk kenyamanan, tetapi tidak dirancang untuk menjadi sangat efisien, stabil, atau aman.

Sebagai gantinya, gunakan server produksi `WSGI`. Misalnya, untuk menggunakan `Waitress` , instal terlebih dahulu di virtual environment:
```
$ pip install waitress
```

Pengguna juga perlu memberi tahu `Waitress` tentang aplikasi yang dibuat, tetapi aplikasi itu tidak menggunakan `FLASK_APP` melainkan suka menggunakan `flask run`. Pengguna hanya perlu memberitahunya untuk mengimpor dan memanggil application factory untuk mendapatkan objek aplikasi.
```
$ waitress-serve --call 'flaskr:create_app'

Serving on http://0.0.0.0:8080
```