#!/usr/bin/env python
# coding: utf-8

# # 18. 정규식(Regular Expression)
# 
# #### 정규식 혹은 정규표현식은 특정한 규칙을 가진 문자열의 집단을 표현하는 방식이다.
# 

# #### Python 은 정규식을 지원하는 re module 을 제공한다. 사용 방법은 다음과 같다.  

# - re.compile 을 이용하여 정규식을 compile 하여 pattern 객체를 얻음.  

# - pattern 객체를 이용하여 문자열의 검색을 수행.   

# - 검색 method :  
# 
#     search() - 문자열 전체를 검색하여 정규식과 match 되는지 조사  (문자열의 아무곳이나 match)  
# 
#     match = re.search(pattern, str)
# 
#     검색하여 match 되는 문자열이 있으면 match object 를 반환하고, 없으면 None 이 반환된다. 

# pattern = re.compile(pattern)  
# match = pattern.search(string)
# 
# - 두줄을 아래와 같이 한줄로 코딩 가능
# 
# match = re.match(pattern, string)  
# 
# - 첫번째 match 되는 문자열 반환
# - match.group() method 를 통해 matching text 를 가져온다.

# pattern = re.compile(pattern)  
# matches = pattern.finditer(string)
# 
# - 두줄을 아래와 같이 한줄로 코딩 가능
# 
# matches = re.finditer(pattern, string)  
# 
# - 모든 match 되는 문자열 반환
# - for 문을 이용하여 matches print

# In[2]:


import re

str = 'an example word:cat!!'

match = re.search(r'word:\w\w\w', str)      # r - raw string : backslash 를 특수문자로 인식하지 않는다.

print('abc\tabc')
print(r'abc\tabc')


# In[3]:


if match:
    print('found - ', match.group())
else:
    print('Not found')


# ## 정규식의 기본 pattern 

# - a, X, 9 $\leftarrow$ 영문 대소문자, 숫자는 자기 자체로 match 시킨다.

# In[22]:


re.search(r'ta', 'testaaabbaacca')


# In[23]:


match = re.search(r'ta', 'testaaabbaacca')

match.group()


# - meta 문자는 특수한 의미를 가지므로 위와 같이 자기 자체로 match 시키지 않는다.   
#     . ^ $ * + ? { } [ ] \ | ( )
# 

# In[28]:


match = re.search(r'\wb', 'testabaa\wbaacca')

match.group()


# - . (period) 는 아무 문자와도 match 가 된다. (단, \n (new line) 제외)  

# In[32]:


match = re.search(r'.ca.', 'testabaa\wbaa%ca&')

match.group()


# - \w 는 word character (a-z, A-Z, 0-9) 와 match 된다. (single character)  

# In[34]:


match = re.search(r'\w\w\wa', 'tcstabaa\wbaaccac')

match.group()


# - \b 는 word 와 non-word 의 boundary 이다

# In[4]:


match = re.search(r'\bsend', 'resend send')

match.group()


# - \s 는 white space (space, new line, return, tab) 와 match 된다. (single white space)

# In[41]:


match = re.search(r'\s\w\wa', 'tcst abaa\wbaaccac')

match.group()


# - \S 는 non-white space 와 match 된다.

# In[44]:


match = re.search(r'\S\w\wa', 'tcst abaa\wbaaccac')

match.group()


# In[18]:


matches = re.finditer(r'\S\w\wa', 'tcst abaa\wbaaccac')

for match in matches:
    print(match)


# - \d 는 decimal digit (0-9) 와 match 된다.

# 
# - ^ 는 string 의 처음을 의미, $ 는 string 의 끝을 의미한다.

# In[13]:


match = re.finditer(r'^ha', 'ha haha')

list(match)


# - special character 는 \를 앞에 두면 된다. $\text{ex, \., \\, \@}$

# In[46]:


match = re.search(r'Mr\. K', 'Hello, Mr. Kim')

match.group()


# In[47]:


match = re.search(r'iii', 'piiig')

match.group()


# In[48]:


match = re.search(r'igs', 'piiig')

type(match)


# In[50]:


match = re.search(r'..g', 'piiig')

match.group()


# In[51]:


match = re.search(r'\d\d\d', 'p123g')

match.group()


# In[7]:


match = re.search(r'\w\w\w', '@@abcd!!')
match.group()


# In[8]:


match = re.search(r'^b', 'rebook')
type(match)


# In[9]:


match = re.search(r'k$', 'book')

match.group()


# ### match 되는 pattern 의 반복 (Repetition)

# - \+ $\rightarrow$ 1개 혹은 그 이상의 해당 pattern 이 왼쪽에 있음

# In[49]:


matches = re.finditer(r'\w+', 'book store')

for match in matches:
    print(match)


# - \* $\rightarrow$ 0 혹은 그 이상의 해당 pattern 이 왼쪽에 있음

