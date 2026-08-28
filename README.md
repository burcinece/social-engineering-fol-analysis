 Dinamik Ağ Topolojilerinde A* Algoritması ile
Oltalama Yayılım Analizi
==============================================================

Klasördeki dosyalar
--------------------
solution_code.ipynb   -> Çalışan notebook (tüm fonksiyonlar, Model A/B/C, LLM karşılaştırması)
raw_llm_code.py        -> LLM'den alınan ham kod (Model D)
fixed_code.py           -> Elle düzeltilmiş kod (Model E)
results.csv             -> S1-S12 senaryolarının tüm metrikleri (Model A-E)
llm_error_log.xlsx      -> LLM hata kayıt formu
figures/                -> İstenen 7 grafik
readme.txt              -> Bu dosya

Nasıl çalıştırılır
--------------------
Gerekli paketler: pandas, matplotlib (standart kütüphaneler dışında)
    pip install pandas matplotlib

Tek başına çalıştırma:
    python3 raw_llm_code.py
    python3 fixed_code.py

Notebook'u çalıştırmak için (aynı klasörde olmalı, results.csv ve figures/ ile birlikte):
    jupyter notebook solution_code.ipynb
    Kernel > Restart & Run All

Kısa özet
----------
Model A - Statik A*            : IDS'i yok sayar
Model B - Naive Dynamic A*      : IDS maliyeti var ama durum sadece node, heuristik güncellenmiyor
Model C - Time-Aware Dynamic A* : doğru çözüm, durum = (node, step, alarm_bin)
Model D - LLM (ham)             : raw_llm_code.py
Model E - LLM (düzeltilmiş)     : fixed_code.py

results.csv, S1-S12 senaryolarının her biri için 5 tekrarla alınan ortalama sonuçları
içerir. Optimality gap, her modelin bulduğu yolun gerçek dinamik IDS maliyetine göre
yeniden hesaplanmasıyla bulunmuştur.
