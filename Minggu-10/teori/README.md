# Akses ke Basis Data
`Database` adalah sekumpulan data yang dikelola berdasarkan ketentuan tertentu yang saling berkaitan sehingga memudahkan dalam pengelolaannya. Database memiliki peran penting dalam perangkat untuk mengumpulkan informasi, data, atau file secara terintegrasi. Database membuat penyimpanan dan pengelolaan data menjadi lebih efisien. 

Fungsi database adalah untuk menghindari data ganda yang tersimpan. Suatu database management system (**DBMS**) dapat diatur supaya bisa mengenali duplikasi data ketika diinput. Namun selain untuk menghindari data ganda, database memiliki fungsi lainnya, antara lain: 
- Mengelompokan data dan informasi. 
- Memudahkan dalam identifikasi data.
- Memudahkan proses akses, menyimpan, pembaharuan, dan penghapusan data. 
- Menjadi alternatif terkait masalah penyimpanan ruang dalam suatu aplikasi. 
- Menjaga kualitas data yang diakses sesuai input. 
- Menunjang kinerja aplikasi yang memerlukan penyimpanan data. 

Selain fungsi di atas, database bermanfaat untuk meminimalisasi redundansi data atau munculnya banyak data dalam file yang berbeda. Database dapat menunjang keamanan data. Hal tersebut lantaran sistem yang telah disusun secara aman melalui instrumen password sehingga data hanya bisa diakses oleh pihak yang diizinkan.

**Standar Interface Python** untuk database adalah `Python DB-API`. Kebanyakan Interface database Python mematuhi standar ini. `API` ini telah didefinisikan untuk mendorong kesamaan antara modul Python yang digunakan untuk mengakses database. Ketika melakukan ini, dapat mencapai konsistensi yang mengarah ke modul yang lebih mudah dipahami, kode yang umumnya lebih portabel di seluruh basis data, dan jangkauan konektivitas basis data yang lebih luas dari Python.

**Google Cloud Spanner**, layanan basis data relasional yang dikelola sepenuhnya berjalan di **Google Compute Engine (GCE)** yang dirilis pada Februari 2017, memiliki skalabilitas basis data NoSQL sambil mempertahankan kompatibilitas SQL, skema relasional, transaksi ACID, dan konsistensi eksternal yang kuat. `Spanner` adalah basis data relasional yang terbuang, terdistribusi global, dan direplikasi yang menggunakan algoritma **Paxos** untuk mencapai konsensus di antara simpul-simpulnya.

Seperti **Cloud Spanner**, `CockroachDB` adalah database SQL terdistribusi yang dibangun di atas penyimpanan nilai kunci yang transaksional dan konsisten, dalam kasus CockroachDB tentang **RocksDB**. Tujuan desain utama CockroachDB adalah dukungan untuk transaksi **ACID**, skalabilitas horizontal, dan (sebagian besar dari semua) kemampuan bertahan hidup.

`CockroachDB` adalah open source dan database SQL cloud-asli yang dikembangkan oleh **CockroachLabs**. Ini adalah database SQL terdistribusi yang dibangun di atas transaksi dan penyimpanan nilai kunci. `CockroachDB` adalah database **SQL scalable** yang telah dibandingkan dengan database **Google Spanner**. Ini didasarkan pada utas protokol **PostgreSQL** dan produksi siap.

## 1. Akses ke Basis Data CockroachDB menggunakan psycopg2
`Psycopg` adalah adaptor **PostgreSQL** paling populer untuk bahasa pemrograman Python. Intinya adalah implementasi lengkap dari spesifikasi `Python DB API 2.0`. Beberapa ekstensi memungkinkan akses ke banyak fitur yang ditawarkan oleh **PostgreSQL**. `Psycopg` dirilis di bawah ketentuan **GNU Lesser General Public License**, memungkinkan penggunaan dari perangkat lunak bebas dan berpemilik.

Berikut ini cara mengakses ke Database **CockroachDB** menggunakan **psycopg2** :

