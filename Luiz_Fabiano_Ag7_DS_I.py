# PROGRAMA PARA CLASSIFICAR O CONSUMO DE ÁGUA

print("##############################################")
print("       CLASSIFICAÇÃO DO CONSUMO DE ÁGUA       ")
print("##############################################\n")

# Entrada de dados - é sempre bom dar um destaque aos blocos nesse inicio de programação
tipo = input("Digite o tipo de imóvel (casa, apartamento ou comercial): \n").lower() #item adicionado pela IA após erros consecutivos. Verificar o modivo desse comando
consumo = float(input("Digite o consumo mensal de água em m³: \n")) #Tive que substituit a varialvel Int por Float, devido aos erros com números quebrados

# Tomada de decisão - utilizando o comando novo elif no lugar encadeamento com if else. Muito melhor!
if tipo == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.\n") #A parte boa que o Vsacode ajuda durante o desenvolvimento do programa, dando dicas para construir o programa

elif tipo == "apartamento" and consumo < 10: #refino na IA, estava dando erro na lógica, foi acrescentado o ":" verifiar no programa original se esta correto
    print("Consumo econômico – excelente controle de água!\n")

elif (tipo == "apartamento" or tipo == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.\n   ")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.\n") #frase  sugerida pelo programa VScode. não precisei digitar.