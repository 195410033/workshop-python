# BAB 9 : Classes

`Class` adalah prototipe yang ditentukan pengguna untuk objek yang mendefinisikan seperangkat atribut yang menjadi ciri objek kelas apa pun. `Classes` menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama-sama. Setiap `instance class` dapat memiliki atribut yang dilampirkan untuk mempertahankan statusnya. Instance class juga dapat memiliki metode (ditentukan oleh class) untuk memodifikasi statusnya.

Mekanisme `class` Python menambahkan kelas dengan sintaks dan semantik baru. Ini merupakan campuran dari mekanisme class yang ditemukan di `C++` dan `Modula-3`. Class Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme **class inheritance** memungkinkan beberapa kelas dasar, **class override** dapat mengganti method apa pun dari kelas atau kelas dasarnya, dan  **methode** dapat memanggil methode class dasar dengan nama yang sama. **Object** dapat berisi jumlah dan jenis data yang berubah-ubah. Seperti halnya **modules**, classes mengambil bagian dari sifat dinamis Python: dibuat saat runtime, dan dapat dimodifikasi lebih lanjut setelah pembuatan.

Dalam terminologi `C++`, biasanya anggota class (termasuk anggota data) bersifat publik (kecuali yang ada pada `Private Variables`), dan semua fungsi anggotanya adalah virtual. Seperti di `Modula-3`, tidak ada singkatan untuk mereferensikan anggota objek dari method: fungsi method dideklarasikan dengan argumen pertama eksplisit yang mewakili objek, yang disediakan secara implisit oleh panggilan. Seperti di `Smalltalk`, class itu sendiri adalah objek. Ini menyediakan semantik untuk mengimpor dan mengganti nama. Tidak seperti C++ dan Modula-3, tipe bawaan dapat digunakan sebagai kelas dasar untuk ekstensi oleh pengguna. Juga, seperti di C++, sebagian besar operator bawaan dengan sintaks khusus (operator aritmatika, subskrip, dll.) dapat didefinisikan ulang untuk instance kelas.

## 1. Sepatah Kata Tentang Nama dan Objek
`Object` memiliki individualitas, dan beberapa nama yang dapat diikat ke objek yang sama, ini dikenal sebagai `aliasing` dalam bahasa lain. Ini biasanya tidak disadari dan dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak dapat diubah (numbers, strings, tuples). Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang bisa berubah seperti list, dictionaries, dan sebagian besar jenis lainnya. Ini biasanya digunakan untuk kepentingan program, karena `alias` berperilaku seperti pointer dalam beberapa hal. Misalnya, melewatkan sebuah objek karena sebuah pointer yang dilewatkan oleh implementasi; dan jika suatu fungsi memodifikasi objek yang diteruskan sebagai argumen, pemanggil akan melihat perubahannya. ini menghilangkan kebutuhan akan dua mekanisme penerusan argumen yang berbeda seperti dalam `Pascal`.

## 2. Lingkup Python dan Namespaces
`Namespace` adalah pemetaan dari nama ke objek. Sebagian besar namespace saat ini diimplementasikan sebagai Python dictionaries, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin berubah di masa mendatang. Contoh namespace adalah: 
- Kumpulan built-in names (berisi fungsi seperti `abs()`, dan `built-in exception names`); 
- Kumpulan global names dalam modules; 
- dan local names dalam pemanggilan function. Dalam arti `set of attributes` dari suatu objek juga membentuk namespace. Hal penting yang perlu diketahui tentang namespace adalah bahwa sama sekali tidak ada hubungan antara nama di namespace yang berbeda; misalnya, dua module berbeda dapat mendefinisikan suatu fungsi `maximize` tanpa confusion—user modul harus mengawalinya dengan module name.