### Buat Cluster Gratis
1. Jika Anda belum mempunyai akun, [daftar akun CockroachDB Cloud terlebih dahulu](https://cockroachlabs.cloud/signup?referralId=docs_python_psycopg2&_ga=2.118502793.1016630131.1652537862-608809893.1652537862).
2. [Masuk](https://cockroachlabs.cloud/?_ga=2.93150365.1016630131.1652537862-608809893.1652537862) ke akun Cloud CockroachDB Anda.
3. Pada halaman **Clusters**, klik **Create Cluster**.
4. Pada halaman **Create your cluster**, pilih **Serverless**.
    
    Kecuali Anda mengubah anggaran bulanan, cluster ini akan gratis selamanya.
5. Klik **Create cluster**.
    
    Cluster Anda akan dibuat dalam beberapa detik dan dialog **Create SQL user** akan ditampilkan.

### Buat pengguna SQL
Dialog **Create SQL user** memungkinkan Anda membuat pengguna dan kata sandi SQL baru.
1. Masukkan nama pengguna di bidang **SQL user** atau gunakan yang disediakan secara default.
2. Klik **Generate & save password**.
3. Salin kata sandi yang dihasilkan dan simpan di lokasi yang aman.
4. Klik **Next**.

### Dapatkan sertifikat root
Dialog **Connect to cluster** menampilkan informasi tentang cara menghubungkan ke cluster Anda.
1. Pilih **General connection string** dari dropdown **Select option**.
2. Buka terminal baru di komputer lokal Anda, dan jalankan perintah **CA Cert download command** yang disediakan di bagian **Download CA Cert**. Driver client yang digunakan dalam tutorial ini memerlukan sertifikat ini untuk terhubung ke **CockroachDB Cloud**.

### Dapatkan connection string
Buka bagian **General connection string** , lalu salin connection string yang disediakan dan simpan di lokasi yang aman.

**Catatan** : 
String koneksi sudah diisi sebelumnya dengan nama pengguna, kata sandi, nama cluster, dan detail lainnya. Kata sandi Anda, khususnya, hanya akan diberikan sekali. Simpan di tempat yang aman (**Cockroach Labs** merekomendasikan pengelola kata sandi) untuk terhubung ke cluster Anda di masa mendatang. Jika Anda lupa kata sandi, Anda dapat mengatur ulang dengan membuka halaman [SQL Users](https://www.cockroachlabs.com/docs/cockroachcloud/user-authorization).

### Dapatkan sample code
Kloning repo Github kode sampel :
```
$ git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
```
Kode sampel di `example.py` melakukan hal berikut:
- Membuat `accounts table` dan menyisipkan beberapa baris
- Mentransfer dana antara dua akun dalam suatu [transaksi](https://www.cockroachlabs.com/docs/v21.2/transactions)
- Hapus akun dari tabel sebelum keluar sehingga Anda dapat menjalankan kembali `example.py`.

Untuk [menangani kesalahan percobaan ulang transaksi](https://www.cockroachlabs.com/docs/v21.2/error-handling-and-troubleshooting#transaction-retry-errors), kode menggunakan pengulangan percobaan tingkat aplikasi yang, jika terjadi kesalahan, tidur sebelum mencoba transfer dana lagi. Jika menemukan kesalahan coba lagi, ia tidur untuk interval yang lebih lama, menerapkan [backoff eksponensial](https://en.wikipedia.org/wiki/Exponential_backoff).

### Instal driver psycopg2
`psycopg2-binary` adalah satu-satunya dependensi modul pihak ketiga aplikasi sampel.

Untuk menginstal `psycopg2-binary`, jalankan perintah berikut:
```
$ pip install psycopg2-binary
```
Untuk cara lain menginstal `psycopg2`, lihat [official documentation](http://initd.org/psycopg/docs/install.html).

### Jalankan kode
1. Setel `DATABASE_URL` environment variable ke connection string ke cluster CockroachDB Cloud Anda:
    ```
    $ export DATABASE_URL="{connection-string}"
    ```
    Di mana `{connection-string}` string koneksi yang Anda peroleh dari CockroachDB Cloud Console.

    Aplikasi menggunakan connection string yang disimpan ke `DATABASE_URL` environment variable untuk terhubung ke cluster Anda dan mengeksekusi kode.

2. Jalankan kode :
    ```
    $ cd hello-world-python-psycopg2
    ```

    ```
    $ python example.py
    ```
    Output harus menunjukkan saldo akun sebelum dan sesudah transfer dana:
    ```    
    Balances at Sun May 15 08:11:02 2022:
    (1, 1000)
    (2, 250)
    Balances at Sun May 15 08:11:02 2022:
    (1, 900)
    (2, 350)
    ```

## 2. Akses ke Basis Data CockroachDB menggunakan SQLAlchemy
`SQLAlchemy` adalah **toolkit Python SQL** dan **Object Relational Mapper** yang memberi pengembang aplikasi kekuatan penuh dan fleksibilitas SQL. Ini menyediakan rangkaian lengkap pola persistensi tingkat perusahaan yang terkenal, dirancang untuk akses database yang efisien dan berkinerja tinggi, diadaptasi ke dalam bahasa domain yang sederhana dan Pythonic. Tujuan utama `SQLAlchemy` adalah mengubah cara berpikir tentang database dan SQL!.

Berikut ini cara mengakses ke Database **CockroachDB** menggunakan **SQLAlchemy** :
### Dapatkan sample code
Kloning repo Github kode sampel :
```
$ git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
```

Proyek ini memiliki struktur direktori seperti berikut ini :
```
├── README.md
├── dbinit.sql
├── main.py
├── models.py
└── requirements.txt
```

File `requirements.txt` tersebut menyertakan pustaka yang diperlukan untuk terhubung ke **CockroachDB** dengan **SQLAlchemy**, termasuk [sqlalchemy-cockroachdb Python package](https://github.com/cockroachdb/sqlalchemy-cockroachdb), yang menjelaskan beberapa perbedaan antara **CockroachDB** dan **PostgreSQL** :
```
psycopg2-binary
sqlalchemy
sqlalchemy-cockroachdb
```

File `dbinit.sql` menginisialisasi skema database yang digunakan aplikasi :
```sql
CREATE TABLE accounts (
    id UUID PRIMARY KEY,
    balance INT8
);
```

Menggunakan **SQLAlchemy** `models.py` untuk memetakan tabel `Accounts` ke objek Python :
```python
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Account(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    balance = Column(Integer)
```

Menggunakan **SQLAlchemy** `main.py` untuk memetakan metode Python ke operasi SQL :
```python
"""This simple CRUD application performs the following operations sequentially:
    1. Creates 100 new accounts with randomly generated IDs and randomly-computed balance amounts.
    2. Chooses two accounts at random and takes half of the money from the first and deposits it
     into the second.
    3. Chooses five accounts at random and deletes them.
"""

from math import floor
import os
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from models import Account

# The code below inserts new accounts.


def create_accounts(session, num):
    """Create N new accounts with random account IDs and account balances.
    """
    print("Creating new accounts...")
    new_accounts = []
    while num > 0:
        account_id = uuid.uuid4()
        account_balance = floor(random.random()*1_000_000)
        new_accounts.append(Account(id=account_id, balance=account_balance))
        seen_account_ids.append(account_id)
        print(f"Created new account with id {account_id} and balance {account_balance}.")
        num = num - 1
    session.add_all(new_accounts)


def transfer_funds_randomly(session, one, two):
    """Transfer money between two accounts.
    """
    try:
        source = session.query(Account).filter(Account.id == one).one()
    except NoResultFound:
        print("No result was found")
    except MultipleResultsFound:
        print("Multiple results were found")
    dest = session.query(Account).filter(Account.id == two).first()
    print(f"Random account balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")

    amount = floor(source.balance/2)
    print(f"Transferring {amount} from account {one} to account {two}...")

    # Check balance of the first account.
    if source.balance < amount:
        raise ValueError(f"Insufficient funds in account {one}")
    source.balance -= amount
    dest.balance += amount

    print(f"Transfer complete.\nNew balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")


def delete_accounts(session, num):
    """Delete N existing accounts, at random.
    """
    print("Deleting existing accounts...")
    delete_ids = []
    while num > 0:
        delete_id = random.choice(seen_account_ids)
        delete_ids.append(delete_id)
        seen_account_ids.remove(delete_id)
        num = num - 1

    accounts = session.query(Account).filter(Account.id.in_(delete_ids)).all()

    for account in accounts:
        print(f"Deleted account {account.id}.")
        session.delete(account)


if __name__ == '__main__':
    # For cockroach demo:
    # DATABASE_URL=postgresql://demo:<demo_password>@127.0.0.1:26257?sslmode=require
    # For CockroachCloud:
    # DATABASE_URL=postgresql://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>
    db_uri = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_uri)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")

    seen_account_ids = []

    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_accounts(s, 100))

    from_id = random.choice(seen_account_ids)
    to_id = random.choice([id for id in seen_account_ids if id != from_id])

    run_transaction(sessionmaker(bind=engine),
                    lambda s: transfer_funds_randomly(s, from_id, to_id))

    run_transaction(sessionmaker(bind=engine), lambda s: delete_accounts(s, 5))
```

### Install requirements aplikasi
Tutorial ini digunakan [virtualenv](https://virtualenv.pypa.io/) untuk manajemen dependency.
1. Install `virtualenv` :
    ```
    $ pip install virtualenv
    ```

2. Di tingkat atas direktori proyek aplikasi, buat dan aktifkan virtual environment :
    ```
    $ virtualenv env
    ```

    ```
    $ source env/bin/activate
    ```

3. Install module yang diperlukan ke virtual environment :
    ```
    $ pip install -r requirements.txt
    ```

### Inisialisasi database
1. Setel `DATABASE_URL` environment variable ke connection string ke cluster Anda:
    ```
    $ export DATABASE_URL="{connection-string}"
    ```
    Di mana `{connection-string}` string koneksi yang Anda peroleh dari CockroachDB Cloud Console.

2. Untuk menginisialisasi database, gunakan [cockroach sql](https://www.cockroachlabs.com/docs/v21.2/cockroach-sql) perintah untuk mengeksekusi pernyataan SQL dalam file `dbinit.sql`:
    ```
    $ cat dbinit.sql | cockroach sql --url $DATABASE_URL
    ```

    Pernyataan SQL dalam file inisialisasi harus dijalankan akan menampilkan :
    ```
    CREATE TABLE

    Time: 102ms
    ```

### Jalankan kode
File `main.py` menggunakan **connection string** yang disimpan ke `DATABASE_URL` environment variable untuk terhubung ke cluster Anda dan mengeksekusi kode.

Jalankan aplikasi:
```
$ python main.py
```

Aplikasi akan terhubung ke **CockroachDB**, dan kemudian melakukan beberapa penyisipan baris sederhana, pembaruan, dan penghapusan.

Outputnya akan terlihat seperti berikut:
```
Creating new accounts...
Created new account with id 534fe2fd-824b-4ea3-a8f8-5f7d6e8e51a3 and balance 675410.
Created new account with id 6c2d71ab-180b-4608-9045-7df461a01701 and balance 535972.
Created new account with id aed6c03b-4b4f-42d6-9c13-b7de02b528e7 and balance 817291.
...
Created new account with id a27bca32-cc27-4e23-8261-73486437943e and balance 485417.
Random account balances:
Account 5d064a2f-70a8-46b0-a141-5bf24403e705: 249601
Account 0a6c3c52-1d33-4906-8839-966e2a3e6694: 634961
Transferring 335073 from account 5d064a2f-70a8-46b0-a141-5bf24403e705 to account 0a6c3c52-1d33-4906-8839-966e2a3e6694...
Transfer complete.
New balances:
Account 5d064a2f-70a8-46b0-a141-5bf24403e705: 800977
Account 0a6c3c52-1d33-4906-8839-966e2a3e6694: 214557
Deleting existing accounts...
Deleted account b5cb0b18-520f-45db-b5ec-0141575a7536.
Deleted account 7f6361a3-1891-462e-bc6c-f289f77fd4c0.
Deleted account 6c55e9cb-71b5-46d9-8f29-644c6ba3e9d4.
Deleted account 2e20d57a-b837-499e-931f-f3140c7d2132.
Deleted account 1ff4085d-ef3f-4479-9884-1ece0f29afdf.
```

Dalam **shell SQL** yang terhubung ke cluster, Anda dapat memverifikasi bahwa baris berhasil dimasukkan, diperbarui, dan dihapus. Menggunakan perintah berikut :
```sql
SELECT COUNT(*) FROM accounts;
```

Pernyataan yang akan ditampilkan sebagai berikut :
```
  count
---------
     95
(1 row)
```