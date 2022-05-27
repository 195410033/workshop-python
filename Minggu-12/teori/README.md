# Jupyter
`Jupyter` adalah aplikasi web gratis untuk yang digunakan untuk membuat dan membagikan dokumen yang memiliki kode, hasil hitungan, visualisasi, dan teks. Jupyter adalah singkatan dari tiga bahasa pemrograman `Julia` (Ju), `Python` (Py), dan `R`. Tiga bahasa pemrograman ini adalah sesuatu yang penting bagi seorang data `scientist`. 

Jupyter berfungsi untuk membantu kamu dalam membuat narasi komputasi yang menjelaskan makna dari data di dalamnya dan memberikan insight mengenai data tersebut. Selain itu, Jupyter juga mempermudah kerja sama antara insinyur dan data scientist karena kemudahannya dalam menulis dan berbagi teks dan kode.Karena alasan inilah, Jupyter mempermudah data scientist untuk berkolaborasi dengan data scientist, data researchers atau data engineers lainnya.

Jupyter sendiri terbagi menjadi beberapa model, diantaranya :
- `JupyterLab` adalah interactive development environment yang berbasis web untuk jupyter notebooks kode program, dan data. JupyterLab fleksibel dalam hal mendukung workflow untuk data sains, komputasi ilmiah, dan machine learning.
- `Jupyter Notebook` adalah aplikasi web asli untuk membuat dan berbagi dokumen komputasi. Ini menawarkan pengalaman yang sederhana, efisien, dan berpusat pada dokumen.
- `Voilà` adalah aplikasi web yang membantu mengomunikasikan wawasan dengan mengubah buku catatan menjadi aplikasi web mandiri yang aman yang dapat disesuaikan dan bagikan.

## Install JupyterLab
1. Instal JupyterLab mengggunakan perintah pip:
    ```
    pip install jupyterlab
    ```
    `Catatan` : Jika menginstal JupyterLab dengan `conda` atau `mamba`, sebaiknya gunakan saluran `conda-forge`.

2. Setelah terinstal, untuk menjalankan JupyterLab dengan:
    ```
    jupyter-lab
    ```

## Install Jupyter Notebook
1. Instal Jupyter Notebook mengggunakan perintah:
    ```
    pip install notebook
    ```

2. Setelah terinstal, untuk menjalankan JupyterLab dengan:
    ```
    jupyter notebook
    ```

## Install Voila
1. Instal Voila mengggunakan perintah:
    ```
    pip install voila
    ```

## Struktur Data menggunakan JupyterLab
`Struktur Data` adalah cara penyimpanan, penyusunan dan pengaturan data di dalam media media penyimpanan komputer sehingga data tersebut dapat digunakan secara efisien. Dalam teknik pemrograman, struktur data berarti tata letak data yang berisi kolom-kolom data, baik itu kolom yang tampak oleh pengguna (user) ataupun kolom yang hanya digunakan untuk keperluan pemrograman yang tidak tampak oleh pengguna.

## 1. More on Lists
`List` adalah tipe data yang paling serbaguna yang tersedia dalam bahasa `Python`, yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (item) antara tanda kurung siku. Hal penting tentang daftar adalah item dalam list tidak boleh sama jenisnya.

Tipe data `list` memiliki beberapa method, Berikut adalah semua method objek dalam list:
|No|Python Methods|Penjelasan|
| -- | -------- | ----- |
|1|list.**append**(obj)|Menambahkan objek obj ke list|
|2|list.**extend**(seq)|Tambahkan isi seq ke list|
|3|list.**insert**(index, obj)|Sisipkan objek ke dalam list di indeks offset|
|4|list.**remove**(obj)|Removes object obj from list|
|5|list.**pop**(obj = list[-1])|Menghapus dan mengembalikan objek atau obj terakhir dari list|
|6|list.**clear**()|Menghapus semua item dalam list|
|7|list.**index**(obj)|Mengembalikan indeks terendah dalam list di indeks offset|
|8|list.**count**(obj)|Jumlah pengemmbalian berapa kali obj terjadi dalam list|
|9|list.**sort**(func)|Urutkan objek list, gunakan compare func jika diberikan|
|10|list.**reverse**()|Membalik list objek di tempat|
|11|list.**copy**()|Mengembalikan salinan list|

Dibawah ini adalah contoh penggunaan Tipe data `List` pada Python :
```python
# Bentuk penggunaan tipe data list
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# list.count(obj)
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0

# list.index(obj)
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6

# list.reverse()
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

# list.append(obj)
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

# list.sort(func)
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

# list.pop(obj = list[-1])
>>> fruits.pop()
'pear'
```

Hal lain yang mungkin perlu perhatikan adalah tidak semua data dapat diurutkan atau dibandingkan. Misalnya, tidak mengurutkan karena bilangan bulat tidak dapat dibandingkan dengan **string** dan Tidak Ada tidak dapat dibandingkan dengan tipe lain. Juga, ada beberapa tipe yang tidak memiliki relasi pengurutan yang ditentukan. Misalnya, bukan perbandingan yang valid. Contohnya, `3 + 4j < 4 + 7j` bukan perbandingan yang valid.

