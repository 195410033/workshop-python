# BAB 6 : Modules

`Python` memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam script atau dalam instance interpreter yang interactive. File seperti itu disebut `module`, definisi dari sebuah module dapat diimpor ke modul lain atau ke modul utama.

`Module` pada Python adalah sebuah file yang berisikan sekumpulan kode fungsi, class dan variabel yang disimpan dalam satu file berekstensi `.py` dan dapat dieksekusi oleh interpreter Python. Nama dari module .py merupakan nama dari file itu sendiri. Misalkan kita memiliki file bernama `"fibo.py"`, maka kita telah membuat sebuah module bernama "fibo" dan module sendiri bisa memiliki berbagai macam isi, baik itu fungsi, class, maupun variabel.

Berikut ini adalah contoh penggunaan fungsi module `fibo.py` pada Python :
```python
# Fibonacci numbers module
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Kemudian masukkan interpreter Python dan import module `fibo.py` untuk menjalankan module tersebut :
```python
# Perintah import fibo.py
>>> import fibo

# Mengakses fungsi yang ada dalam module fibo.py
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'

# fungsi untuk menetapkan nama lokal module fibo.py
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## 1. More on Modules
`Module` dapat berisi pernyataan yang dapat dieksekusi serta didefinisikan sebagai fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Modul tersebut dieksekusi hanya saat pertama kali nama modul ditemukan dalam pernyataan import.

Setiap module memiliki tabel simbol pribadi sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam module. Dengan demikian, penulis module dapat menggunakan `variabel global` dalam module tanpa khawatir jika mengalami kesamaan yang tidak disengaja dengan variabel global pengguna. Module digunakan untuk memecah sebuah program besar menjadi file yang lebih kecil agar lebih mudah dimanage dan diorganisir. Module membuat kode bersifat `reusable`, artinya satu module bisa dipakai berulang dimana saja diperlukan.

`Module` dapat mengimpor modul lain. Module biasanya tidak diharuskan untuk menempatkan semua import pernyataan di awal modul. Nama modul yang diimpor ditempatkan di tabel simbol global modul pengimpor. Ada varian dari `import` pernyataan yang mengimpor nama dari modul langsung ke tabel simbol modul pengimpor. 

Berikut ini adalah contoh penggunaan fungsi module `fibo.py` pada Python :
```python
# Mengakses fungsi yang ada dalam module fibo.py
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# Mengakses semua nama ada dalam modul menggunakan simbol `*`
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# Mengakses fungsi module menggunakan perintah `as`
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# Mengakses fungsi module menggunakan perintah `from`
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

**Catatan :**
*Untuk alasan efisiensi, setiap modul hanya diimpor sekali per sesi juru bahasa. Oleh karena itu, jika Pengguna mengubah modul, Pengguna harus memulai ulang penerjemah atau jika hanya satu modul yang ingin Pengguna uji secara interaktif, gunakan `importlib.reload()`, `mis .import importlib`; `importlib.reload(modulename)`*

### - Menjalankan modules sebagai scripts
Saat Pengguna menjalankan module Python dengan `python fibo.py <arguments>`, perintah dalam module akan dieksekusi, sama seperti jika Pengguna mengimpornya, tetapi dengan `__name__` set ke `"__main__"`. Itu berarti dengan menambahkan kode ini di akhir module, seperti berikut ini :
```python
# Penggunaan script
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
Pengguna dapat membuat file yang dapat digunakan sebagai skrip serta module yang dapat diimpor, karena kode yang mem-parsing baris perintah hanya berjalan jika modul dijalankan sebagai file "main". Ini sering digunakan untuk menyediakan antarmuka pengguna yang nyaman ke module, atau untuk tujuan pengujian (menjalankan modul saat skrip mengeksekusi rangkaian pengujian).

Berikut ini adalah contoh program penggunaan *script* :
```python
# Penggunaan modules as scripts
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34

# Perintah import fibo.py
>>> import fibo
```