`Lingkup` adalah wilayah tekstual dari program Python di mana namespace dapat diakses secara langsung. “Dapat diakses secara langsung” di sini berarti bahwa referensi yang tidak memenuhi syarat untuk sebuah nama mencoba menemukan nama tersebut di namespace. Meskipun cakupan ditentukan secara statis, mereka digunakan secara dinamis. Setiap saat eksekusi, ada 3 atau 4 cakupan nested yang namespace dapat diakses secara langsung:
- Lingkup terdalam, yang dicari terlebih dahulu, berisi nama-nama lokal
- Cakupan dari setiap fungsi terlampir, yang dicari mulai dengan lingkup terlampir terdekat, berisi nama non-lokal, tetapi juga non-global
- Lingkup next-to-last berisi nama global module
- Lingkup terluar (dicari terakhir) adalah namespace yang berisi nama bawaan.

Contoh scopes dan namespaces :
```python
# Program
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# Output program
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

## 3. Pandangan Pertama terhadap Classes
### a. Definisi Sintaks Class
`Class definitions`, seperti definisi function (pernyataan `def`) harus dieksekusi sebelum memiliki efek apa pun (Pengguna bisa menempatkan class definition di cabang pernyataan `if`, atau di dalam function.). Dalam praktiknya, pernyataan di dalam class definition biasanya berupa definisi function, tetapi pernyataan lain diperbolehkan, dan terkadang berguna. Definisi fungsi di dalam kelas biasanya memiliki bentuk daftar argumen yang khas, dan ditentukan oleh konvensi pemanggilan untuk method.

Contoh class definitions :
```python
# Contoh class definition
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

Ketika class definition dimasukkan, namespace baru dibuat, dan digunakan sebagai lingkup lokal. Dengan demikian, semua tugas ke variabel lokal masuk ke namespace baru. Secara khusus, definisi fungsi mengikat nama fungsi baru. Ketika class definition dibiarkan secara normal, objek kelas dibuat. Ini pada dasarnya adalah pembungkus konten namespace yang dibuat oleh class definition.

### b. Objek Class
`Class object` mendukung dua jenis operasi: 
- *`Attribute references`* menggunakan sintaks standar yang digunakan untuk semua referensi atribut di Python: `obj.name`. Nama atribut yang valid adalah semua nama yang ada di ruang nama kelas saat objek kelas dibuat. Jadi, jika dalam class definition akan terlihat seperti ini:
```python
# Contoh attribute references
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```
- *`Class instantiation`* menggunakan notasi function. Anggap saja objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. Misalnya (dengan asumsi kelas di atas):
```python
# Contoh class instantiation
x = MyClass()

# Mendefinisikan method __init__()
def __init__(self):
    self.data = []
```

Ketika sebuah class mendefinisikan sebuah method `__init__()`, maka instantiasi class secara otomatis memanggil `__init__()` instance kelas yang baru dibuat. Jadi dalam contoh ini, instance baru yang diinisialisasi dapat diperoleh dengan :
```python
# Operator instantiaton
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
# Output
(3.0, -4.5)
```

### c. Instance Objects
Satu-satunya operasi yang dipahami oleh `instance objects` adalah referensi atribut. Ada dua jenis nama atribut yang valid, yaitu : 
- *`data attributes`* sesuai dengan "instance variable" di `Smalltalk`, dan "data members" di `C++`. Data attributes tidak perlu dideklarasikan; seperti variabel lokal, mereka muncul saat pertama kali ditugaskan.

Contoh *data attributes* :
```python
# Contoh data attributes
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```
- *`method`* adalah function yang “belongs to” suatu objek. (Dalam Python, istilah method tidak unik untuk `class instances`: tipe objek lain dapat memiliki method juga. Misalnya, objek list memiliki method yang disebut **append**, **insert**, **remove**, **sort**, dan sebagainya.)

Nama method yang valid dari `instance object` bergantung pada kelasnya. Menurut definisi, semua atribut kelas yang merupakan objek fungsi mendefinisikan method yang sesuai dari instance-nya.

