# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut adalah lembaga pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah menghasilkan banyak lulusan berkualitas. Namun, institusi ini juga menghadapi tantangan serius dengan tingginya jumlah mahasiswa yang tidak menyelesaikan studi alias dropout.

Masalah ini menjadi perhatian utama, karena dapat memengaruhi reputasi dan kualitas pendidikan. Untuk itu, Jaya Jaya Institut berupaya mengidentifikasi mahasiswa yang berisiko mengalami dropout sedini mungkin agar dapat diberikan pendampingan khusus.

Sebagai institusi pendidikan, Jaya Jaya Institut ingin mengatasi permasalahan tingginya angka dropout di kalangan mahasiswa. Institusi berencana menggunakan dataset terkait performa mahasiswa yang telah dikumpulkan untuk mengembangkan model machine learning prediktif. Selain itu, Jaya Jaya Institut memerlukan dashboard yang dapat memudahkan mereka dalam memahami data dan memantau perkembangan akademik mahasiswa secara lebih efisien.

### Permasalahan Bisnis
1. **Menganalisis Faktor-Faktor yang Menyebabkan Tingginya Dropout Rate**\
   Apa saja faktor yang memengaruhi keputusan mahasiswa untuk berhenti melanjutkan studi di Jaya Jaya Institut?
2. **Memprediksi Potensi Risiko Mahasiswa Dropout**\
   Bagaimana cara memprediksi mahasiswa yang berisiko Dropout agar pihak Insitusi dapat melakukan intervensi secara tepat?
3. **Memprediksi Kemungkinan Dropout Secara Efisien**\
   Bagaimana solusi agar pihak Institusi dengan mudah memprediksi risiko Dropout secara efisien?
5. **Membangun Visualisasi Data yang Informatif**\
   Bagaimana membuat Jaya Jaya Institusi dapat memantau faktor-faktor risiko Dropout melalui visualisasi yang mudah dipahami?

### Cakupan Proyek
1. **Menganalisa Data Performa Mahasiswa**
   - Melakukan eksplorasi mendalam terhadap data (EDA) untuk menemukan tren dan wawasan penting yang berkaitan dengan status mahasiswa (Dropout, Enrolled, Graduate).
   - Mengidentifikasi faktor-faktor utama yang memiliki pengaruh signifikan terhadap status Dropout mahasiswa.
2. **Membangun Model Machine Learning Prediksi**
   - Membangun model machine learning untuk memperkirakan kemungkinan seorang mahasiswa akan Dropout.
   - Model ini bertujuan membantu Jaya Jaya Institusi mengidentifikasi mahasiswa yang berisiko Dropout agar bisa segera mencari cara solutif.
   - Melakukan deployment model machine learning ke Streamlit Cloud agar pihak Institusi dapat memprediksi risiko Dropout secara efisien
3. **Membuat Business Dashboard**
   - Merancang dashboard interaktif yang menyajikan visualisasi dari faktor-faktor kunci penyebab Dropout.
   - Dashboard ini akan menjadi alat bantu bagi pihak Institusi dalam memantau kondisi status mahasiswa.
4. **Merekomendasikan Strategi Efektif**
   - Menyusun saran strategis berdasarkan temuan data dan hasil prediksi guna membantu Jaya Institusi dalam menurunkan angka Dropout di masa mendatang.

### Persiapan
Institusi menyiapkan dataset yang memuat data terkait mahasiswa, mencakup aspek demografis, performa akademik, status finasial mahasiswa dan lainnya. Data ini berguna untuk menganalisis pola dan keterkaitannya dengan angka Dropout.\
Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md

