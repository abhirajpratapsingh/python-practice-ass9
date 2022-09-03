# Q 5 : Write a python script to print first N odd natural numbers in reverse order

take_num = int ( input ( 'enter the number you want to print :' ) )
loop_vari = 1 
while loop_vari <= take_num :
    loop_vari2 = 2 * take_num - 1
    take_num -= 1
    print ( loop_vari2 )