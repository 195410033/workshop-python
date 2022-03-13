# BAB 7 : I/O

`Input` merupakan sebuah data, informasi, atau nilai apa pun yang dikirimkan oleh user kepada komputer untuk diproses lebih lanjut. User melakukan proses input melalui media atau perangkat masukan seperti kibor, mouse, kamera, mikrofon dan lain sebagainya.

`Output` merupakan setiap nilai atau data atau informasi yang dikirimkan oleh mesin / komputer kepada user (manusia) setelah tahap pemrosesan tertentu. Secara umum output bisa berupa teks, gambar, suara, atau bahkan berupa informasi yang dicetak di atas kertas, dan sebagainya.

## 1. Fancier Output Formatting
Ketika User tidak membutuhkan output yang mewah tetapi hanya ingin tampilan cepat dari beberapa variabel untuk keperluan debugging, User dapat mengonversi nilai apa pun menjadi string menggunakan fungsi `repr()` atau `str()`.
- Fungsi `str()` digunakan untuk mengembalikan representasi nilai yang cukup yang dapat dibaca oleh manusia
- Fungsi `repr()` digunakan untuk menghasilkan representasi yang dapat dibaca oleh interpreter (atau akan memaksa suatu SyntaxError jika tidak ada sintaks yang setara). 

Untuk objek yang tidak memiliki representasi khusus untuk konsumsi manusia, fungsi `str()` akan mengembalikan nilai yang sama dengan fungis `repr()`. 
```python
# Contoh fungsi str() dan repr()
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"

>>> str(1/7)
'0.14285714285714285'

>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...

>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'

>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

Ada beberapa cara untuk memformat output :
- `Formatted string literals` digunakan untuk memulai string dengan `f` atau `F` sebelum tanda kutip pembuka atau tanda kutip tiga. Dalam string ini, User dapat menulis ekspresi Python menggunakan karakter `{` dan `}` yang dapat merujuk ke variabel atau nilai literial.
```python
# Contoh Formatted string literals
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
# Output
'Results of the 2016 Referendum'
```

- `str.format()` merupakan metode string yang membutuhkan lebih banyak upaya secara manual. User masih menggunakan karakter `{` dan `}` untuk menandai di mana variabel yang akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi User juga harus memberikan informasi yang akan diformat.
```python
# Contoh str.format()
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
# Output
' 42572654 YES votes  49.67%'
```

- `Manual string formatting` merupakan metode string yang dilakukan secara manual. Metode `str.rjust()` merupakan objek string yang membenarkan string di bidang dengan lebar tertentu dengan mengisinya dengan spasi di sebelah kiri. Ada metode serupa `str.ljust()` dan `str.center()`, metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Jika string input terlalu panjang, mereka tidak memotongnya, tetapi mengembalikannya namun tidak berubah.
```python
# Contoh manual string formatting
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
# Output
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

- `Old string formatting` merupakan operator %(module) yang dapat digunakan untuk pemformatan string. Mengingat `'string' % values`, contoh dari `%` diganti dengan nol atau nilai lebih. Operasi ini biasa disebut dengan interpolasi string. Sebagai contoh:
```python
# Contoh old string formatting
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
# Output
The value of pi is approximately 3.142.
```

## 2. Reading and Writing Files
Fungsi `open()` digunakan untuk mengembalikan objek file, dan format yang biasanya menggunakan dua argument yaitu : `open(filename,mode)`
- Argumen pertama adalah string yang berisi nama file yang digunakan `filename`.
- Argumen kedua adalah string yang berisi beberapa karakter yang menjelaskan cara file akan digunakan. Mode `r` bisa ketika file hanya akan dibaca, `w` hanya untuk menulis (file yang ada dengan nama yang sama akan dihapus), `a` membuka file untuk ditambahkan, dan `r+` membuka file untuk membaca dan menulis.
```python
# Contoh mode Writing Files
>>> f = open('workfile', 'w')
```
Biasanya, file dibuka dalam mode teks, artinya User membaca dan menulis string yang dikodekan dalam pengkodean tertentu. Jika penyandian tidak ditentukan, defaultnya adalah bergantung pada platform. Mode `b` ditambahkan ke mode membuka file dalam mode biner : sekarang data dibaca dan ditulis dalam bentuk objek byte. Mode ini harus digunakan untuk semua file yang tidak berisi teks.

### a. Methods or File Objects
- Fungsi `f.read(size)` digunakan untuk membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). `size` adalah argumen numerik opsional. Ketika ukuran dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan.  Jika file akhir telah tercapai, fungsi `f.read()` akan mengembalikan string kosong (' ').
```python
# Contoh f.read(size)
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

- Fungsi `f.readline()` digunakan untuk membaca satu baris dari file; karakter baris baru (\n) ditinggalkan di akhir string, dan hanya dihilangkan pada baris terakhir file jika file tidak diakhiri dengan baris baru. Ini membuat nilai pengembalian tidak ambigu; jika `f.readline()` mengembalikan string kosong, akhir file telah tercapai, sedangkan baris kosong diwakili oleh '\n', string yang hanya berisi satu baris baru.
```python
# Contoh f.readline()
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

- Fungsi `f.write(string)` digunakan untuk menulis isi string ke file, dan mengembalikan jumlah karakter yang ditulis.
```python
# Contoh f.write(string)
>>> f.write('This is a test\n')
15

>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

- Fungsi `f.tell()` digunakan untuk mengembalikan bilangan bulat yang memberikan posisi objek file saat ini, dalam file yang direpresentasikan sebagai jumlah byte dari awal file, saat dalam mode biner dan angka buram, dan saat dalam mode teks.

- Fungsi `f.seek(offseet, whence)` digunakan untuk mengubah posisi objek file. Posisi dihitung dari penambahan offset ke titik referensi; titik referensi dipilih oleh argumen where. Nilai whence dari 0 mengukur dari awal file, 1 menggunakan posisi file saat ini, dan 2 menggunakan akhir file sebagai titik referensi. `whence` dapat dihilangkan dan default ke 0, menggunakan awal file sebagai titik referensi.
```python
# Contoh f.seek(offset, whence)
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

### b. Saving structured data with json
Format `JSON` biasanya digunakan oleh aplikasi modern untuk memungkinkan pertukaran data. Daripada membuat user terus-menerus menulis dan men-debug kode untuk menyimpan tipe data yang rumit ke file, Python memungkinkan User untuk menggunakan format pertukaran data populer yang disebut `JSON (JavaScript Object Notation)`. Modul standar yang dipanggil json dapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string; proses ini disebut `serializing`. Merekonstruksi data dari representasi string disebut `deserializing`. Antara serializing dan deserializing, string yang mewakili objek mungkin telah disimpan dalam file atau data, atau dikirim melalui koneksi jaringan ke beberapa mesin yang jauh.
```python
# Contoh Saving structured data with json
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
# Output
'[1, "simple", "list"]'
```