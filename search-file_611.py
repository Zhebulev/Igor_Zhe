import os
stroka = ''
stroka = input('введите, что вы ищите в папке "офис_611": ')
g = [os.path.join(z, i)
     for z, x, c in os.walk('Y:\\Офис_611')
     for i in c if stroka in i]
print('\nвот что сколько нашёл: ', len(g),'\n')
for i in g:
    print(i,'\n')


  
            
            

            
            
            

