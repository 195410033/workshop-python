# BAB 1 : Pengenalan Python

`Python` adalah Bahasa pemrograman komputer serta piranti penerjemah ( **Interpreter** ) untuk menjalankan / mengeksekusi source code yang dibuat menggunakan Bahasa pemrograman Python. Bahasa pemrograman Python dibuat pertama kali pada tahun 1980-an oleh `Guido Van Rossum` dan saat ini dikembangkan oleh komunitas di bawah kendali `PSF` ( **Python Software Foundation** ). Python dibuat dengan cara yang relatif intuitif untuk ditulis dan dipahami. Dengan demikian, Python merupakan bahasa coding yang ideal bagi pengguna yang menginginkan perkembangan yang pesat.

Python merupakan Bahasa pemrograman tingkat tinggi dan memiliki keistimewaan yang membedakannya dengan Bahasa-bahasa pemrograman lain yaitu :
- Sudah tersedia di sistem operasi **Windows**, **macOS**, dan **Unix**. Karena bersifat platform independent membuat program yang dibuat menggunakan Python dapat berjalan pada sistem operasi manapun selama di dalamnya terdapat **Interpreter Python**;
- Membantu penggunanya menyelesaikan pekerjaan dengan lebih cepat;
- Mudah digunakan, tetapi menggunakan bahasa yang kompleks. Namun menawarkan lebih banyak struktur dan dukungan untuk programnya dibandingkan yang ditawarkan oleh script **shell** atau file **batch**;
- Lebih banyak pemeriksaan kesalahan daripada bahasa pemrograman **C**;
- Dapat menghemat banyak waktu selama pengembangan program, karena tidak memerlukan kompilasi dan penautan.

Bahasa pemrograman Python juga memungkinkan program yang ditulis dengan ringkas dan mudah dibaca. Biasanya program yang ditulis Python jauh lebih pendek daripada Program **C**, **C++**, atau **Java**, karena beberapa alasan :
- Tipe data tingkat tinggi yang memungkinkan penggunanya untuk mengekspresikan operasi kompleks dalam satu pernyataan;
- Pengelompokan pernyataan dilakukan dengan indentasi alih-alih tanda kurung awal dan akhir;
- Tidak diperlukan deklarasi variabel atau argumen.

# BAB 2 : Interpreter Python

Python merupakan bahasa `Interpreter`, Interpreter di sini maksudnya Python akan memproses kode program secara baris perbaris, berbeda dengan compiler. Jadi metode yang dipakai sama dengan bahasa PHP, PERL dan lain-lain. Python juga merupakan `High Programming Language` atau bahasa tingkat tinggi, artinya instruksi-intruksi yang ada di dalamnya sudah mendekati bahasa manusia.

Interpreter Python biasanya diinstall di direktori `/usr/local/bin/python3.10` pada sistem operasi yang tersedia. Karena pilihan direktori Interpreter Python tersebut merupakan pilihan instalasi. Pada sistem operasi Windows dimana pengguna telah menginstall Python dari `Microsoft Store`, perintah untuk menjalankan Python yang tersedia akan menampilkan Python sesuai versi yang telah diinstall contohnya `python3.10`.

Salah satu fitur yang digunakan Interpreter Python adalah penyuntingan baris penerjemah yang mencakup penyuntingan `interactive`, pergantian riwayat dan penyelesaian kode pada sistem yang mendukung pustaka `GNU Readline`. Pemeriksaan tercepat untuk melihat apakah pengeditan baris perintah didukung atau tidak adalah dengan cara mengetik ke prompt Python pengguna. Jika berbunyi bip, maka pengguna memiliki pengeditan baris perintah untuk pengenalan `keys`. Jika tidak ada yang terjadi, maka pengeditan baris perintah tidak tersedia. Pengguna hanya dapat menggunakan backspace untuk menghapus karakter dari baris tersebut.

Interpreter beroperasi seperti `shell Unix`: ketika dipanggil dengan input standar yang terhubung ke perangkat `tty`, ia membaca dan mengeksekusi perintah secara interaktif; ketika dipanggil dengan argumen nama file atau dengan file sebagai input standar, ia membaca dan mengeksekusi script dari file tersebut.

Ketika perintah dibaca dari `tty`, interpreter dikatakan dalam `interactive mode`. Dalam mode ini menampilkan `primary prompt`, biasanya tiga tanda lebih besar dari `>>>`. Sedangkan untuk baris lanjutan ia menampilkan `secondary prompt`, biasanya tiga tanda tiga titik `...`. 

