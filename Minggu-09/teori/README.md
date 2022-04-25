# BAB 12 : Virtual Environments and Packages

## 1. Introduction
Aplikasi Python sering menggunakan `packages` dan `modules` yang tidak datang sebagai bagian dari library standar. Aplikasi ini terkadang memerlukan versi library tertentu, karena aplikasi ini mungkin mengharuskan bug tertentu telah diperbaiki atau aplikasi mungkin ditulis menggunakan versi library's interface yang sudah usang.

Ini berarti tidak mungkin satu instalasi Python memenuhi persyaratan setiap aplikasi. Jika aplikasi `A` membutuhkan versi `1.0` dari module tertentu tetapi aplikasi `B` membutuhkan versi `2.0`, maka persyaratan tersebut bertentangan dan menginstal versi `1.0` atau `2.0` akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah dengan membuat `virtual environment`, pohon direktori mandiri yang berisi instalasi Python untuk versi Python tertentu, ditambah sejumlah paket tambahan.

Aplikasi yang berbeda kemudian dapat menggunakan `virtual environment` yang berbeda. Untuk mengatasi contoh sebelumnya dari persyaratan yang saling bertentangan, aplikasi `A` dapat memiliki `virtual environment` sendiri dengan versi `1.0` terinstal, sementara aplikasi `B` memiliki `virtual environment` lain dengan versi `2.0`. Jika aplikasi `B` memerlukan library yang ditingkatkan ke versi `3.0`, ini tidak akan memengaruhi lingkungan aplikasi `A`.

## 2. Creating Virtual Environments
Module yang digunakan untuk membuat dan mengelola `virtual environment` disebut venv. `venv` biasanya akan menginstal versi terbaru Python yang Pengguna miliki. Jika Pengguna memiliki beberapa versi Python di sistem, Pengguna dapat memilih versi Python tertentu dengan menjalankan `python3` atau versi mana pun yang Anda inginkan.

Untuk membuat `virtual environment`, Pengguna menentukan direktori tempat ingin meletakkannya, dan jalankan `venv module` sebagai skrip dengan jalur direktori:

```python
python3 -m venv tutorial-env
```

Ini akan membuat direktori `tutorial-env` jika tidak ada, dan juga membuat direktori di dalamnya yang berisi salinan interpreter Python dan berbagai file pendukung.

Lokasi direktori umum untuk `virtual environment` adalah `.venv`. Nama ini membuat direktori biasanya tersembunyi di shell Pengguna dan dengan demikian menyingkir sambil memberinya nama yang menjelaskan mengapa direktori itu ada. Ini juga mencegah bentrokan dengan file `.env` definisi variabel lingkungan yang didukung oleh beberapa tool.

Setelah Pengguna membuat `virtual environment`, Pengguna dapat mengaktifkannya menggunakan perintah/syntax.

Di `Windows`, jalankan:
```python
tutorial-env\Scripts\activate.bat
```

Di `Unix` atau `MacOS`, jalankan:
```python
source tutorial-env/bin/activate
```
`Catatan : (Skrip ini ditulis untuk bash shell. Jika Pengguna menggunakan csh atau fish shells, ada alternatif activate.csh dan activate.fish skrip yang harus Pengguna gunakan.)`

Mengaktifkan `virtual environment` akan mengubah prompt shell Pengguna untuk menunjukkan `virtual environment` apa yang digunakan, dan memodifikasi lingkungan sehingga menjalankan python akan memberi Pengguna versi tertentu dan instalasi Python. Sebagai contoh:

```python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

## 3. Managing Packages with pip
Pengguna dapat menginstal, memutakhirkan, dan menghapus paket menggunakan program bernama `pip`. Secara default pip akan menginstal paket dari Python Package Index, `<https://pypi.org>`. Pengguna dapat menelusuri Indeks Paket Python dengan membukanya di browser web. pip memiliki sejumlah sub-perintah: *“install”*, *“uninstall”*, *“freeze”*, dll.

Pengguna dapat menginstal versi terbaru dari sebuah paket dengan menentukan nama packages:
```python
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

Pengguna juga dapat menginstal versi paket tertentu dengan memberikan nama paket diikuti oleh `==` dan nomor versi:
```python
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```

Jika Pengguna menjalankan kembali perintah ini, pip akan melihat bahwa versi yang diminta sudah diinstal dan tidak melakukan apa-apa. Pengguna dapat memberikan nomor versi yang berbeda untuk mendapatkan versi tersebut, atau Pengguna dapat menjalankan `pip install --upgrade` untuk memutakhirkan paket ke versi terbaru:
```python
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

