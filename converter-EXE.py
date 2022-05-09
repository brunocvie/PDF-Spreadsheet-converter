import tabula
import tkinter as tk
from tkinter import simpledialog, messagebox

ROOT = tk.Tk()

ROOT.withdraw

def conversor(arquivo, saida):

    try:

        tabula.convert_into(arquivo + ".pdf", saida + ".csv", output_format="csv", pages='all')

        messagebox.showinfo(title="CONCLUÍDO", message="CONVERSÃO REALIZADA COM SUCESSO")

    except:

        messagebox.showinfo(title="ATENÇÃO", message="ALGO DEU ERRADO!")


arquivo = simpledialog.askstring(title="ARQUIVO", prompt="Escreva o nome do arquivo: ")
saida = simpledialog.askstring(title="SAÍDA", prompt="Nome do arquivo de saída: ")

conversor(arquivo, saida)
