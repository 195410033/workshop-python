# Scikit-learn

`Scikit-Learn` merupakan library Machine Learning open source berbasis Python yang bisa digunakan dalam Data Science. Kelebihan Scikit-Learn adalah penggunaan API yang mudah serta kecepatannya saat melakukan tolok ukur yang berbeda dalam dataset. Sklearn kompatibel dengan `NumPy` dan `SciPy`. Ini artinya kamu akan dapat beroperasi dengan library-library yang berbeda untuk Python dengan mudah.

Scikit-Learn memberikan sejumlah fitur untuk keperluan Data Science seperti algoritma Regresi, clustering, algoritma Naive Bayes, algoritma Decision Tree, parameter tuning, data preprocessing tool, export/import model, Machine learning pipeline dan algoritma klasifikasi termasuk gradien, K-means, mesin dukungan vektor, DBSCAN, dan juga mampu beroperasi dengan SciPy dan NumPy.

## Machine learning: the problem setting
Secara umum, masalah pembelajaran mempertimbangkan satu set sampel `n` data dan kemudian mencoba memprediksi sifat data yang tidak diketahui. Jika setiap sampel lebih dari satu angka dan instance, maka sebuah **multi-dimensional entry** (alias data `multivariat`) dikatakan memiliki beberapa atribut atau fitur .

Masalah belajar terbagi dalam beberapa kategori:

- `Supervised Learning`, di mana data dilengkapi dengan atribut tambahan yang ingin diprediksi. Masalah ini dapat berupa:

    - `klasifikasi` : bisa diartikan sebagai proses mengategorisasikan suatu hal menjadi beberapa kelompok berdasarkan persamaan dan perbedaannya. Contoh masalah klasifikasi adalah pengenalan digit tulisan tangan, di mana tujuannya adalah untuk menetapkan setiap vektor input ke salah satu dari sejumlah kategori diskrit yang terbatas. 

    - `regresi` : jika keluaran yang diinginkan terdiri dari satu atau lebih variabel continous, maka task tersebut disebut regresi. Contoh masalah regresi adalah prediksi panjang ikan salmon sebagai fungsi dari umur dan beratnya.

- `Unsupervised Learning`, di mana data pelatihan terdiri dari satu set vektor input `x` tanpa nilai target yang sesuai. Tujuan dalam masalah tersebut mungkin untuk menemukan kelompok dalam data, yang disebut `clustering`, atau untuk menentukan distribusi data dalam ruang input, yang dikenal sebagai `density estimation`, atau untuk memproyeksikan data dari sebuah high-dimensional ruang ke dua atau tiga dimensi untuk tujuan `visualization`.

## Loading an example dataset
Berikut ini, memulai interpreter Python dari Command Prompt dan kemudian memuat dataset `iris` dan dataset `digits`. Command prompt yang digunakan akan menampilkan `>` yang menunjukkan prompt, sedangkan `>>>` menunjukkan prompt interpreter Python:
```python
> py
# Python 3.11.0b1 (main, May  7 2022, 22:58:47) [MSC v.1931 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.

# mengimport library
>>> from sklearn import datasets

# memuat dataset iris dan digits
>>> iris = datasets.load_iris()
>>> digits = datasets.load_digits()
```

`Dataset` adalah sebuah objek seperti kamus yang menyimpan semua data dan beberapa metadata tentang data tersebut. Data ini disimpan dalam `.data` member, yang merupakan sebuah `n_samples`, `n_features` array. Dalam kasus masalah yang diawasi, satu atau lebih variabel respons disimpan di `.target` member.

Misalnya, dalam kasus kumpulan data digits, `digits.data` memberikan akses ke fitur yang dapat digunakan untuk mengklasifikasikan sampel digits:
```python
>>> print(digits.data)
# output:
[[ 0.   0.   5. ...   0.   0.   0.]
 [ 0.   0.   0. ...  10.   0.   0.]
 [ 0.   0.   0. ...  16.   9.   0.]
 ...
 [ 0.   0.   1. ...   6.   0.   0.]
 [ 0.   0.   2. ...  12.   0.   0.]
 [ 0.   0.  10. ...  12.   1.   0.]]
```