```
$ python3.10
Python 3.10 (default, June 4 2019, 09:25:04)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Kemudian secara default, file sumber Python diperlakukan sebagai pengkodean dalam bentuk `UTF-8`. Dalam pengkodean itu, karakter sebagian besar bahasa di dunia dapat digunakan secara bersamaan dalam literal string, pengidentifikasi, dan komentar. Meskipun pustaka standar hanya menggunakan karakter `ASCII` untuk pengidentifikasian. Untuk menampilkan semua karakter ini dengan benar, programmer harus mengenali bahwa file tersebut adalah `UTF-8`, dan harus menggunakan font yang mendukung semua karakter dalam file tersebut.

# BAB 3 : Pengantar Informal Python

Input dan Output dibedakan dengan ada atau tidaknya prompt ( `>>>` dan `…` ): Pengguna harus mengetikkan semuanya setelah prompt, ketika prompt muncul; baris yang tidak dimulai dengan prompt adalah output dari interpreter. Perhatikan bahwa perintah `secondary prompt` pada baris dengan sendirinya dalam script berarti pengguna harus mengetikkan baris kosong; ini digunakan untuk mengakhiri perintah multi-baris.

Begitu Banyak contoh dalam modul ini, bahkan yang dimasukkan pada `prompt interactive`, termasuk komentar. Komentar dalam Python dimulai dengan karakter hash ( `#` ), dan diperpanjang hingga akhir baris fisik. Sebuah komentar mungkin muncul di awal baris atau setelah spasi atau kode, tetapi tidak dalam `literal string`. Karakter hash dalam string literal hanyalah karakter hash. Karena komentar adalah untuk memperjelas kode dan tidak ditafsirkan oleh Python.

## Menggunakan Python Sebagai Calculator

### 1. Number

`Number` adalah tipe data Python yang menyimpan nilai numerik. Number adalah tipe data yang tidak berubah. Ini berarti, mengubah nilai dari sejumlah tipe data akan menghasilkan objek yang baru dialokasikan. Pengguna dapat mengetikkan ekspresi pada prompt dan itu akan menulis nilainya. Terdapat beberapa sintaks ekspresi yaitu operator ` + `, ` - `, ` * ` dan ` / ` yang bekerja seperti kebanyakan bahasa lainnya ( misalnya `Pascal` atau `C` ); sedangkan tanda kurung  ( `(   )` ) dapat digunakan untuk pengelompokan.

```
>>> 2 + 2
4

>>> 50 - 5*6
20

>>> (50 - 5*6) / 4
5.0

>>> 8 / 5
1.6
```

Bilangan bulat ( misalnya **2, 4, dan 20** ) memiliki tipedata `int`, bilangan dengan bagian pecahan ( misalnya **5.0, dan 1.6** ) memiliki tipedata `float`. Operator `/` selalu menampilkan nilai float. Untuk melakukan pembagian dan mendapatkan hasil bilangan bulat (membuang hasil pecahan apa pun), pengguna dapat menggunakan operator `//`; sedangkan untuk menghitung sisanya, Pengguna dapat menggunakan operator `%`.

Selain `int` dan `float`, Python juga mendukung jenis angka lain, seperti `Decimal` dan `Fraction`. Python juga memiliki dukungan bawaan untuk bilangan kompleks , dan menggunakan akhiran `j` or `J` untuk menunjukkan bagian imajiner ( misalnya **3+5j** ).

### 2. String

Selain `Number`, Python juga dapat menggunakan `string`, yang dapat diekspresikan dalam beberapa cara. Pengguna dapat diapit oleh tanda kutip tunggal ( `'...'` ) atau tanda kutip ganda ( `"..."` ) dengan hasil yang sama.

```
>>> 'spam eggs'  # single quotes
'spam eggs'

>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"

>>> "doesn't"  # ...or use double quotes instead
"doesn't"
```