Setup environment:
1. Prasyarat Tools
   - Google Colab: [Google Colab](https://colab.research.google.com/)
   - Google Looker Studio: [Looker Studio](https://lookerstudio.google.com/u/0/navigation/reporting)
2. Clone Repository\
   Clone Repository menggunakan `git`:
   ```
   git clone https://github.com/username/education_status_predictive
   cd education_status_predictive
   ```
3. Setup Google Colab
   ```
   Python 3.11.12
   ```
   Penggunaan Google Colab sudah menyediakan versi Python terbaru secara default. Sebagian besar library populer sudah kompatibel.
4. Setup Looker Studio
   - Membuat **Blank Report**
   - Koneksikan data dengan Upload File CSV yaitu `data_clean.csv`
   - Kemudian klik **Add Data to Report**
   - Sesuaikan layout menggunakan **Responsive Layout**
   - Dataset dan canvas dashboard telah tersedia dan dapat digunakan untuk visualisasi data

5. Setelah seluruh proses setup selesai, Anda bisa menjalankan skrip utama atau mulai melakukan proses prediksi.
   - Untuk menjalankan analisis utama terdapat pada
     ```
     status_predictive_notebook.ipynb
     ```
   - Untuk mencoba prediksi menggunakan model machine learning, jalankan perintah berikut di terminal atau command prompt
     ```
     streamlit run app.py
     ```

## Business Dashboard
Perancangan Business Dahboard diharapkan dapat membantu Jaya Jaya Institusi untuk monitoring berbagai faktor yang mempengaruhi Dropout Rate mahasiswa. Dashboard ini memberikan visualisasi data yang informatif terhadap pola data, korelasi antar variabel, dan faktor risiko utama mahasiswa berhenti untuk melanjutkan studi mereka.

Dashboard ini mencakup:
1. **Key Performance Indicator (KPI) Section**\
   Section ini menampilkan informasi umum indikator terkait Status Dropout mahasiswa.
   - **Total Students:** Menampilkan jumlah keseluruhan mahasiswa, yaitu sebanyak **4,424** mahasiswa
   - **Graduated Students:** Menampilkan jumlah mahasiswa yang lulus, yaitu sebanyak **2,209** mahasiswa
   - **Enrolled Students:** Menampilkan jumlah mahasiswa yang terdaftar (sedang melaksanakan studi), yaitu sebanyak **794** mahasiswa
   - **Dropout Students:** Menampilkan jumlah mahasiswa yang tidak menyelesaikan pendidikan, yaitu sebanyak **1,421** mahasiswa
   - **Dropout Rate:** Menampilkan persentase mahasiswa Dropout terhadap total mahasiswa, yaitu **32.12%**. Dapat memberikan gambaran seberapa besar Dropout Rate pada Institusi
2. **Distribution Rate of Student Status**
   - Menampilkan pie chart yang menunjukkan bahwa sebagian besar mahasiswa telah lulus **(49.9%)**, sedangkan mahasiswa terdaftar sebesar **(17.9%)**. Untuk mahasiswa Dropout terlihat persentase signifikan sebesar **(32.1%)**
3. **Gender Distribution by Student Status**
   - Menampilkan horizontal bar chart yang menunjukkan angka Dropout antara laki-laki **(701 mahasiswa)** dan perempuan **(720 mahasiswa)** terlihat seimbang. Meskipun seimbang, gender merupakan fitur yang dianggap penting dan berkorelasi tinggi terhadap status mahasiswa
4. **Academic Section**\
   Section ini menampilkan informasi terkait performa akademik mahasiswa.
   - **Distribution Students by Grade (1st Semester)**
     - Menapilkan stacked vertical bar chart yang menunjukkan bahwa nilai terendah mahasiswa **(0-5)** memiliki jumlah Dropout yang tinggi **(570 mahasiswa)**
     - Nilai tinggi rentang **(11-20)** didominasi oleh siswa yang lulus **(Graduate)** 
   -  **Approved Curricular Units (1st Semester)**
      - Menampilkan pivot table yang menunjukkan bahwa jumlah unit yang disetujui **(0-5 unit)** mayoritas berstatus Dropout **(1,217 mahasiswa)**. Semakin tinggi jumlah unit yang disetujui, angka Dropout cenderung menurun
   -  **Distribution Students by Grade (2nd Semester)**
      - Menunjukkan bahwa terdapat kemiripan pola dengan data semester 1. Nilai mahasiswa dengan rentang **(0-5)** memiliki jumlah Dropout tertinggi **(727 mahasiswa)**
      - Pola dominasi mahasiswa yang lulus juga serupa
   -  **Approved Currricular Units (2nd Semester)**
      - Menunjukkan adanya kemiripan pola dengan data semester 1. Jumlah unit yang disetujui **(0-5)** mayoritas berstatus Dropout **(1,287 mahasiswa)**. Semakin banyak unit yang disetujui, semakin kecil angka Dropout.
5. **Finance & Age Section**\
   Section ini menampilkan informasi yang divisualisasikan menggunakan vertical bar chart terkait status finansial dan umur mahasiswa ketika menempuh pendidikan di Institusi.
   - **Tuition Fees Up to Date by Student Status**
     - Menunjukkan bahwa mahasiswa yang tidak membayar biaya kuliah tepat waktu, mayoritas berstatus Dropout **(457 mahasiswa)**. Sedangkan mahasiswa yang membayar tepat waktu, mayoritas berstatus Graduate **(2,180 mahasiswa)**. Sehingga faktor keuangan berpengaruh besar terhadap dropout.
   - **Scholarship Holder by Student Status**
     - Menunjukkan bahwa mahasiswa yang tidak menerima beasiswa memiliki angka dropout yang tinggi **(1,287 mahasiswa)**, sedangkah terdapat **(134 mahasiswa)** yang memperoleh beasiswa tetapi mengalami Dropout. Bantuan finansial berhubungan dengan retensi dan keberhasilan studi mahasiswa
   - **Debtor by Student Status**
     - Menunjukkan bahwa mahasiswa yang memiliki tunggakan biaya mayoritas mengalami Dropout **(312 mahasiswa)**, sedangkan mahasiswa yang tidak memiliki tunggakan biaya di dominasi oleh mahasiswa yang lulus **(2,108 mahasiswa)**. Tunggakan mahasiswa juga merupakan indikator risiko dropout.
   - **Starting Age Enrollment by Students Status**
     - Menunjukkan bahwa mahasiswa dengan rentang usia **(17-20 tahun)** memiliki angka Dropout yang signifikan, meskipun kelompok umur tersebut bermayoritas lulus. Memulai pendidikan saat rentang usia yang lebih tua cenderung mengalami Dropout. Sehingga semakin tua usia masuk, semakin tinggi risiko dropout.

Dashboard ini sangat membantu pihak Jaya Jaya Institut dalam mengidentifikasi profil mahasiswa berisiko untuk dropout, agar bisa segera diberikan bimbingan atau intervensi.\
Link Dashboard: [Status Monitoring Dashboard Jaya Institut](https://lookerstudio.google.com/reporting/e3efc3bb-a66c-406a-a160-8ee65e7cc51b)

## Menjalankan Sistem Machine Learning
Untuk mengoperasikan prototipe sistem machine learning yang telah dikembangkan, tersedia dua opsi metode: menjalankannya secara lokal atau memanfaatkan layanan Streamlit Cloud.
1. **Menjalankan Secara Lokal**
   - Pastikan seluruh dependensi yang dibutuhkan telah terpasang.
   - Buka terminal atau command prompt, lalu jalankan perintah berikut:
     ```
     streamlit run app.py
     ```
   - File aplikasi utama ditulis dalam berkas Python bernama `app.py.`
2. **Menjalankan Melaui Streamlit Cloud**
   - Sistem prototipe ini juga dapat diakses secara daring melalui tautan berikut:\
     [Education Status Prediction App](https://education-status-prediction.streamlit.app/)

## Conclusion
Proyek ini menghasilkan sebuah sistem prediksi untuk mengidentifikasi potensi dropout mahasiswa di Jaya Jaya Institut. Berdasarkan analisis data dan evaluasi model machine learning yang dilakukan, diperoleh temuan bahwa:
1. **Faktor akademik,** khususnya jumlah mata kuliah yang disetujui dan nilai pada semester 1 dan 2, merupakan indikator paling kuat dalam memprediksi Dropout.
2. **Faktor keuangan,** contohnya seperti status pembayaran uang kuliah, kepemilikan beasiswa, dan tunggakan biaya kuliah juga berkontribusi signifikan terhadap kemungkinan Dropout.
3. **Faktor personal,** seperti usia saat masuk kuliah dan jenis kelamin juga berkorelasi cukup kuat dengan Dropout.
4. **Model prediksi** yang dibangun menggunakan algoritma **Gradient Boosting Classifier** menunjukkan performa akurasi dan F1-score yang dinilai cukup baik dalam membedakan mahasiswa yang kemungkinan akan dropout atau tidak. Tetapi masih memiliki ruang untuk kesalahan.
5. **Prototipe** sistem prediksi telah dikembangkan menggunakan **Streamlit**, dan **dashboard analitik** berbasis **Looker Studio** juga telah dikembangkan untuk membantu pihak Institusi memantau performa mahasiswa secara menyeluruh.

### Rekomendasi Action Items
1. **Meningkatkan Bimbingan dan Motivasi Akademik**
   - Melakukan intervensi pada mahasiswa yang bernilai dan jumlah mata kuliah yang disetujuinya rendah dengan memberikan program mentoring atau remedial untuk memperbaiki performa semester 1 dan 2
   - Memberikan bimbingan dan motivasi dini terhadap mahasiswa yang baru masuk, terkait pentingnya meningkatkan performa belajar guna menghindari performa yang buruk di masa depan. 
2. **Melakukan Pendekatan Khusus**
   - Mahasiswa yang berusia lebih tua saat pendaftaran atau yang memiliki tunggakan (debtors) memerlukan pendekatan fleksibel seperti kelas online, jadwal malam, atau dukungan psikologis.
3. **Meningkatkan Dukungan dan Layanan Finansial**
   - Mahasiswa yang tidak membayar uang kuliah tepat waktu atau tidak memiliki beasiswa perlu diprioritaskan untuk diberi keringanan (seperti cicilan).
   - Perlu mempertimbangkan sistem notifikasi dini untuk mahasiswa yang mengalami tunggakan dan menyediakan konseling baik bersama mahasiswa maupun orang tua/wali.
4. **Menggunakan Sistem Secara Rutin**
   - Model prediksi dapat digunakan oleh dosen wali, bagian keuangan, dan konselor sebagai bahan dasar pengambilan keputusan.
   - Pantau dashboard Looker Studio secara berkala untuk memantau performa akademik dan keuangan mahasiswa.
