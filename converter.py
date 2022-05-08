import tabula


arquivo = input("Escreva o nome do arquivo: ")

saida = input("Escreva o nome do arquivo de saída: ")



tabula.convert_into(arquivo + ".pdf", saida + ".csv", output_format="csv", pages='all')
