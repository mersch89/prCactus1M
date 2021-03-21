from PIL import Image

#CONTADORES
fo = 1
br = 1
bo = 1
oj = 1

#Medidas 626x684

fondo = 'f'+str(fo)+'.png'
brazo = 'br'+str(br)+'.png'
ojo = 'o'+str(oj)+'.png'
boca = 'bo'+str(bo)+'.png'

img_fondo = Image.open(fondo)
img_brazo = Image.open(brazo)
img_ojo = Image.open(ojo)
img_boca = Image.open(boca)


"""
dimensiones = (100,100)
img_ok_resize = img_ok.resize(dimensiones)
#img_ok_redimensionada.save('ok_redimen.png')
"""

#ESTA PARTE FUNCIONA BIEN. GUARDA LA IMAGEN.
"""
img_fondo.paste(brazo,(0,0),brazo)
img_fondo.paste(ojo,(0,0),ojo)
img_fondo.paste(boca,(0,0),boca)
#img_fondo.show()
img_fondo.save('fo'+str(fo)+'br'+str(br)+'bo'+str(bo)+'oj'+str(oj)+'.png')
"""

#while br <= 3:
#    while bo < = 3:


#while bo <= 3:
for x in range(1):
    oj = 1
    ojo = 'o'+str(oj)+'.png'
    img_ojo = Image.open(ojo)
    img_boca = Image.open(boca)
    #for i in range (8):
    while bo <= 8:
        if oj <= 11:
            img_fondo.paste(img_brazo,(0,0),img_brazo)
            img_fondo.paste(img_ojo,(0,0),img_ojo)
            img_fondo.paste(img_boca,(0,0),img_boca)
            img_fondo.save('fo'+str(fo)+'br'+str(br)+'bo'+str(bo)+'oj'+str(oj)+'.png')
            oj += 1
            ojo = 'o'+str(oj)+'.png'
            if oj <= 11:
                img_ojo = Image.open(ojo)
                img_fondo = Image.open(fondo)
        else:
            print('Ojo llegó a 5')
            oj = 1
            ojo = 'o'+str(oj)+'.png'
            img_ojo = Image.open(ojo)  
            bo += 1
            boca = 'bo'+str(bo)+'.png'
            if bo <= 8:
                img_boca = Image.open(boca)