### a. Menggunakan List sebagai Stacks
Metode `list` ini memudahkan untuk menggunakan list sebagai tumpukan,  di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil (*"masuk terakhir, keluar pertama"*). Untuk menambahkan item ke bagian atas tumpukan, gunakan `append()`. Untuk mengambil item dari atas tumpukan, gunakan `pop()` tanpa indeks eksplisit. 

Sebagai contoh:
```python
# Bentuk penggunaan metode Stacks
>>> stack = [3, 4, 5]

# append()
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]

# pop()
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5

# Hasil akhir
>>> stack
[3, 4]
```

### b. Menggunakan List sebagai Queues
Metode `Queues` ini menggunakan list sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil (*"masuk pertama, keluar pertama"*); namun, list tidak efisien untuk tujuan ini. Sementara menambahkan dan memunculkan dari akhir list secara cepat, melakukan sisipan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu). Untuk mengimplementasikan antrian, gunakan `collections.deque` yang dirancang untuk menambahkan dan memunculkan dengan cepat dari kedua ujungnya. 

Sebagai contoh:
```python
# Bentuk penggunaan metode Queues
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'

# Hasil akhir
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### c. List Comprehensions
`List Comprehensions` menyediakan cara ringkas untuk membuat list. `Common aplications` adalah untuk membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau iterable, atau untuk membuat sub urutan dari elemen-elemen yang memenuhi kondisi tertentu. 

Sebagai contoh:
```python
# Bentuk penggunaan metode squares
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

`List Comprehensions` terdiri dari tanda kurung yang berisi ekspresi yang diikuti oleh **for klausa**, lalu nol atau lebih **for** atau **if klausa**. Hasilnya adalah list baru yang dihasilkan dari evaluasi ekspresi dalam konteks **for** dan **if klausa** yang mengikutinya. Sebagai contoh:

```python
# Bentuk penggunaan metode listcomp
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

### d. Nested List Comprehensions
Ekspresi awal dalam `List Comprehensions` dapat berupa ekspresi arbitrer, termasuk **List Comprehensions** lainnya. Perhatikan contoh berikut dari **matriks 3x4** yang diimplementasikan sebagai daftar 3 baris 4 kolom:
```python
# Bentuk matriks 3 x 4
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

`List Comprehensions` tersebut dapat diubah menjadi sebagai berikut:
```python
# Bentuk penggunaan List Comprehensions
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

Di dunia nyata, Pengguna harus lebih memilih fungsi bawaan daripada pernyataan aliran yang kompleks. Fungsi `zip()` ini akan melakukan pekerjaan yang baik untuk kasus penggunaan ini:

```python
# Bentuk penggunaan fungsi zip()
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

## 2. Pernyataan del 
Ada cara untuk menghapus item dari list yang diberikan indeksnya alih-alih nilainya: pernyataan `del`. Ini berbeda dari metode `pop()` yang mengembalikan nilai. Pernyataan `del` juga dapat digunakan untuk menghapus irisan dari list atau menghapus seluruh list (yang kita lakukan sebelumnya dengan menetapkan list kosong ke irisan). 

Sebagai contoh:
```python
# Bentuk penggunaan statement del
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

## 3. Tuples dan Sequences
`Tupel` adalah urutan objek Python seperti list yang tidak berubah. Perbedaan utama antara tupel dan list adalah bahwa tupel tidak dapat diubah tidak seperti List Python. Tupel menggunakan tanda kurung, sedangkan `List Python` menggunakan tanda kurung siku. Membuat tuple semudah memasukkan nilai-nilai yang dipisahkan koma. Secara opsional, Pengguna dapat memasukkan nilai-nilai yang dipisahkan koma ini di antara tanda kurung juga. 

Sebagai contoh :
```python
# Bentuk penggunaan Tuple
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

### 4. Set
`Python` juga menyertakan tipe data untuk set. `Himpunan` adalah kumpulan yang tidak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. `Set` objek juga mendukung operasi matematika seperti serikat pekerja, persimpangan, perbedaan, dan perbedaan simetris. Kurung kurawal atau fungsi`set()` dapat digunakan untuk membuat himpunan. 

**Catatan**: *untuk membuat set kosong Anda harus menggunakan `set()`, bukan {}; yang terakhir membuat kamus kosong, struktur data yang akan kita bahas di bagian selanjutnya.*

