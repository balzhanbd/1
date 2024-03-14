#ex1
#import re
#with open("row.txt",'r') as f:
    #content = f.read()
    #pattern = "ab+"
    #if re.search(pattern, content):
         #matching=re.findall(pattern,content)
         #print(matching)

#ex2
#import re
#with open("row.txt",'r') as f:
    #content = f.read()
    #pattern1 = "abb"
    #pattern2 = "abbb"
    #if re.search(pattern1, content) or re.search(pattern2,content):
        #matching1=re.findall(pattern1,content)
        #matching2=re.findall(pattern2,content)
        #print(matching1,matching2)
    
#ex3
# import re
# with open("row.txt", "r") as f:
#     content = input()
#     pattern = r'[a-z]+_[a-z]+'
#     matching = re.findall(pattern, content)
#     print(matching)

#ex4
# import re
# with open("row.txt", "r") as f:
#     content = f.read()
#     pattern = r'[A-Z]+[a-z]+'
#     matching = re.findall(pattern, content)
#     print(matching)
    
#ex5
# import re
# content=input()
# pattern=r'a.*b$'
# matching=re.findall(pattern,content)
# print(matching)

#ex6
# import re
# input_text =input()
# pattern = r'[ ,.]'
# replaced_text = re.sub(pattern, ':', input_text)
# print(replaced_text)

#ex7
# import re
# input_text = input() 
# print(''.join(x.capitalize() or '_' for x in input_text.split('_')))

#ex8
# import re
# input=input()
# pattern = r'(?=[A-Z])'
# result = re.split(pattern, input)
# print(result)

#ex9
# import re
# input_text =input()
# pattern = r'([A-Z])'
# replaced_text = re.sub(pattern, r' \1', input_text)
# print(replaced_text)

#ex10
import re
input_text=input()
str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_text)
print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower())