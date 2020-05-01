---
title: "Instalasi Java"
date: 2019-07-06T20:36:48+07:00
draft: false
tags: ['instalasi']
categories: ['java']
---

Setelah mengetahui [apa itu Java](/posts/java/01-perkenalan/), selanjutnya kita akan
mencoba untuk mempersiapkan komputer kita agar dapat membuat sebuah program dengan
menggunakan bahasa pemrograman Java. Adapun hal-hal yang harus dipersiapkan adalah
berikut ini.

<br/>

1. Java Runtime Environment (JRE)
2. Java Development Kit (JDK)

<br/>

Karena kedua perangkat lunak di atas tidak diinstalasi bersamaan dengan Sistem Operasi sehingga
kita perlu melakukan instalasi secara manual. Berikut ini salah satu cara instalasinya berdasarkan
Sistem Operasi yang digunakan.

### 1. Windows
Karena keterbatasan mesin saya yang tidak terinstalasi Sistem Operasi Windows di dalamnya, maka
mari kita bukan alamat [berikut ini](https://www.whatismybrowser.com/guides/how-to-install-java/windows)
untuk melihat cara menginstall JRE di Windows.

<br/>

Kemudian, instalasi JDK dapat dilakukan dengan mengikuti cara yang ada [di sini](https://access.redhat.com/documentation/en-us/openjdk/11/html/openjdk_11_for_windows_getting_started_guide/getting_started_with_openjdk_for_windows).

Sampai di sini, komputer kita sudah siap untuk membuat program menggunakan bahasa pemrograman Java
sekaligus menjalankannya. Namun, yang menjadi catatan saat instalasi adalah
**pastikan JRE dan JDK memiliki versi yang sama**.

### 2. Linux (Ubuntu)
Instalasi JRE dan JDK di Linux Ubuntu dapat dilakukan dengan menjalankan perintah di bawah ini pada terminal emulator.
```sh
$ sudo apt install -y default-jre default-jdk
```

## Penutup
Setiap bahasa pemrograman, memiliki persiapan yang berbeda-beda.

<br/>
NB: <br/>
Di website ini, saya akan membagikan berbagai macam hal mengenai programming.
Mulai dari tutorial, tips dan trik, sampai berita (informasi-informasi terbaru)
mengenai programming.