Sebagai contoh :
```python
# Bentuk penggunaan fungsi set()
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

### 5. Dictionaries
Tipe data lain yang berguna yang dibangun ke dalam Python adalah Dictionary. `Dictionaries` kadang-kadang ditemukan dalam bahasa lain sebagai **"associative memories"** atau **"associative arrays"**. Tidak seperti urutan, yang diindeks oleh rentang angka, dictionaries diindeks oleh keys, yang dapat berupa tipe apa pun yang tidak dapat diubah; **string** dan **angka** selalu bisa menjadi key. `Tuple` dapat digunakan sebagai key jika hanya berisi string, angka, atau tupel; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung maupun tidak langsung, itu tidak dapat digunakan sebagai key. Pengguna tidak dapat menggunakan list sebagai key, karena list dapat dimodifikasi di tempat menggunakan penetapan indeks, penetapan irisan, atau metode seperti `append()` dan `extend()`.

Operasi utama pada `dictionary` adalah menyimpan nilai dengan beberapa key dan mengekstrak nilai yang diberikan key tersebut. Dimungkinkan juga untuk menghapus pasangan key:*value* dengan *del*. Jika Pengguna menyimpan menggunakan key yang sudah digunakan, nilai lama yang terkait dengan key tersebut akan terlupakan. Ini adalah kesalahan untuk mengekstrak nilai menggunakan key yang tidak ada.

Melakukan `list(d)` di dictionary mengembalikan daftar semua key yang digunakan dalam dictionary, dalam urutan penyisipan (jika Pengguna ingin diurutkan, gunakan `sorted(d)` saja). Untuk memeriksa apakah suatu key ada dalam dictionary, gunakan perintah `in`.

Berikut adalah contoh kecil menggunakan `dictonary`:
```python
# Bentuk penggunaan tipe data list
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False

# Bentuk penggunaan konstruktor dict()
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## 6. Teknik Perulangan
Saat mengulang melalui `dictionary`, key dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan metode `items()`.
```python
# Bentuk penggunaan metode items()
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

Saat mengulang melalui urutan, indeks posisi dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan fungsi `enumerate()`.
```python
# Bentuk penggunaan fungsi enumerate()
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

Untuk mengulang dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan fungsi `zip()`.
```python
# Bentuk penggunaan fungsi zip()
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil fungsi `reversed()`.
```python
# Bentuk penggunaan fungsi resersed()
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

Untuk mengulang urutan dalam urutan terurut, gunakan fungsi `sorted()` yang mengembalikan daftar terurut baru sambil membiarkan sumbernya tidak berubah.
```python
# Bentuk penggunaan fungsi sorted()
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```

Menggunakan fungsi `set()` pada urutan menghilangkan elemen duplikat. Penggunaan `sorted()` kombinasi dengan `set()` lebih dari urutan adalah cara idiomatik untuk mengulang elemen unik dari urutan dalam urutan yang diurutkan.
```python
# Bentuk penggunaan fungsi set()
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

Terkadang tergoda untuk mengubah list saat Pengguna mengulangnya; namun, seringkali lebih sederhana dan lebih aman untuk membuat list baru.
```python
# Bentuk penggunaan membuat list baru
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

## 7. Kondisi
Kondisi yang digunakan dalam pernyataan `while` dan `if` dapat berisi operator apa pun, bukan hanya perbandingan. Operator perbandingan `in` dan `not in` merupakan keanggotaan yang menentukan apakah suatu nilai ada di (atau tidak) dalam wadah. Operator dan membandingkan apakah dua objek benar-benar objek yang sama. Semua operator pembanding memiliki prioritas yang sama, yaitu lebih rendah dari semua operator numerik

`Comparisons` dapat digabungkan menggunakan operator Boolean `and` dan `or`, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan `not`. Ini memiliki prioritas lebih rendah daripada operator pembanding; antara mereka, `not` memiliki prioritas tertinggi dan `or` terendah, sehingga setara dengan *A and not B or C is equivalent (A and (not B)) or C*. Seperti biasa, tanda kurung dapat digunakan untuk menyatakan komposisi yang diinginkan.

Operator Boolean `and` dan `or` yang disebut operator `short-circuit`: argumen tersebut dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika *A* dan *C* benar tetapi *B* salah, maka *A* and *B* and *C* tidak mengevaluasi ekspresi *C*. Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator `short-circuit` adalah argumen terakhir yang dievaluasi.

Dimungkinkan untuk menetapkan hasil `comparison` atau ekspresi Boolean lainnya ke variabel. Sebagai contoh:
```python
# Bentuk penggunaan operator comparison
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

### 8. Membandingkan Urutan dan Jenis
`Sequence objects` biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingannya menggunakan *lexicographical ordering*: yang pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis. Jika dua item yang akan dibandingkan itu sendiri merupakan urutan dari jenis yang sama, perbandingan `lexicographical` dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutan dianggap sama. Jika satu barisan merupakan sub-urutan awal dari yang lain, barisan yang lebih pendek adalah yang lebih kecil (*lesser*). *Lexicographical ordering* untuk string menggunakan nomor titik kode Unicode untuk mengurutkan karakter individual. 

Beberapa contoh `comparisons` antara `sequences` dari jenis yang sama:
```python
# Bentuk penggunaan Comparing Sequences
1, 2, 3)               < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```

Perhatikan bahwa membandingkan objek dari jenis yang berbeda dengan `<` atau `>` legal asalkan objek tersebut memiliki metode perbandingan yang sesuai. Misalnya, tipe numerik campuran dibandingkan menurut nilai numeriknya, jadi 0 sama dengan 0,0, dll. Jika tidak, alih-alih memberikan pengurutan arbitrer, penerjemah akan memunculkan `TypeError exception`.