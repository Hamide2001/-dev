menu = {'kola':10,
       'tuz':40,
       'pasta':50,
       'kek':25,
       'soda' :8,
       'defter':35, 
       'su' :3,
       'sut':10,
       'cay':100, 
       'sabun':16}

print("----Menu su sekildedir----")
for i in menu:
    print(i)

almak_istenen = input("Ne almak istersiniz? : ")

if(almak_istenen == 'kola'):
    print("Hesap: ",menu['kola'])
    para = int(input("Para giriniz: "))
    kalan = para - menu['kola']
    print("Kalan para: ",kalan)

elif(almak_istenen == 'tuz'):
    print("Hesap: ",menu['tuz'])
    para = int(input("Para giriniz: "))
    kalan = para-menu['tuz']
    print("Kalan para: ",kalan)

elif(almak_istenen == 'pasta'):
    print("Hesap: ", menu['pasta'])
    para = int(input("Para giriniz: "))
    kalan = para-menu['pasta']
    print("Kalan para: ",kalan)

elif(almak_istenen == 'kek'):
    print("Hesap: ", menu['kek'])
    para = int(input("Para giriniz: "))
    kalan = para-menu['kek']
    print("Kalan para: ",kalan)

elif(almak_istenen == 'soda'):
    print("Hesap: ", menu['soda'])
    para = int(input("Para giriniz: "))
    kalan = para-menu['soda']
    print("Kalan para: ",kalan)

elif(almak_istenen == 'defter'):
    print("Hesap: ",menu['defter'])
    para = int(input("Para giriniz: "))
    kalan = para-menu['defter']
    print("Kalan para: ",kalan)

elif(almak_istenen == 'su'):
    print("Hesap: ", menu['su'])
    para = int(input("Para giriniz: "))
    kalan = para-menu['su']
    print("Kalan para: ",kalan)

elif(almak_istenen == 'sut'):
    print("Hesap: ", menu['sut'])
    para = int(input("Para giriniz: "))
    kalan = para-menu['sut']
    print("Kalan para: ",kalan)

elif(almak_istenen == 'cay'):
    print("Hesap: ", menu['cay'])
    para = int(input("Para giriniz: "))
    kalan = para-menu['cay']
    print("Kalan para: ",kalan)

elif(almak_istenen == menu['sabun']):
    print("Hesap: ",menu['sabun'])
    para = int(input("Para giriniz: "))
    kalan = para-menu['sabun']
    print("Kalan para: ",kalan)

else:
    print("Hesap 0. Girdiginiz urun marketimizde bulunmamaktadir.")