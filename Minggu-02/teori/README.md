# BAB 4 : Control Flow
`Control flow` dalam bahasa Indonesia dapat diartikan sebagai aliran kendali. Maksud sebenarnya dari control flow adalah bagaimana urutan eksekusi perintah di dalam program. Control Flow adalah sebuah cara untuk memberi tahu program instruksi apa yang harus dijalankan.

## 1. Pernyataan If
Pernyataan `If` digunakan untuk mengantisipasi kondisi yang terjadi saat jalannya program dan menentukan tindakan apa yang akan diambil sesuai dengan kondisi. Pada python ada beberapa statement/kondisi diantaranya adalah `if`, `else` dan `elif`. 
- Kondisi `if` digunakan untuk mengeksekusi kode jika kondisi bernilai benar True. Jika kondisi bernilai salah False, maka statement/kondisi `if` tidak akan dieksekusi. 
- Kondisi `else` digunakan untuk mengeksekusi kode jika kondisi `if` bernilai salah False maka akan mengeksekusi kode di dalam `else`.
- Kondisi `elif` digunakan untuk mengeksekusi kode jika kondisi kode program yang akan menyeleksi beberapa kemungkinan yang bisa terjadi. Hampir sama dengan kondisi `else`, bedanya kondisi `elif` bisa banyak dan tidak hanya satu.

Dibawah ini adalah contoh penggunaan kondisi `if`, `elif` dan `else` pada **Python** :
```python
# Bentuk penggunaan kondisi 'if', 'elif', dan 'else'
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
# Output Program
More
```

## 2. Pernyataan For
Pernyataan `For` digunakan untuk melakukan perulangan berdasarkan interval yang ditentukan pengguna. Perulangan `For` pada bahasa pemrograman `Python` mempunyai kelebihan yang tidak hanya berdasarkan range bilangan, juga termasuk perulangan terhadap item suatu urutan (**list** atau **string**).

Dibawah ini adalah contoh penggunaan perulangan `for` pada **Python** :
```python
# Bentuk penggunaan perulangan for
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
# Output Program
cat 3
window 6
defenestrate 12
```

## 3. Fungsi Range()
Fungsi `range()` digunakan untuk mengembalikan deret bilangan bulat (integer) secara berurutan pada kisaran (range) yang sudah ditentukan dari start sampai stop. `Range` dengan satu parameter akan menghasilkan list dengan rentang parameter itu. Sedangkan ``Range` dengan dua parameter akan menghasilkan list dengan rentang dari parameter pertama sampai parameter kedua. Kemudian, `Range` yang menggunakan tiga parameter akan menghasilkan list dengan rentang dari parameter pertama sampai parameter kedua dengan jarak interval parameter ketiga.

Dibawah ini adalah contoh penggunaan fungsi `range()` pada **Python** :
```python
# Bentuk penggunaan function range()
>>> for i in range(5):
...     print(i)
...
# Output Program
0
1
2
3
4
```

## 4. Break dan Continue
Perintah `Break` merupakan perintah khusus yang digunakan untuk memaksa perulangan berhenti sebelum waktunya. Perintah break ini dapat di gunakan dalam perulangan `for` maupun `while` di python. Sedangkan perintah `Continue` mirip seperti perintah break, hanya saja jika dalam perintah break perulangan langsung berhenti, untuk perintah continue perulangan hanya melewati 1 kali proses iterasi saja.

Dibawah ini adalah contoh penggunaan fungsi `break` pada **Python** :
```python
# Bentuk penggunaan function break
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
# Output Program
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

Dibawah ini adalah contoh penggunaan fungsi `continue` pada **Python** :
```python
# Bentuk penggunaan function continue
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found an odd number", num)
...
# Output Program
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```

## 5. Pernyataan Pass
Pernyataan `Pass` adalah sebuah statement pada `python` yang tidak memiliki tugas apa pun. Tidak menginstruksi sistem untuk melakukan satu hal pun. Ia ada, tapi keberadaannya seolah tidak ada. Statement `pass` berguna sebagai `placeholder` untuk suatu fungsi atau suatu class yang belum diimplementasikan secara nyata.

Dibawah ini adalah contoh penggunaan pernyataan `pass` pada **Python** :
```python
# Perulangan while
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...

# definisi class
>>> class MyEmptyClass:
...     pass
...

# placeholder
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
```

## 6. Pernyataan Match
Pernyataan `match`mengambil ekspresi dan membandingkan nilainya dengan pola berurutan yang diberikan sebagai satu atau lebih blok kasus. Ini sangat mirip dengan pernyataan `switch` di `C`, `Java` atau `JavaScript` (dan banyak bahasa lainnya), tetapi juga dapat mengekstrak komponen (elemen urutan atau atribut objek) dari nilai ke dalam variabel.