### - Module Search Path
Ketika sebuah module bernama `spam` diimport, interpreter pertama mencari modul `built-in` dengan nama itu. Jika tidak ditemukan, maka akan mencari file bernama `spam.py` dalam daftar direktori yang diberikan oleh variabel sys.path. `sys.path` diinisialisasi dari lokasi ini:
- Direktori yang berisi skrip input (atau direktori saat ini ketika tidak ada file yang ditentukan).
- `PYTHONPATH`(daftar nama direktori, dengan sintaks yang sama dengan variabel shell `PATH`).
- Default yang bergantung pada instalasi (berdasarkan konvensi termasuk `site-packages` direktori, ditangani oleh site module).

**Catatan :**
*Pada sistem file yang mendukung symlink, direktori yang berisi skrip input dihitung setelah symlink diikuti. Dengan kata lain direktori yang berisi symlink tidak ditambahkan ke jalur pencarian modul.*

Setelah inisialisasi, program Python dapat memodifikasi file `sys.path`. Direktori yang berisi skrip yang sedang dijalankan ditempatkan di awal jalur pencarian, di awal standar library path. Ini berarti bahwa skrip di direktori itu akan dimuat alih-alih module dengan nama yang sama di direktori library. Ini adalah kesalahan kecuali penggantian yang dimaksudkan.

### - "Compiled" file Python
Untuk mempercepat pemuatan module, Python menyimpan versi terkompilasi dari setiap modul dalam `__pycache__` direktori dengan nama `module.version.pyc`, di mana versi mengkodekan format file yang dikompilasi; biasanya berisi nomor versi Python. Misalnya, di *CPython rilis 3.3* versi kompilasi dari `spam.py` akan di-cache sebagai `__pycache__/spam.cpython-33.pyc`. Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang berbeda dan versi Python yang berbeda untuk hidup berdampingan.

Python memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah itu kedaluwarsa dan perlu dikompilasi ulang. Ini adalah proses yang sepenuhnya otomatis. Juga, module yang dikompilasi adalah `platform-independen`, sehingga library yang sama dapat dibagi di antara sistem dengan arsitektur yang berbeda.

Python tidak memeriksa cache dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil untuk module yang dimuat langsung dari baris perintah. Kedua, tidak memeriksa cache jika tidak ada modul sumber. Untuk mendukung distribusi `non-sumber` (hanya dikompilasi), modul yang dikompilasi harus berada di direktori sumber, dan tidak boleh ada modul sumber.

Beberapa tips untuk para pengguna :
- Pengguna dapat menggunakan `-O` atau `-OO` mengaktifkan perintah Python untuk mengurangi ukuran modul yang dikompilasi. `-O switch` untuk menghapus pernyataan tegas, sedangkan `-OO` switch untuk menghapus pernyataan tegas dan string `__doc__`. Karena beberapa program mungkin bergantung pada ketersediaannya, Pengguna hanya boleh menggunakan opsi ini jika Anda tahu apa yang Anda lakukan. Modul "Dioptimalkan" memiliki `opt-tag` dan biasanya lebih kecil. Rilis mendatang dapat mengubah efek pengoptimalan.
- Sebuah program tidak berjalan lebih cepat saat dibaca dari file `.pyc` daripada saat dibaca dari file `.py`; satu-satunya hal yang lebih cepat tentang file `.pyc` adalah kecepatan pemuatannya.
- Module `compileall` dapat membuat file `.pyc` untuk semua modul dalam direktori.
- Ada lebih detail tentang proses ini, termasuk diagram alir keputusan, di `PEP 3147`.

## 2. Modules Standar
Python hadir dengan library of standard modules, yang dijelaskan dalam dokumen terpisah, Python Library Reference (“Referensi Pustaka”). Beberapa module dibangun ke dalam interpreter; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Kumpulan module tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. Misalnya, `winreg` module hanya disediakan pada sistem Windows. Satu modul tertentu patut mendapat perhatian: `sys`, yang dibangun ke dalam setiap interpreter Python. Variabel `sys.ps1` dan `sys.ps2` ditentukan string yang digunakan sebagai prompt primer dan sekunder:

```python
# Penggunaan variabel sys.ps1 dan sys.ps2
>>> import sys

# variabel sys.ps1
>>> sys.ps1
'>>> '

# variabel sys.ps2
>>> sys.ps2
'... '

>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

Kedua variabel tersebut hanya ditentukan jika interpreter dalam mode interaktif. Variabel `sys.path` adalah daftar string yang menentukan jalur pencarian interpreter untuk module. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkungan `PYTHONPATH`, atau dari default bawaan jika *PYTHONPATH* tidak diatur. Pengguna dapat memodifikasinya menggunakan operasi daftar standar:

```python
# Penggunaaan PYTHONPATH
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