`pip uninstall` diikuti oleh satu atau lebih nama paket akan menghapus paket dari `virtual environment`.

`pip show` akan menampilkan informasi tentang paket tertentu:
```python
(tutorial-env) $ pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```

`pip list` akan menampilkan semua paket yang diinstal di `virtual environment`:
```python
(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

`pip freeze` akan menghasilkan daftar paket yang diinstal serupa, tetapi output menggunakan format `pip install` yang diharapkan. Konvensi umum adalah meletakkan daftar ini dalam file `requirements.txt`:
```python
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

Kemudian file `requirements.txt` dapat dikomit ke kontrol versi dan dikirimkan sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan `install -r`:
```python
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```


# Conda
`Conda` adalah sistem manajemen paket sumber terbuka dan sistem manajemen lingkungan yang berjalan di `Windows`, `macOS`, dan `Linux`. Conda dengan cepat menginstal, menjalankan, dan memperbarui paket dan dependensinya. Conda dengan mudah membuat, menyimpan, memuat, dan beralih antar lingkungan di komputer lokal. Itu dibuat untuk program Python tetapi dapat mengemas dan mendistribusikan perangkat lunak untuk bahasa apa pun.

Conda sebagai manajer paket membantu Pengguna menemukan dan menginstal `packages`. Jika Pengguna memerlukan paket yang memerlukan versi Python yang berbeda, Pengguna tidak perlu beralih ke pengelola lingkungan lain karena conda juga merupakan `environment manager`. Hanya dengan beberapa perintah, Pengguna dapat mengatur lingkungan yang benar-benar terpisah untuk menjalankan versi Python yang berbeda itu, sambil terus menjalankan versi Python yang biasa di lingkungan normal Pengguna.

Dalam konfigurasi default, conda dapat menginstal dan mengelola lebih dari `7.500` paket di `repo.anaconda.com` yang dibuat, ditinjau, dan dikelola oleh `Anaconda®`.

Conda dapat dikombinasikan dengan sistem integrasi berkelanjutan seperti `Travis CI` dan `AppVeyor` untuk menyediakan pengujian kode yang sering dan otomatis.

`conda packages` dan  `environment manager` disertakan dalam semua versi `Anaconda®`, `Miniconda`, dan `Anaconda Repository`. Conda juga disertakan dalam `Anaconda Enterprise`, yang menyediakan paket perusahaan di tempat dan manajemen lingkungan untuk `Python`, `R`, `Node.js`, `Java`, dan tumpukan aplikasi lainnya. Conda juga tersedia di `conda-forge` , saluran komunitas. Pengguna mungkin juga mendapatkan conda di `PyPI`, tetapi pendekatan itu mungkin tidak mutakhir.

## Memulai Conda
- `Windows`, Dari menu Start, cari dan buka `"Anaconda Prompt."` di `Windows`.
- `MacOS`, Buka Launchpad, lalu klik ikon terminal. Di `macOS`, semua perintah di bawah ini diketik ke jendela terminal.
- `Linux`, Buka jendela terminal. Di `Linux`, semua perintah di bawah ini diketik ke jendela terminal.

## Mengelola Conda
Verifikasi bahwa conda diinstal dan berjalan di sistem Pengguna dengan mengetik:
```
# Perintah :
conda --version
```
Conda akan menampilkan nomor versi yang telah Pengguna instal. Pengguna tidak perlu menavigasi ke direktori Anaconda.

Contoh: `conda 4.7.12`

`Catatan : `

`Jika Pengguna mendapatkan pesan kesalahan, pastikan Pengguna menutup dan membuka kembali jendela terminal setelah menginstal, atau lakukan sekarang. Kemudian verifikasi bahwa Pengguna masuk ke akun pengguna yang sama yang Pengguna gunakan untuk menginstal Anaconda atau Miniconda.`

Perbarui conda ke versi saat ini. Ketik perintah berikut ini:
```
# Perintah :
conda update conda
```

Conda membandingkan versi dan kemudian menampilkan apa yang tersedia untuk diinstal.

Jika versi conda yang lebih baru tersedia, ketik `y` untuk memperbarui:
```
# Perintah :
Proceed ([y]/n)? y
```

## Mengelola Lingkungan
`Conda` memungkinkan Pengguna membuat lingkungan terpisah yang berisi file, paket, dan dependensinya yang tidak akan berinteraksi dengan lingkungan lain.