Dibawah ini adalah contoh penggunaan pernyataan `match` pada **Python** :
```python
# Bentuk penggunaan pernyataan match
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

## 7. Mendefinisikan Fungsi
Fungsi `Defining` atau biasanya disebut `def` adalah kata kunci yang digunakan untuk mendefinisikan sebuah function. `function` sendiri adalah kelompok kode yang dapat digunakan kembali di bagian program yang lain. Sebab `Python` adalah bahasa pemrograman `multi-paradigma`, dalam paradigma `OOP` (pemrograman berorientasi objek), kata kunci `def` digunakan juga untuk mendefinisikan `method` alias fungsi dalam sebuah `class`.

Dibawah ini adalah contoh penggunaan function `def` pada **Python** :
```python
# Bentuk penggunaan function def
>>> def fib2(n):  # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # call it
>>> f100                # write the result
# Output Program
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

## 8. Lebih lanjut tentang Mendefinisikan Fungsi
Dimungkinkan juga untuk mendefinisikan `funtion` dengan sejumlah variabel argumen. Ada beberapa bentuk, yang bisa digabungkan.
### a. Nilai Argumen Bawaan (default)
Bentuk yang paling berguna adalah untuk menentukan nilai `default` untuk satu atau lebih argumen. Ini menciptakan fungsi yang dapat dipanggil dengan argumen yang lebih sedikit daripada yang ditentukan untuk diizinkan.

Sebagai contoh :
```python
# Bentuk Default Argument Values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

### b. Kata Kunci Arguments
Dalam panggilan fungsi, argumen `keywords` harus mengikuti argumen posisi. Semua argumen kata kunci yang diteruskan harus cocok dengan salah satu argumen yang diterima oleh function (misalnya aktor bukan argumen yang valid untuk `parrot` fungsi tersebut), dan urutannya tidak penting. Ini juga termasuk argumen non-opsional (misalnya parrot(voltage=1000) valid juga). Tidak ada argumen yang dapat menerima nilai lebih dari sekali.

Sebagai contoh :
```python
# Bentuk Keyword Arguments
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```

### c. Parameter Spesial
Secara default, argumen dapat diteruskan ke fungsi `Python` baik dengan posisi atau secara eksplisit dengan keyword. Untuk keterbacaan dan kinerja, masuk akal untuk membatasi cara argumen dapat diteruskan sehingga pengembang hanya perlu melihat definisi fungsi untuk menentukan apakah item dilewatkan berdasarkan posisi, posisi atau keyword, atau keyword.

Sebagai contoh :
```python
# Bentuk Special Parameters
>>> def standard_arg(arg):
...     print(arg)
...
>>> def pos_only_arg(arg, /):
...     print(arg)
...
>>> def kwd_only_arg(*, arg):
...     print(arg)
...
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)
```

### d. Arbitrary Argument Lists
Akhirnya, opsi yang paling jarang digunakan adalah menentukan bahwa suatu fungsi dapat dipanggil dengan sejumlah argumen yang berubah-ubah. Argumen-argumen ini akan dibungkus dalam sebuah tuple (lihat `Tuples` and `Sequences` ). Sebelum jumlah variabel argumen, nol atau lebih argumen normal dapat terjadi.

Sebagai contoh :
```python
# Bentuk Arbitrary Argument Lists
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```

### e. Unpacking Argument Lists
Situasi sebaliknya terjadi ketika argumen sudah ada dalam daftar atau tupel tetapi perlu dibongkar untuk pemanggilan fungsi yang memerlukan argumen posisi terpisah. Misalnya, function `range()` bawaan mengharapkan argumen mulai dan berhenti yang terpisah. Jika tidak tersedia secara terpisah, tulis pemanggilan fungsi dengan operator `*-` untuk membongkar argumen dari daftar atau tupel.

Sebagai contoh :
```python
# Bentuk Unpacking Argument Lists
>>> list(range(3, 6))    # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))   # call with arguments unpacked from a list
[3, 4, 5]
```

### f. Ekspresi Lambda
Fungsi anonim kecil dapat dibuat dengan kata kunci `lambda`. Fungsi ini mengembalikan jumlah dari dua argumennya. Fungsi `Lambda` dapat digunakan di mana pun objek fungsi diperlukan. Mereka secara sintaksis terbatas pada satu ekspresi. Secara semantik, mereka hanyalah gula sintaksis untuk definisi fungsi normal. Seperti definisi fungsi bersarang, fungsi `lambda` dapat mereferensikan variabel dari cakupan yang berisi:`lambda` a, b: a + b.

Sebagai contoh :
```python
# Bentuk Lambda Expressions
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
# Output f(0)
42
>>> f(1)
# Output f(1)
43
```

### g. String Dokumentasi
- Baris pertama harus selalu merupakan ringkasan singkat dan ringkas dari tujuan objek. Untuk singkatnya, itu tidak boleh secara `eksplisit` menyatakan nama atau jenis objek, karena ini tersedia dengan cara lain (kecuali jika nama itu merupakan kata kerja yang menggambarkan operasi suatu fungsi). Baris ini harus dimulai dengan huruf kapital dan diakhiri dengan titik.
- Jika ada lebih banyak baris dalam `string dokumentasi`, baris kedua harus kosong, yang secara visual memisahkan ringkasan dari deskripsi lainnya. Baris berikut harus berupa satu atau lebih paragraf yang menjelaskan konvensi pemanggilan objek, efek sampingnya, dll.

Sebagai contoh :
```python
# Bentuk Documentation Strings
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
# Output Program
Do nothing, but document it.

    No, really, it doesn't do anything.