## 3. Fungsi dir()
Fungsi bawaan `dir()` digunakan untuk mengetahui nama mana yang didefinisikan oleh module. Ini mengembalikan daftar string yang diurutkan, seperti berikut ini :
```python
# Penggunaan function dir()
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```
Tanpa argumen, buat `dir()` daftar nama yang telah  ditetapkan saat pada module `fibo.py`. Perhatikan bahwa ini mencantumkan semua jenis nama: variabel, modul, fungsi, dll. Sehingga yang ditampilkan seperti berikut ini :
```python
# Function dir() yang telah ditetapkan oleh Pengguna
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
 ```

Function `dir()` tidak mencantumkan nama fungsi dan variabel bawaan. Jika Pengguna ingin daftarnya, mereka didefinisikan dalam module standar `builtins` :
```python
# Penggunaan perintah builtins
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

## 4. Package
`Package` adalah cara menyusun namespace module Python dengan menggunakan *"dotted modules names"*. Misalnya, nama modul `A`.`B` menunjuk sebuah submodul yang dinamai `B` dalam sebuah paket bernama `A`. Sama seperti penggunaan module yang menyelamatkan pembuat modul yang berbeda dari keharusan khawatir tentang nama variabel global satu sama lain, penggunaan nama modul bertitik menyelamatkan penulis package multi-modul seperti `NumPy` atau `Pillow` dari keharusan khawatir tentang nama module masing-masing.

Misalkan Pengguna ingin merancang kumpulan module ("package") untuk penanganan file suara dan data suara yang seragam. Ada banyak format file suara yang berbeda (biasanya dikenali dari ekstensinya, misalnya: .*wav*, .*aiff*, .I), jadi Pengguna mungkin perlu membuat dan memelihara koleksi module yang terus bertambah untuk konversi antara berbagai format file. Ada juga banyak operasi berbeda yang mungkin ingin Pengguna lakukan pada data suara (seperti mencampur, menambahkan gema, menerapkan fungsi equalizer, membuat efek stereo buatan), jadi selain itu Pengguna akan menulis aliran module yang tidak pernah berakhir untuk dilakukan operasi ini. 

Berikut adalah kemungkinan struktur untuk Package (dinyatakan dalam bentuk sistem file hierarkis) :
```
# Struktur Package
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Saat mengimport package, Python mencari melalui direktori untuk mencari `sys.path` subdirektori package. File `__init__.py` diperlukan untuk membuat direktori memperlakukan Python yang berisi file sebagai paket. Ini mencegah direktori dengan nama umum, seperti string, secara tidak sengaja menyembunyikan module valid yang muncul kemudian di jalur pencarian modul. Dalam kasus yang paling sederhana, hanya `__init__.py` dapat berupa file kosong, tetapi juga dapat mengeksekusi kode inisialisasi untuk paket atau mengatur `__all__variabel`, yang kemudian dijelaskan.

Berikut adalah contoh penggunaan `package` yang mengimport sebuah ekstensi suara :
```python
# Pengguna package dapat mengimport module individual dari package
import sound.effects.echo
# Ini memuat submodule sound.effects.echo. Itu harus dirujuk dengan nama lengkapnya
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# Cara alternatif untuk mengimpor submodule adalah :
from sound.effects import echo
# Ini memuat submodule echo, dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan.
echo.echofilter(input, output, delay=0.7, atten=4)

# Namun variasi lain adalah mengimpor fungsi atau variabel yang diinginkan secara langsung :
from sound.effects.echo import echofilter
# Ini memuat submodule echo, tetapi ini membuat fungsinya echofilter()tersedia secara langsung.
echofilter(input, output, delay=0.7, atten=4)
```

Perhatikan bahwa saat menggunakan `from package import item`, item dapat berupa packages submodul (atau subpaket), atau nama lain yang ditentukan dalam package, seperti fungsi, kelas, atau variabel. Pernyataan `import` menguji apakah item didefinisikan dalam package; jika tidak, ia menganggapnya sebagai module dan mencoba memuatnya. Jika gagal menemukannya, `ImportError` pengecualian dimunculkan.

