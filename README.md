SOSYAL MUHENDISLIK METINLERINDE FOL TABANLI CIKARIM


CALISMA ORTAMI
Python 3.11
Gerekli paketler: matplotlib, openpyxl

DOSYALARIN CALISTIRILMASI

1) solution_code.ipynb
   Jupyter Notebook ile acilir ve hucreler sirasiyla calistirilir.
   Notebook, messages.csv dosyasini ayni klasorden okur; facts.pl,
   rules_buggy.pl, rules_clean_base.pl ve rules_fixed.pl dosyalarindaki
   kural setlerini Python icinde tekrar tanimlar; A'dan G'ye kadar olan
   yedi modeli calistirir; results.csv dosyasini uretir.
   
3) raw_llm_solution.py
   LLM'den alinan ham cozumdur, hic degistirilmeden birebir saklanmistir.
   python3 raw_llm_solution.py komutu ile calistirilabilir.
   NOT: Suspicious/NeedsHumanReview kurallari arasindaki dongu nedeniyle
   backward_chain fonksiyonu bazi sorgularda gecici olarak uzun surebilir
   (bkz. llm_error_log.xlsx, hata kodu E5).

4) raw_llm_rules.pl
   LLM'den alinan ham kural setidir (Model F'de kullanilmistir).

5) rules_fixed.pl
   Adim 8'de yapilan tum duzeltmelerin uygulandigi nihai kural setidir
   (Model G'de kullanilmistir).

6) results.csv
   Yedi modelin (A-G) tum performans metriklerini icerir.

7) llm_error_log.xlsx
   Iki sekmelidir: LLM_Hata_Kaydi
   Hata_Kodlari (E0-E14 siniflandirmasi ve bu calismada gorulen hatalar).


NOT: solution_code.ipynb ve raw_llm_solution.py, messages.csv dosyasini ayni klasorden okur

SONUC OZETI
Model G (duzeltilmis kural seti + stratified negation) en yuksek
dogrulugu vermistir. Model B (naive forward chaining, hatali kural
seti) dongu tespiti (loop_detected=True) ve yuksek iterasyon sayisi
gostermistir.
