# Q 4 : Write a python script to print first N odd natural numbers

take_num = int ( input ( 'enter the number you want to print :' ) )
loop_vari , temp  = 1 , 1
while loop_vari <= take_num :
    print ( temp )
    temp += 2
    loop_vari += 1