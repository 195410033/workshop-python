# BAB 8 : Errors and Exceptions

`Error Message Python` adalah pesan yang ditampilkan interpreter Python saat terjadi kesalahan, baik dari segi penulisan syntax maupun kesalahan terkait lainnya. Terdapat 2 jenis error pada Bahasa pemrograman Python yaitu `Error` dan `Exception`. Pesan tersebut mengindikasi perlu dilakukan penanganan error (debugging) terhadap kode Python yang dieksekusi.

## 1. Syntax Errors
`Syntax Error` adalah suatu keadaan saat kode python mengalami kesalahan penulisan. Python interpreter dapat mendeteksi kesalahan ini saat kode dieksekusi. Syntax Error, juga dikenal sebagai kesalahan penguraian, kesalahan ini mungkin merupakan jenis keluhan paling umum yang Pengguna dapatkan saat masih belajar Python. `Parser` mengulangi baris yang menyinggung dan menampilkan `^` 'panah' kecil yang menunjuk pada titik paling awal di baris tempat kesalahan terdeteksi. Kesalahan disebabkan oleh (atau setidaknya terdeteksi pada) token sebelum panah.

Contoh Syntax Errors :
```python
# Contoh Syntax Errors
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

## 2. Exceptions
`Exception` adalah suatu keadaan saat penulisan syntax sudah benar, namun kesalahan terjadi karena syntax tidak bisa dijalankan, melainkan karena adanya kesalahan matematika, kesalahan nama function, library, dan lainnya. Terdapat 3 jenis Exception di bahasa pemrograman Python, yaitu `ZeroDivisionError`, `NameError`, dan `TypeError`.
- `ZeroDivisionError` adalah exception yang terjadi saat eksekusi program menghasilkan perhitungan matematika pembagian dengan angka nol;
- `NameError` adalah exception yang terjadi saat kode mengeksekusi terhadap local name atau global name yang tidak terdefinisi;
- `TypeError` adalah exception yang terjadi saat dilakukan eksekusi terhadap suatu operasi atau fungsi dengan tipe objek yang tidak sesuai.

Contoh Exceptions :
```python
# ZeroDivisionError
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

# NameError
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined

# TypeError
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

## 3. Handling Exceptions
`Handling Exceptions` merupakan mekanisme yang paling diperlukan dalam menangani error yang terjadi pada saat runtime (program berjalan) atau yang lebih dikenal dengan sebutan runtime error. Secara umum, adanya kesalahan / error yang terjadi pada program pada saat runtime dapat menyebabkan program berhenti. Untuk itulah diperlukan mekanisme untuk memastikan bahwa program tetap dapat berjalan meskipun terdapat kesalahan yang terjadi.

Exception Handling dapat dilakukan menggunakan keyword `try-catch`. Keyword `try` digunakan untuk menentukan bagian statement program dimana akan terjadi pengecualian, sedangkan keyword `except` digunakan untuk menangani kesalahan / pengecualian yang terjadi.

Contoh Handling Exceptions :

```python
# Contoh Handling Exceptions :
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

## 4. Raising Exceptions
`Raise Exceptions` adalah pengecualian (exception) yang dibangkitkan, hanya untuk meningkatkan pernyataan pengecualian tanpa mengangani sebuah error pada keluaran shell python. Ketika dimana raise tidak ada pengecualian (Except), jadi raise mengeluarkan nilai parameter tanpa menangani error.

Contoh Raising Exceptions :

```python
# Contoh Raising Exceptions
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

## 5. Exception Chaining
`Exception Chaining` merupakan exception yang bisa asosiasikan satu exception dengan exception lainnya. Exception Chaining terjadi secara otomatis ketika pengecualian dinaikkan di dalam `except` atau bagian `finally`, ini dapat dinonaktifkan dengan menggunakan `from None`.

Contoh Exception Chaining

```python
# Contoh Exception Chaining
>>> try:
...    open('database.sqlite')
... except OSError:
...    raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

## 6. User-defined Exceptions
`User-defined Exceptions` merupakan exception yang dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk pengecualian. Sebagian besar Exception didefinisikan dengan nama yang diakhiri dengan "Error", mirip dengan penamaan standar except.

## 7. Defining Clean-up Actions
`Defining Clean-up Actions` merupakan exception yang pernyataan `try` klausa memiliki opsional lain untuk mendefinisikan tindakan define clean-up actions dalam semua keadaan. Jika ada pernyataan `finally` klausa, maka finally klausa akan dieksekusi sebagai tugas terakhir sebelum pernyataan try selesai.

Contoh Defining Cleaning-up Actions :

```python
# Contoh Defining Cleaning-up Actions
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```

## 8. Predefined Clean-up Actions
`Predefined Clean-up Actions` merupakan exception yang beberapa objek-nya menentukan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Pernyataan `with` memungkinkan objek seperti file untuk digunakan dengan cara yang memastikan mereka selalu dibersihkan dengan cepat dan benar. Setelah pernyataan dieksekusi, file selalu ditutup, bahkan jika ada masalah saat memproses baris. Objek yang seperti file menyediakan tindakan pembersihan yang telah ditentukan sebelumnya akan menunjukkan hal ini dalam dokumentasinya.

Contoh Predefined Clean-up Actions :

```python
# Contoh Predefined Clean-up Actions
for line in open("myfile.txt"):
    print(line, end="")

# Statement with
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```