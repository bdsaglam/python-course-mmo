
# coding: utf-8

# # Exam

# ## Question 1
# 
# Take two sequences, find the indices where the second is matched in the first.
# 
# Verilen iki diziden ikincisinin birinci dizide hangi indexlerde eşleştiğini yazan bir program yazın. Program eğer hiç eşleşme yoksa boş liste verebilir.
# 
# ```
# Input: [0,0,1,1,0,1,1,0,1,0,1] and [1,0,1]
# Expected output: [3,6,8]
# 
# Input: [0,1,1,0,1,1,0,1,0,1] and [1,1,1]
# Expected output: []
# 
# Input: 'tanzania' and 'an'
# Expected output: [1, 4]
# ```

# ## Question 2
# 
# Write a Python program that computes greatest common divisor of two numbers.
# 
# Verilen iki sayının en büyük ortak bölenini bulan bir program yazın.
# 
# ```
# Input: 0, 1
# Expected output: 1
# 
# Input: 1, 2
# Expected output: 1
# 
# Input: 2, 5
# Expected output: 1 
# 
# Input: 2, 4
# Expected output: 2
# 
# Input: 12, 18
# Expected output: 6
# 
# ```

# ## Question 3
# 
# Remove all characters repeating.
# 
# Bir stringdeki ardışık olarak tekrar eden karakterlerden tekrar edenleri silen bir program yazın.
# 
# ```
# Input: "aaabccddd"
# Expected result: "abcd"
# 
# Input: "aaabccbddad"
# Expected result: "abcbdad"
# ```

# ## Question 4
# Write a Python program to count the number of characters (character frequency) in a string.
# 
# Input: "google"
# 
# Expected Output: {'g': 2, 'o': 2, 'l': 1, 'e': 1}

# ## Question 5
# 
# Write a function that takes a string with a name, phone number and email; extract phone number and email as a tuple.
# 
# Verilen örnek metinlerden telefon numarası ve emaili tuple olarak çıkaran bir fonksiyon yazın.
# 
# Input: "Name: Guido van Rossum Phone:0 532 123 45 67 guido@python.org"   
# Expected Result: ('05321234567', 'guido@python.org')
# 
# Input: "name: Hedy Lamarr phone: +01 (222) 123 45 67 hedy@lamarr.com"   
# Expected Result: ('012221234567', 'hedy@lamarr.com')
# 
# Input: "İsim: Masal Hattı Tel: 0800 314 11 66 masal@turkiye.gov.tr"   
# Expected Result: ('08003141166', 'masal@turkiye.gov.tr')

# ## Question 6
# 
# Write a function that flattens a nested list. Use isinstance(element, list) to check whether an element of the given list is list or not.
# 
# İç içe bir listeyi düzleştiren bir fonksiyon yazın. Elemanların liste olup olmadığını isinstance(element, list) ile kontrol edebilirsiniz. Örneğin,
# 
# ```
# isinstance(1, list)
# >>> False
# 
# isinstance([1,2,3], list)
# >>> True
# 
# isinstance([], list)
# >>> True
# 
# ```
# 
# Your function named flatten:
# 
# ```
# Input:
# seq = [1,2,3,[3,2,1,[0,-1,-2]]]
# list(flatten(seq))
# 
# Output: 
# [1, 2, 3, 3, 2, 1, 0, -1, -2]
# 
# ```

# ## Question 7
# 
# From io folder, read all comma-separated files including 'sales-' in filename. Those files are monthly sales record for books. The fields represent respectively title, units sold and price. Calculate total sales revenue in three months for each book, sort them in descending order and write into a file named "total_book_sales.txt" in specified format below:
# 
# 
# io klasöründeki isminde 'sales-" geçen tüm dosyaları okuyun. Bu dosyalar aylık kitap satışlarına tekabül etmektedir. Kolonlar sırasıyla kitabın ismi, satış adedi ve fiyatıdır. Dosyaların tamamını okuyup her kitap için toplam satış gelirini hesaplayın. Daha sonra kitapları satış gelirine göre büyükten küçüğe sıralayıp alttaki format ile "total_book_sales.txt" dosyasına yazdırın.
# 
# ```
# header-width: 48, 8
# header-alignment: center, center
# entry-width:48,8
# entry-alignment: left, right
# float-precision: 1
# 
#                      Title                      Revenue 
# --------------------------------------------------------
# Pining for the Fisheries of Yore                   420.5
# The Duck Goes Here                                 125.5
# The Bricklayer's Bible                             110.3
# The Tower Commission Report                         64.0
# Swimrand                                            18.9
# ```

# ## Question 8
# 
# From io folder, read 'forbes500.csv' file. Find the companies which have at least 100,000 employees, profitted over 10 billion and have a positive growth rate.
# 
# io klasöründeki 'forbes500.csv' dosyasını okuyun. En az 100,000 çalışanı olan, 10 milyardan fazla kar etmiş ve pozitif büyüme oranına sahip şirketleri bulun. Daha sonra bu şirketleri çalışan başına edilen kara göre sıralayın.
# 

# ## Question 9
# 
# Solve the differential equation below for three different w values (1,3,5) from t=0 to t=50. Plot y results for three solutions in separate subplots.
# 
# Aşağıdaki differensiyel denklemi üç farklı w değeri (1,3,5) ile t=(0,50) zaman aralığı için çözün. Sonuçları üç farklı subplotta çizdirin.

# In[264]:


get_ipython().run_cell_magic('latex', '', "\\begin{align}\n\\omega_n = 3 \\newline\n\\zeta = 0.05 \\newline\n\\omega = 1,3,5 \\newline\n\\newline\n\\quad y'' + 2 \\zeta \\omega_n y' + \\omega_n^2 y = 10\\sin(\\omega t) \\newline\ninitial conditions = (0,0)\n\\end{align}")

