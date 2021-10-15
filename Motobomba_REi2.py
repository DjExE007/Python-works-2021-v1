#Prototipo formula de volumen m3

'''ancho = input('Digite el valor del ancho del tanque' )
largo = input('Digite el valor del largo del tanque')
alto = input('Digite el valor de la altura del tanque')

ancho = int(ancho)
largo = int(largo)
alto = int(alto)


volumen_tanquei2 = (ancho * largo) * alto

print(volumen_tanquei2)'''

#Funcion formula de volumen

def fun_vol_tanqueib (ancho, largo, alto):
    ancho = int(ancho)
    largo = int(largo)
    alto = int(alto)
    volumen_tanqueib = ancho * largo * alto
    return volumen_tanqueib


ancho = input(' Digite el valor del ancho del tanque : ' )
largo = input(' Digite el valor del largo del tanque : ')
alto = input(' Digite el valor de la altura del tanque : ')

resultado_volumen = fun_vol_tanqueib(ancho,largo, alto)

motobomba_desempeño =  0.5*3

tiempo_tanque_llenado = resultado_volumen / motobomba_desempeño

equivalencia_horas_ttl = tiempo_tanque_llenado / 60

print('La motobomba llenará el tanque de ' + str(resultado_volumen) + 'm3' + ' en ' + str(tiempo_tanque_llenado) + ' minutos, equivalente a ' +  str(equivalencia_horas_ttl) + ' horas.')
