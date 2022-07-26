# y=b"python"
# print(y,type(y))     # b'python' <class 'bytes'>
# print(y,list(y))       # b'python' [112, 121, 116, 104, 111, 110]
# print(y,tuple(y))       #  b'python' (112, 121, 116, 104, 111, 110)
# print(y,set(y))         # b'python' {104, 110, 111, 112, 116, 121}     
# y=b"python"
# for i in y:
# '''ord pass only strins chr pass only numbers'''
# print(ord('p'))          # 112
# print(chr(80))             # P
# y=b"python"
# y[0]=80        # no modifications  TypeError: 'bytes' object does not support item assignment
# v=b'[1,2,3]'
# print(list(v))    #  [91, 49, 44, 50, 44, 51, 93]
# v=b'[7,8,9]'
# print(list(v))      #  [91, 55, 44, 56, 44, 57, 93]
# print(ord('['))       # 91
# print(ord(','))        #  44  
# print(chr('91'))        #[
# m=bytearray(b"python")   # bytearray(b'python')   bytearray is mutable modifications made
# print(m)
# m=bytearray("python") 
# print(m)                 #  TypeError: string argument without an encoding
# print(m[0])               #  112
# print(m[0])
# m[0]=80
# print(m)
# in the case of mutable bytearry in the case of immutable bytes