dan `digits.target` memberikan kebenaran dasar untuk kumpulan data digit, yaitu angka yang sesuai dengan setiap gambar digit yang ada :
```python
>>> digits.targer
# output:
array([0, 1, 2, ..., 8, 9, 8])
```

### Shape of the data arrays
Data selalu berupa 2D array, dalam bentuk (n_samples, n_features), meskipun data asli mungkin memiliki bentuk yang berbeda. Dalam hal digit, setiap sampel asli adalah gambar bentuk (8, 8) dan dapat diakses menggunakan:
```python
>>> digits.images[0]
# output:
array([[  0.,   0.,   5.,  13.,   9.,   1.,   0.,   0.],
       [  0.,   0.,  13.,  15.,  10.,  15.,   5.,   0.],
       [  0.,   3.,  15.,   2.,   0.,  11.,   8.,   0.],
       [  0.,   4.,  12.,   0.,   0.,   8.,   8.,   0.],
       [  0.,   5.,   8.,   0.,   0.,   9.,   8.,   0.],
       [  0.,   4.,  11.,   0.,   1.,  12.,   7.,   0.],
       [  0.,   2.,  14.,   5.,  10.,  12.,   0.,   0.],
       [  0.,   0.,   6.,  13.,  10.,   0.,   0.,   0.]])
```

## Learning and predicting
Dalam kasus dataset digits, tugasnya adalah memprediksi, dengan diberikan gambar, dimana digit yang diwakilinya. Kemudian diberikan sampel dari masing-masing 10 kelas yang mungkin (angka nol sampai sembilan) yang disesuaikan dengan estimator untuk dapat memprediksi kelas yang termasuk dalam sampel tak terlihat.

Dalam `scikit-learn`, estimator untuk klasifikasi adalah objek Python yang mengimplementasikan metode `fit(X, y)` dan `predict(T)`.

Contoh `estimator` adalah kelas `sklearn.svm.SVC` yang mengimplementasikan `support vector classification`. Konstruktor estimator mengambil parameter model sebagai argumen. Untuk saat ini akan mempertimbangkan estimator sebagai black box:
```python
>>> from sklearn import svm
>>> clf = svm.SVC(gamma=0.001, C=100.)
```

`clf` (untuk classifier) estimator menginisiasi pertama-tama dipasang ke model; yaitu, ia harus belajar dari model. Ini dilakukan dengan meneruskan set pelatihan ke method `fit`. Untuk set pelatihan akan menggunakan semua gambar dari dataset, kecuali untuk gambar terakhir, yang akan disimpan untuk prediksi. Kemudian memilih set pelatihan dengan `[:-1]` sintaks Python, yang menghasilkan array baru yang berisi semua kecuali item terakhir dari `digits.data`:
```python
>>> clf.fit(digits.data[:-1], digits.target[:-1])
# output:
SVC(C=100.0, gamma=0.001)
```

Sekarang dapat memprediksi nilai baru. Dalam hal ini akan memprediksi menggunakan gambar terakhir dari `digits.data`. Dengan memprediksi akan menentukan gambar dari set pelatihan yang paling cocok dengan gambar terakhir.
```python
>>> clf.predict(digits.data[-1:])
# output:
array([8])
```

## Conventions
### Type casting
Akan ditentukan yang masukannya akan diberikan ke `float64`:
```python
# mengimport library
>>> import numpy as np
>>> from sklearn import kernel_approximation

>>> rng = np.random.RandomState(0)
>>> X = rng.rand(10, 2000)
>>> X = np.array(X, dtype='float32')
>>> X.dtype
# output float32
dtype('float32')

>>> transformer = kernel_approximation.RBFSampler()
>>> X_new = transformer.fit_transform(X)
>>> X_new.dtype
# output float64
dtype('float64')
```

Dalam contoh ini, `X` adalah `float32` yang dilemparkan ke `float64` oleh `fit_transform(X)`.