```

### h. Anotasi Fungsi
`Anotasi` merupakan informasi metadata opsional tentang jenis yang digunakan oleh fungsi yang ditentukan pengguna. Anotasi disimpan dalam atribut `__annotations__` fungsi sebagai kamus dan tidak berpengaruh pada bagian lain dari fungsi tersebut. Anotasi parameter ditentukan oleh titik dua setelah nama parameter, diikuti dengan ekspresi yang mengevaluasi nilai anotasi. Anotasi pengembalian ditentukan oleh literal `->`, diikuti oleh ekspresi, antara daftar parameter dan titik dua yang menunjukkan akhirdefpernyataan. 

Contoh berikut memiliki argumen yang diperlukan, argumen opsional, dan nilai kembalian yang dianotasi :
```python
# Bentuk Function Annotations 
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
# Output Program
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

## 9. Intermezzo: Coding Style
Ketika akan menulis bagian `Python` yang lebih panjang dan lebih kompleks, inilah saatnya yang tepat untuk membicarakan tentang gaya pengkodean Python. Sebagian besar bahasa dapat ditulis (atau lebih ringkas, diformat ) dalam gaya yang berbeda; beberapa lebih mudah dibaca daripada yang lain. Mempermudah orang lain untuk membaca kode merupakan ide yang bagus, dan mengadopsi gaya pengkodean yang bagus sangat membantu untuk itu.

Untuk Python, `PEP 8` telah muncul sebagai panduan gaya yang dipatuhi sebagian besar proyek; itu mempromosikan gaya pengkodean yang sangat mudah dibaca dan menyenangkan mata. Setiap pengembang Python harus membacanya di beberapa titik; berikut adalah poin terpenting yang diekstraksi :
- Gunakan lekukan 4 spasi, dan tanpa tab. 4 spasi adalah kompromi yang baik antara lekukan kecil (memungkinkan kedalaman sarang yang lebih besar) dan lekukan besar (lebih mudah dibaca). Tab menimbulkan kebingungan, dan sebaiknya ditinggalkan.
- Bungkus garis sehingga tidak melebihi 79 karakter. Ini membantu pengguna dengan layar kecil dan memungkinkan untuk memiliki beberapa file kode secara berdampingan pada layar yang lebih besar.
- Gunakan baris kosong untuk memisahkan fungsi dan kelas, dan blok kode yang lebih besar di dalam fungsi.
- Jika memungkinkan, berikan komentar pada baris mereka sendiri.
- Gunakan `docstrings`.
- Gunakan spasi di sekitar operator dan setelah koma, tetapi tidak langsung di dalam konstruksi tanda kurung: `a = f(1, 2) + g(3, 4)`
- Beri nama kelas dan fungsi Anda secara konsisten; konvensi adalah untuk digunakan UpperCamelCaseuntuk kelas dan `lowercase_with_underscores`untuk fungsi dan metode. Selalu gunakan self sebagai nama untuk argumen metode pertama (lihat Pandangan Pertama pada Kelas untuk mengetahui lebih lanjut tentang kelas dan metode).
- Jangan gunakan penyandian mewah jika kode Anda dimaksudkan untuk digunakan di lingkungan internasional. Default `Python`, `UTF-8`, atau bahkan `ASCII` biasa bekerja paling baik dalam hal apa pun.
- Demikian juga, jangan gunakan karakter `non-ASCII` dalam pengidentifikasi jika hanya ada sedikit kemungkinan orang yang berbicara bahasa yang berbeda akan membaca atau mempertahankan kode.