### d. Objek Method
Ketika `non-data attribute` dari sebuah instance direferensikan, maka instance class akan dicari. Jika nama menunjukkan atribut kelas yang valid yang merupakan function object, `method object` dibuat dengan mengemas (menunjuk ke) instance object dan function object yang baru saja ditemukan bersama dalam objek abstrak: ini adalah method object. Ketika method object dipanggil dengan argument list, maka argument list baru dibuat dari instance object dan argument list, dan function object akan dipanggil dengan argument list yang baru.

### e. Class dan Instance Variables
`Instance variable` adalah untuk data yang unik untuk setiap instance dan class variables untuk atribut dan method yang dibagikan oleh semua class instance :
```python
# Contoh instance class
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```
Desain class yang benar untuk menggunakan instance variable sebagai berikut :
```python
# Contoh instance variable
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

### 4. Random Remarks
`Data attributes` dapat direferensikan oleh method serta oleh pengguna biasa ("klien") dari suatu objek. Dengan kata lain, class tidak dapat digunakan untuk mengimplementasikan tipe data abstrak murni. Faktanya, tidak ada dalam Python yang memungkinkan untuk memaksakan penyembunyian data, semuanya didasarkan pada konvensi.

Jika nama atribut yang sama terjadi di kedua instance dan di class, maka pencarian atribut memprioritaskan instance :
```python
>>> class Warehouse:
        purpose = 'storage'
        region = 'west'

>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```

Apapun `Function object` yang merupakan class attribute akan mendefinisikan sebuah method untuk class instance tersebut. Definisi function tidak perlu secara tekstual dilampirkan dalam class definition: menetapkan objek fungsi ke variabel lokal di kelas juga tidak masalah. Sebagai contoh:
```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```
`Method` dapat mereferensikan nama global dengan cara yang sama seperti fungsi biasa. Lingkup global yang terkait dengan suatu method adalah module yang berisi definition. Meskipun jarang ditemukan alasan yang baik untuk menggunakan data global dalam suatu method, ada banyak penggunaan yang sah dari lingkup global. Setiap nilai adalah objek, oleh karena itu memiliki class. Itu disimpan sebagai `object.__class__`.

## 5. Inheritance
`Inheritance` adalah sebuah proses dimana sebuah class mengambil semua properti dan semua method dari kelas lain. Inheritance biasanya disebut kelas turunan. Sintaks untuk class definition turunan terlihat seperti ini:
```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Eksekusi definisi kelas turunan berlangsung sama seperti untuk kelas dasar. Ketika objek kelas dibangun, kelas dasar diingat. Ini digunakan untuk menyelesaikan referensi atribut: jika atribut yang diminta tidak ditemukan di kelas, pencarian dilanjutkan untuk mencari di kelas dasar. Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri diturunkan dari beberapa kelas lain.

Python memiliki dua fungsi bawaan yang bekerja dengan Inheritance :
- Gunakan `isinstance()` untuk memeriksa jenis instance: `.isinstance(obj, int)` akan bernilai `True` hanya jika `obj.__class__` adalah int atau beberapa kelas turunan dari int.
- Gunakan `issubclass()` untuk memeriksa pewarisan kelas: `issubclass(bool, int)` adalah `True` karena `bool` adalah subclass dari int. Namun, `issubclass(float, int)` adalah `False` karena `float` bukan subclass dari int.