Target regresi diberikan ke `float64` dan target klasifikasi akan dipertahankan:
```python
# mengimport library
>>> from sklearn import datasets
>>> from sklearn.svm import SVC

>>> iris = datasets.load_iris()
>>> clf = SVC()
>>> clf.fit(iris.data, iris.target)
# output:
SVC()

>>> list(clf.predict(iris.data[:3]))
# output:
[0, 0, 0]

>>> clf.fit(iris.data, iris.target_names[iris.target])
# output:
SVC()

>>> list(clf.predict(iris.data[:3]))
# output:
['setosa', 'setosa', 'setosa']
```

Di sini, yang pertama `predict()` mengembalikan array integer, karena `iris.target` (array integer) digunakan dalam `fit`. Yang kedua `predict()` mengembalikan array string, karena `iris.target_names` untuk pemasangan.

### Refitting and updating parameters
Hyper-parameter dari estimator dapat diperbarui setelah dibangun melalui method `set_params()`. Kemudian memanggil `fit()` lebih dari sekali akan menimpa apa yang dipelajari oleh sebelum `fit()`:
```python
# mengimport library
>>> import numpy as np
>>> from sklearn.datasets import load_iris
>>> from sklearn.svm import SVC

>>> X, y = load_iris(return_X_y=True)

>>> clf = SVC()
>>> clf.set_params(kernel='linear').fit(X, y)
# output:
SVC(kernel='linear')
>>> clf.predict(X[:5])
# output:
array([0, 0, 0, 0, 0])

>>> clf.set_params(kernel='rbf').fit(X, y)
# output:
SVC()
>>> clf.predict(X[:5])
# output:
array([0, 0, 0, 0, 0])
```

Di sini, default kernel `rbf` pertama kali diubah menjadi `linear` via `SVC.set_params()` setelah estimator dibuat, dan diubah kembali ke rbf untuk menyesuaikan estimator dan membuat prediksi kedua.

### Multiclass vs multilabel fitting
Saat menggunakan `multiclass classifiers`, tugas learning dan prediksi yang dilakukan bergantung pada format data target yang sesuai:
```python
# mengimport library
>>> from sklearn.svm import SVC
>>> from sklearn.multiclass import OneVsRestClassifier
>>> from sklearn.preprocessing import LabelBinarizer

>>> X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
>>> y = [0, 0, 1, 1, 2]

>>> classif = OneVsRestClassifier(estimator=SVC(random_state=0))
>>> classif.fit(X, y).predict(X)
# output:
array([0, 0, 1, 1, 2])
```

Dalam kasus di atas, classifier cocok pada array 1d dari `multiclass labels` dan method `predict()` oleh karena itu metode ini menyediakan prediksi mmulticlass yang sesuai. Dimungkinkan juga untuk menyesuaikan pada array 2d dari binary label indicators:
```python
>>> y = LabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
# output:
array([[1, 0, 0],
       [1, 0, 0],
       [0, 1, 0],
       [0, 0, 0],
       [0, 0, 0]])
```

Di sini, classifier `fit()` pada representasi label biner 2d dari `y`, menggunakan `LabelBinarizer`. Dalam hal ini `predict()` mengembalikan array 2d yang mewakili prediksi multilabel yang sesuai.

Perhatikan bahwa contoh keempat dan kelima mengembalikan semua nol, menunjukkan bahwa mereka tidak cocok dengan tiga label `fit`. Dengan keluaran multilabel, sebuah instance juga dapat diberi beberapa label:
```python
# mengimport library
>>> from sklearn.preprocessing import MultiLabelBinarizer

>>> y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
>>> y = MultiLabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
### output:
array([[1, 1, 0, 0, 0],
       [1, 0, 1, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0],
       [1, 0, 1, 0, 0]])
```

Dalam hal ini, classifier cocok pada instance yang masing-masing diberi beberapa label. `MultiLabelBinarizer` digunakan untuk binerisasi array 2d dari multilabel ke `fit`. Akibatnya, `predict()` kembalikan array 2d dengan beberapa label yang diprediksi untuk setiap instance.