# In[50]:


matches = re.finditer(r'\w*', 'book store')

for match in matches:
    print(match)


# - \? $\rightarrow$ 0 혹은 1 개의 해당 pattern 이 왼쪽에 있음

# In[51]:


matches = re.finditer(r'\w?', 'book store')

for match in matches:
    print(match)


#  
# - match 다음에 즉시 if 문으로 match 성공 여부를 check 하는 것이 일반적인 사용법
# 
# 

# In[53]:


match = re.search(r'k$', 'book')

if match:
    print('found - ', match.group())
else:
    print('Not found')


# ### Leftmost and Largest 규칙
# 
# search 는 가장 왼쪽 (leftmost) match 를 먼저 찾고 repetition 메타문자 (\., \*, \+)를 만족하는 한 match 를 계속 찾는다.

# In[10]:


match = re.search(r'pi+', 'piiig')

match.group()


# In[11]:


match = re.search(r'i+', 'piigiiig')

match.group()


# In[12]:


match = re.search(r'\d\s*\d\s*\d', 'xx1 2    3xx')

match.group()


# In[13]:


match = re.search(r'\d\s*\d\s*\d', 'xx12   3xx')
match.group()


# In[14]:


match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
match.group()


# In[15]:


match = re.search(r'^b\w+', 'foobar')
type(match)


# In[16]:


match = re.search(r'b\w', 'foobar')

match.group()


# ### 대괄호 ([  ])

# character set 을 표시한다. 예를 들어 [abc] 는 a, b, c 와 match 된다. 단, [ ] 내의 \. 는 메타문자가 아니라 실제 \. 표시이다. 

# [a-z] : 소문자  
# [A-Z] : 대문자  
# [1-9] : digit

# In[38]:


str = "전화번호 010-1234-9876 혹은 02-1544-1899 로 Telephone 연락" 
matches = re.finditer(r'[012]+-\d+-\d+', str)
for match in matches:
    print(match)


# In[41]:


matches = re.finditer(r'[a-zA-Z]+', str)
for match in matches:
    print(match)


# In[31]:


str = 'Please send me email to young-jea.oh@citi.com with your return address'

match = re.search(r'[\w.-]+@[\w.-]+', str)

match.group()


# ### Group 구분
# 
# matching text 를 여러 부분으로 구분할 때 사용

# In[18]:


str = 'Please send me email to young-jea.oh@citi.com with your return address'

match = re.search(r'([\w.-]+)@([\w.-]+)', str)


# In[19]:


print(match.group())
print(match.group(1))
print(match.group(2))


# ### findall
# re.search() 는 첫번째 match 하나만 return
# 
# re.findall() 은 string 에서 match 되는 것 전부 list 로 return

# In[59]:


str = """
메인 이멜 주소는 young-jea.oh@citi.com 이고 보조 이멜 주소는 yjohhhhh@naver.com 입니다. 
문의는 faq@gmail.net 으로 보내세요.
"""


# In[60]:


matches = re.findall(r'[\w.-]+@[\w.-]+', str)


# In[61]:


matches


# In[62]:


matches = re.findall(r'([\w.-]+)@([\w.-]+)', str)


# In[63]:


matches


# ### 연습문제

# # HTML 에서 BABY 이름 찾기

# ```html
# <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td> 
#     ```
# 에 match 되는 정규표현식을 이용하여 (rank, boy-name, girl-name) tuples 추출하여 print

# ```python
# import sys
# import re
# ```

# ```python
# def extract_name(filename):
#     names = []
#     f = open(filename, 'r')
#     text = f.read()
#     tuples = re.findall(r'<td>(\d)</td><td>(\w+)</td><td>(\w+)</td>', text)
#     for tup in tuples:
#         print(tup[0], tup[1], tup[2])
# ```

# ```python
# if __name__ == '__main__':
#     args = sys.argv[1:]
#     if not args:
#         print("file 명을 parameter 로 입력 바랍니다.")
#         sys.exit(1)
# 
#     filename = './babynames/' + args[0]
#     extract_name(filename)
# ```
"""
step 1 - https://developers.google.com/edu/python/exercises/baby-names 에서
file download 하여 babynames directory 로 save

step 2 - <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td> 에
match 되는 정규표현식을 이용하여 (rank, boy-name, girl-name) tuples 추출하여
print

"""
import sys
import re

def extract_name(filename):
    names = []
    f = open(filename, 'r')
    text = f.read()
    tuples = re.findall(r'<td>(\d)</td><td>(\w+)</td><td>(\w+)</td>', text)
    for tup in tuples:
        print(tup[0], tup[1], tup[2])

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print("file 명을 parameter 로 입력 바랍니다.")
        sys.exit(1)

    filename = './babynames/' + args[0]
    extract_name(filename)