Saat Pengguna mulai menggunakan conda, Pengguna sudah memiliki lingkungan default bernama `base`. Pengguna tidak ingin memasukkan program ke dalam base environment. Buat lingkungan terpisah untuk menjaga program tetap terisolasi satu sama lain.
1. Buat lingkungan baru dan instal paket di dalamnya.

    Kami akan memberi nama environment `snowflakes` dan menginstal paket `BioPython`. Di Anaconda Prompt atau di jendela terminal, ketikkan yang berikut ini:
    ```
    conda create --name snowflakes biopython
    ```
    Conda memeriksa untuk melihat paket tambahan ("dependensi") apa yang dibutuhkan `BioPython`, dan menanyakan apakah Pengguna ingin melanjutkan:
    ```
    Proceed ([y]/n)? y
    ```
    Ketik **"y"** dan tekan Enter untuk melanjutkan.

2. Untuk menggunakan, atau **"activate"** environment baru, ketik berikut ini:
    - **Windows**: `conda activate snowflakes`
    - **macOS** dan **Linux**: `conda activate snowflakes`

    Untuk versi conda sebelum `4.6`, ketik:
    - **Windows**: `activate snowflakes`
    - **macOS** dan **Linux**: `source activate snowflakes`

    Sekarang Pengguna berada di `snowflakes` environment, semua perintah conda yang diketik akan masuk ke lingkungan itu sampai Pengguna menonaktifkannya.

3. Untuk melihat daftar semua environment Pengguna, ketik:
    
    ```
    conda info --envs
    ```
    
    Daftar environments muncul, mirip dengan berikut ini:
    ```
    conda environments:

        base           /home/username/Anaconda3
        snowflakes   * /home/username/Anaconda3/envs/snowflakes
    ```

4. Ubah environment Pengguna saat ini kembali ke default (basis): `conda activate`

## Mengelola Python
Saat Pengguna membuat environments baru, conda menginstal versi `Python` yang sama dengan yang digunakan saat mengunduh dan menginstal `Anaconda`. Jika Pengguna ingin menggunakan versi Python yang berbeda, misalnya Python `3.5`, cukup buat environments baru dan tentukan versi Python yang diinginkan.
1. Buat environments baru bernama **"snakes"** yang berisi Python `3.9`:
    ```
    conda create --name snakes python=3.9
    ```

    Ketika conda bertanya apakah Anda ingin melanjutkan, ketik **"y"** dan tekan Enter.

2. Aktifkan environments baru:
    - **Windows**:`conda activate snakes`
    - **macOS** dan **Linux**:`conda activate snakes`

    Untuk versi conda sebelum `4.6`, ketik:
    - **Windows**: `activate snakes`
    - **macOS** dan **Linux**: `source activate snakes`

3. Verifikasi bahwa environments **snakes** telah ditambahkan dan aktif:
    ```
    conda info --envs
    ```

    Conda menampilkan daftar semua environments dengan tanda bintang `(*)` setelah nama environments aktif:
    ```
    # conda environments:
    #
    base                     /home/username/anaconda3
    snakes                *  /home/username/anaconda3/envs/snakes
    snowflakes               /home/username/anaconda3/envs/snowflakes
    ```

    environments aktif juga ditampilkan di depan prompt Pengguna di (tanda kurung) atau [kurung] seperti ini:
    ```
    (snakes) $
    ```

4. Verifikasi versi Python mana yang ada di environments Pengguna saat ini:
    ```
    python --version
    ```
5. Nonaktifkan environments **snakes** dan kembali ke environments dasar: `conda activate`

## Mengelola Paket
Di bagian ini, Pengguna memeriksa paket mana yang telah diinstal, memeriksa mana yang tersedia dan mencari paket tertentu dan menginstalnya.

1. Untuk menemukan paket yang telah Pengguna instal, aktifkan terlebih dahulu environments yang ingin dicari. Lihat di atas untuk perintah untuk mengaktifkan environments **snakes**.

2. Periksa untuk melihat apakah paket yang belum Pengguna instal bernama `"beautifulsoup4"` tersedia dari repositori Anaconda (harus terhubung ke Internet):
    ```
    conda search beautifulsoup4
    ```
    Conda menampilkan daftar semua paket dengan nama itu di repositori Anaconda, jadi kami tahu itu tersedia.

3. Instal paket ini ke environments saat ini:
    ```
    conda install beautifulsoup4
    ```

4. Periksa untuk melihat apakah program yang baru diinstal ada di environments ini:
    ```
    conda list
    ```