import sys

    
try :
    val2=sys.argv[1]
except :
    val2='기본값2'
    
try :
    val3=sys.argv[2]
except :
    val3='기본값3'
    
try :
    val4=sys.argv[3]
except :
    val4='기본값4'

try :
    val5=sys.argv[4]
except :
    val5='기본값5'    
    
print('첫인자는 파일명 : ' , sys.argv[0]) 
print('val2 : ' , val2) 
print('val3 : ' , val3) 
print('val4 : ' , val4) 
print('val5 : ' , val5) 