def xor(p, q):
	return not( p and q ) and ( p or q )

def vv(p, q):
	return ( p and not q ) or ( not p and q )


print("===== Primeiro Exercicio =====\n")

rXOR = (True) or (False) and (True) and xor( True , True )
print( 'Resposta XOR: ', rXOR )

rVV = (True) or (False) and (True) and xor( True , True )
print( 'Resposta VV: ', rVV )

print('\n===== Segundo Exercicio =====\n')


salario = 15000
idade   = 44
tempo   = 20

rXOR = ( salario > 2000 ) or ( idade < 30 ) and ( tempo == 10 or idade > 20 ) and xor( not(salario < 3000), ( idade < 60 ) ) 
print( 'Resposta XOR: ', rXOR )

rVV = ( salario > 2000 ) or ( idade < 30 ) and ( tempo == 10 or idade > 20 ) and vv( not(salario < 3000), ( idade < 60 ) ) 
print( 'Resposta VV: ', rVV )


print('\n===== Terceiro Exercicio =====\n')

gato    = False
passaro = True
juca    = False
joana   = True

rXOR = xor( gato, passaro ) and not( juca or joana )
print( 'Resposta XOR: ', rXOR )

rVV  = vv( gato, passaro ) and not( juca or joana )
print( 'Resposta VV: ', rVV )