### a. Multiple Inheritance
Dalam kasus yang paling sederhana, Pengguna dapat menganggap pencarian atribut yang diwarisi dari parent class sebagai depth-first, left-to-right, bukan pencarian dua kali di kelas yang sama di mana terdapat tumpang tindih dalam hierarki. Jadi, jika suatu atribut tidak ditemukan di `DerivedClassName`, maka dicari di `Base1`, kemudian (secara rekursif) di kelas dasar Base1, dan jika tidak ditemukan di sana, dicari di `Base2`, dan seterusnya. Class definition dengan beberapa kelas dasar terlihat seperti ini :
```python
# Class definition multiple inheritance
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Faktanya, ini sedikit lebih kompleks; urutan resolusi method berubah secara dinamis untuk mendukung panggilan kooperatif ke `super()`. Pendekatan ini dikenal dalam beberapa bahasa `multiple-inheritance` lainnya sebagai metode panggilan berikutnya dan lebih kuat daripada panggilan super yang ditemukan dalam bahasa `single-inheritance`.

## 6. Private Variables
`Private` instance variables tidak dapat diakses kecuali dari dalam objek tidak ada di Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama yang diawali dengan garis bawah (misalnya **_spam**) harus diperlakukan sebagai bagian non-publik dari `API`. Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.

Ada kasus penggunaan yang valid untuk class-private members, ada dukungan terbatas untuk mekanisme seperti itu, yang disebut dengan nama `mangling`. Mangling ini dilakukan tanpa memperhatikan posisi sintaks dari pengenal, selama itu terjadi dalam class definition. Nama mangling berguna untuk membiarkan subclass menimpa method tanpa memutus panggilan method intraclass. Sebagai contoh:
```python
# Contoh mangling - Private Variables
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```
Aturan `mangling` sebagian besar dirancang untuk menghindari kecelakaan; masih dimungkinkan untuk mengakses atau memodifikasi variabel yang dianggap pribadi. Ini bahkan dapat berguna dalam keadaan khusus, seperti di debugger.

## 7. Odds and Ends
Terkadang berguna untuk memiliki tipe data yang mirip dengan "record" `Pascal` atau "struct" `C`, yang menggabungkan beberapa item data bernama. Class definition yang kosong akan berfungsi dengan baik:
```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```
Kode Python yang mengharapkan tipe data abstrak tertentu sering kali dapat dilewatkan ke class yang mengemulasi method tipe data itu sebagai gantinya. Instance method objects juga memiliki atribut: `m.__self__` adalah instance object dengan method `m()`, dan `m.__func__`merupakan objek fungsi yang sesuai dengan method.

## 8. Iterators
Penggunaan `iterator` meliputi dan menyatukan Python. Di balik layar, pernyataan `for` tersebut memanggil `iter()` objek container. Fungsi mengembalikan objek iterator yang mendefinisikan method `__next__()` yang mengakses elemen dalam wadah satu persatu. Ketika tidak ada lagi elemen, maka `__next__()` memunculkan `StopIteration` pengecualian yang memberitahu for loop untuk berhenti. Pengguna dapat memanggil method `__next__()` untuk menggunakan fungsi bawaan `next()`.

Contoh ini menunjukkan cara kerjanya:
```python
# Cara kerja Iterators
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
# Output
m
a
p
s
```

## 9. Generator
`Generator` adalah alat yang sederhana dan kuat untuk membuat iterator. Mereka ditulis seperti function biasa tetapi menggunakan pernyataan `yield` setiap kali mereka ingin mengembalikan data. Setiap kali `next()` dipanggil, generator akan melanjutkan dari tempat terakhirnya (ia mengingat semua nilai data dan pernyataan mana yang terakhir dieksekusi). Sebuah contoh menunjukkan bahwa generator dapat dibuat dengan mudah :
```python
# Contoh generator
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

>>> for char in reverse('golf'):
...     print(char)
...
# Output
f
l
o
g
```
Fitur utama lainnya adalah variabel lokal dan status eksekusi secara otomatis disimpan di antara panggilan. Ini membuat function lebih mudah untuk ditulis dan jauh lebih jelas daripada pendekatan menggunakan variabel instan seperti `self.index` dan `self.data`. Selain pembuatan method secara otomatis dan penyimpanan status program, ketika generator dihentikan, mereka secara otomatis menaikkan `StopIteration`. Dalam kombinasi, fitur-fitur ini memudahkan untuk membuat iterator dengan tidak lebih dari menulis function biasa.

## 10. Generator Expressions
`Generator Expressions` dirancang untuk situasi di mana generator digunakan langsung oleh function terlampir. Ekspresi generator lebih ringkas tetapi kurang fleksibel daripada definisi generator lengkap dan cenderung lebih ramah memori daripada pemahaman daftar yang setara.

Contoh generator expressions :
```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```