Dalam `interpreter interactive`, string keluaran diapit oleh tanda kutip dan karakter khusus yang diloloskan dengan garis miring terbalik ( `\` ). Meskipun ini terkadang terlihat berbeda dari input ( tanda kutip terlampir dapat berubah ), kedua string tersebut setara. String diapit dalam tanda kutip ganda jika string berisi tanda kutip tunggal dan tidak ada tanda kutip ganda, selain itu diapit dalam tanda kutip tunggal. Fungsi `print()` berguna untuk menghasilkan keluaran yang lebih mudah dibaca, dengan menghilangkan tanda kutip terlampir dan dengan mencetak karakter khusus.

`String` dapat diindeks, dengan karakter pertama memiliki `indeks` **0**. Tidak ada tipe karakter terpisah, karakter hanyalah string ukuran satu. Indeks juga bisa berupa angka negatif, untuk mulai menghitung dari kanan. Selain pengindeksan, pengirisan juga didukung. Sementara pengindeksan digunakan untuk mendapatkan karakter individu, `slicing` memungkinkan pengguna untuk mendapatkan `substring`. Salah satu cara untuk mengingat cara kerja irisan adalah dengan menganggap indeks sebagai penunjuk antar karakter, dengan tepi kiri karakter pertama bernomor **0**. Kemudian tepi kanan karakter terakhir dari string **n** karakter memiliki indeks **n**.

### 3. Lists

`Python` mengetahui sejumlah tipe data gabungan, yang digunakan untuk mengelompokkan nilai-nilai lain. Biasanya sering disebut `list`, yang dapat ditulis sebagai daftar nilai ( **item** ) yang dipisahkan koma di antara tanda kurung siku. Daftar mungkin berisi item dari jenis yang berbeda, tetapi biasanya semua item memiliki jenis yang sama. Untuk mengakses nilai dalam list Python, gunakan tanda kurung siku untuk mengiris beserta indeks atau indeks untuk mendapatkan nilai yang tersedia pada indeks tersebut.

```
>>> list1 = ['kimia', 'fisika', 1993, 2017]

>>> list2 = [1, 2, 3, 4, 5 ]

>>> list3 = ["a", "b", "c", "d"]
```

Pengguna dapat memperbarui satu atau beberapa nilai di dalam list dengan memberikan potongan di sisi kiri operator **penugasan**, dan pengguna dapat menambahkan nilai ke dalam list dengan metode `append ()`.

Untuk menghapus nilai di dalam list Python, Pengguna dapat menggunakan salah satu pernyataan `del` jika pengguna tahu persis elemen yang ingin dihapus. Pengguna dapat menggunakan metode `remove()` jika tidak tahu persis item mana yang akan dihapus.

## Langkah Pertama Menuju Pemrograman

Tentu saja, pengguna dapat menggunakan Python untuk tugas yang lebih rumit daripada menambahkan dua element secara bersamaan. Misalnya, pengguna dapat menulis sub-urutan awal dari deret Fibonacci sebagai berikut:

```
>>> # Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
```

**Penjelasan :**

- Baris pertama berisi beberapa `assigment` : variabel a dan b secara bersamaan mendapatkan nilai baru 0 dan 1. Pada baris terakhir ini digunakan lagi, menunjukkan bahwa ekspresi di sisi kanan semuanya dievaluasi terlebih dahulu sebelum penugasan dilakukan . Ekspresi sisi kanan dievaluasi dari kiri ke kanan.

- Perulangan `while` dijalankan selama kondisi bernilai benar. Dalam Python, seperti di C, semua nilai integer bukan nol adalah benar; nol salah. Kondisi juga dapat berupa string atau nilai daftar, bahkan urutan apa pun; apa pun dengan panjang bukan nol adalah benar, urutan kosong adalah salah.

- Statement loop diindented : `indented `adalah cara Python mengelompokkan pernyataan. Pada `prompt interactive`, pengguna harus mengetikkan tab atau spasi untuk setiap baris indentasi. Dalam praktiknya penngguna akan menyiapkan input yang lebih rumit untuk Python dengan editor teks; semua editor teks yang layak memiliki fasilitas auto-indent. Ketika pernyataan majemuk dimasukkan secara `interactive`, itu harus diikuti oleh baris kosong untuk menunjukkan penyelesaian ( karena parser tidak dapat menebak kapan pengguna telah mengetik baris terakhir ). Perhatikan bahwa setiap baris dalam blok dasar harus diindentasi dengan jumlah yang sama.

- Fungsi `print()` menulis nilai argumen yang diberikan. Ini berbeda dari hanya menulis ekspresi yang ingin pengguna tulis dalam cara menangani banyak argumen, jumlah `floating point`, dan string. `String` dicetak tanpa tanda kutip, dan spasi disisipkan di antara item, sehingga pengguna dapat memformat sesuatu dengan baik. Argumen kata kunci `end` dapat digunakan untuk menghindari baris baru setelah output, atau mengakhiri output dengan string yang berbeda.