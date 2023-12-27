### Step Flow Deploy Project

Berikut adalah langkah-langkah untuk deploy project Django:

#### Buka terminal/command prompt, kemudian ikuti langkah-langkah dibawah

Buat virtual environment menggunakan kode dibawah:

```
python -m venv venv
```

Kemudian aktifkan venv yang telah dibuat

```
.\venv\Scripts\activate
```

Lakukan upgrade Pip

Pastikan pip Anda sudah dalam versi terbaru. Anda dapat menggunakan perintah berikut untuk memeriksa versi pip:

Jika pip Anda belum dalam versi terbaru, Anda dapat mengupgradenya dengan perintah berikut:

```
python -m pip install --upgrade pip
```

Kemudian silahkan install requirements.txt
``` 
pip install .\image-project-mknows\requirements.txt
```

Lalu pindah ke directory project
```
cd .\image-project-mknows\image_project\
```

Kemudian lakukan migration untuk membuat tabel.
Untuk membuat migrations, Anda dapat menggunakan perintah berikut:

```
python manage.py makemigrations
``` 
Setelah membuat migrations, Anda perlu menjalankan migrations untuk menerapkan perubahan pada database.
```
python manage.py migrate --run-syncdb
```
Setelah migrations dijalankan, Anda dapat menjalankan server Django.

Untuk menjalankan server Django, Anda dapat menggunakan perintah berikut:
```
python manage.py runserver
```

Selamat project telah sukses di deploy.