Sebaliknya, saat menggunakan sintaks seperti `import item.subitem.subsubitem`, setiap item kecuali yang terakhir harus berupa package; item terakhir dapat berupa module atau package tetapi tidak dapat berupa kelas atau fungsi atau variabel yang ditentukan dalam item sebelumnya.

### - Importing * From a Package
Apa yang terjadi ketika Pengguna menulis `from sound.effects import *`. Idealnya, orang akan berharap bahwa ini entah bagaimana keluar ke file sistem, menemukan submodul mana yang ada dalam package, dan mengimport semuanya. Ini bisa memakan waktu lama dan mengimport sub-modul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika sub-modul diimport secara eksplisit.

Satu-satunya solusi adalah bagi pembuat package untuk memberikan indeks eksplisit dari package tersebut. Pernyataan `import` menggunakan konvensi berikut: jika kode package `__init__.py` mendefinisikan daftar bernama `__all__`, itu dianggap sebagai daftar nama modul yang harus diimport ketika ditemui. Terserah pembuat package untuk tetap memperbarui daftar ini ketika versi baru dari paket dirilis. Pembuat paket juga dapat memutuskan untuk tidak mendukungnya, jika mereka tidak melihat kegunaan untuk mengimport * dari package mereka. Misalnya, file `sound/effects/__init__.py` dapat berisi kode berikut : `__all__ = ["echo", "surround", "reverse"]`. Ini berarti bahwa akan mengimpor tiga submodul yang bernama dari package `.from sound.effects import *sound`.

Jika `__all__` tidak didefinisikan, pernyataan `from sound.effects import *` tidak mengimpor semua submodul dari package `sound.effects` ke namespace saat ini; itu hanya memastikan bahwa package telah diimpor (mungkin menjalankan kode inisialisasi apa pun di `__init__.py`) dan kemudian mengimpor nama apa pun yang ditentukan dalam package. Ini termasuk nama apa pun yang ditentukan (dan submodul yang dimuat secara eksplisit) oleh `__init__.py`. Ini juga mencakup setiap submodul dari paket yang secara eksplisit dimuat oleh pernyataan `import` sebelumnya.

```python
# Penggunaan Importing * from a package
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

Meskipun module tertentu dirancang untuk mengekspor hanya nama yang mengikuti pola tertentu saat pengguna menggunakan `import *`, itu masih dianggap sebagai praktik buruk dalam kode produksi. Ingat, tidak ada salahnya menggunakan `from package import specific_submodule`! Sebenarnya, ini adalah notasi yang disarankan kecuali modul pengimpor perlu menggunakan submodul dengan nama yang sama dari package yang berbeda.

### - Intra-package References
Ketika package disusun menjadi subpaket (seperti package `sound` dalam contoh), Pengguna dapat menggunakan import absolut untuk merujuk ke submodul siblings package. Misalnya, jika module `sound.filters.vocoder` perlu menggunakan *echo* module dalam package `sound.effects`, itu dapat menggunakan `.from sound.effects import echo`.

Pengguna juga dapat menulis `relative import`, bersama `from module import name` dengan bentuk pernyataan import. Import ini menggunakan titik awal untuk menunjukkan paket saat ini dan induk yang terlibat dalam relative import. Dari `surround` module misalnya, pengguna dapat menggunakan:

```python
# Penggunaan Intra-package References
from . import echo
from .. import formats
from ..filters import equalizer
```

Perhatikan bahwa `relative import` didasarkan pada nama module saat ini. Karena nama moduel utama selalu `"__main__"`, module yang dimaksudkan untuk digunakan sebagai module utama aplikasi Python harus selalu menggunakan impor absolut.

### - Packages in Multiple Directories
`Package` mendukung satu atribut khusus, `__path__`. Ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan kode package `__init__.py` sebelum file itu dieksekusi. Variabel ini dapat dimodifikasi; hal itu akan memengaruhi pencarian module dan subpaket di masa mendatang yang terdapat dalam package. Meskipun fitur ini tidak sering diperlukan, fitur ini dapat digunakan untuk memperluas kumpulan module yang ditemukan dalam sebuah package.