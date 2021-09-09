import tabula


arquivo = input("Escreva o nome do arquivo .pdf")

saida = input("Escreva o nome do arquivo de saída .csv")



tabula.convert_into(arquivo, saida, output_format="csv", pages='all')
