
# coding: utf-8

# # Python for engineers
# 
# ## Homework 2
# 
# #### Topics: String
# 
# Write your solutions to the cell below each question.

# ## Question 1
# 
# Write a program that takes a string and prints a string such that all the 'a's after an occurrence of a 'c' are turned to 'x'.
# 
# Bir string alıp, bu stringde eğer c'den sonraki a'ları x'e çeviren bir program yazın.
# 
# ```
# Input: "abcd"
# Expected output: "abcd"
# 
# Input: "acbcdada"
# Expected output: "acbcdxdx"
# 
# Input: "ababcabac"
# Expected output: "ababcxbxc"
# ```

# ## Question 2
# 
# Write a Python program that takes a word and removes vowels.
# 
# Bir stringdeki sesli harfleri çıkartan bir program yazın.
# 
# 
# ```
# vowels = {'a','e','ı','i','o','ö','u','ü'}
# 
# Input: "cem Yılmaz"
# 
# Expected output: "cm Ylmz"
# ```

# ## Question 3
# 
# Take a string and replace some characters with an appropriate number.
# 
# Bir string alıp, bazı karakterleri karşılık gelen sayı karakteriyle değiştirin.
# 
# ```
# characters = ['E','I','A', 'O', 'B', 'Z']
# numliterals = ['3', '1', '4', '0', '8', '7']
# 
# Input: "CEM YILMAZ"
# Expected result: "C3M Y1LM47"
# ```
# Hint: Iterate over two list of characters simultaneously and use str.replace one by one

# ## Question 4
# 
# Take a string representing name and surname, split it into name and surname.
# 
# İsim ve soyismi temsil eden bir string alıp, isim ve soyisim olarak 2 ayrı string olarak ayırın.
# 
# ```
# Input: "Raymond Hettinger"
# Expected result: ["Raymond", "Hettinger"]
# 
# Input: "Barış Deniz Sağlam"
# Expected result: ["Barış Deniz", "Sağlam"]
# ```

# ## Question 5
# Take a string consisting of multiple website adresses separated by space and extract all domain names.
# 
# Websitelerinin aralarında virgül karakteriyle sıralandığı bir string alıp domain isimlerini çıkarın.
# 
# ```
# Input: "https://www.python.org, www.metu.edu.tr, comind.ai, edevlet.turkiye.gov.tr, https://jupyter.org"
# Expected result: ["python", "metu", "comind", "turkiye", "jupyter"]
# ```

# ## Question 6
# 
# Remove all characters repeating.
# 
# Bir stringdeki tekrar eden karakterleri silen bir program yazın.
# 
# ```
# Input: "aaabccddd"
# Expected result: "abcd"
# 
# Input: "aaabccbddad"
# Expected result: "abcbdad"
# ```

# ## Question 7
# 
# Write a Python program to reverse words in a string.
# 
# Bir stringdeki kelimeleri ters çeviren bir program yazın.
# 
# ```
# Input: "Raymond Hettinger"
# Expected result: 'dnomyaR regnitteH'
# 
# Input: 'odiuG nav mussoR'
# Expected result: "odiuG "
# ```

# ## Question 8
# 
# Write a Python program to concatenate the each of the floating numbers listed upto 2 decimal places with a sign, centered in 8 character width. Concatenate those 8 character strings.
# 
# Bir dizi sayıyı 2 ondalık basamaklı, işaretli, 8 karakter genişlikte ortalanmış olarak birleştirin.
# 
# ```
# Input: [-3.1416, 2.71, -2, 6.62607004, 2.99]
# Expected output: ' -3.14    +2.71    -2.00    +6.63    +2.99  '
# 
# ```

# ## Question 9
# 
# Write a program to print each string in a list to newline with width of 20. 
# 
# If the string is a number like 123, align it to right, 
# 
# if the string is a float number like 3.14, align it to center,
# 
# otherwise, align it to left.
# 
# Input: 
# ```
# s = ["python", "123", "3.14", "PyCon2017"]
# ```
# 
# Expected Output:
# ```
# python              
#                12312
#         3.14        
# PyCon2017                
# ```  

# ## Question 10
# 
# Write a program to print each number in a list to newline with width of 20. 
# 
# If the number is less than 1, write it with 2 precision, align it to center,
# 
# if the number is greater than or equal to 1 and less than 10, write it and align it to left,
# 
# if the number is greater than or equal to 10, write it in scientific format with 3 precision and align it to right.
# 
# 
# Input: 
# ```
# seq = [-4, 0.7, 1, 10, 222323]
# ```
# 
# Expected Output:
# ```
#        -4.00        
#         0.70        
# 1                   
#            1.000E+01
#            2.223E+05         
# ```  
