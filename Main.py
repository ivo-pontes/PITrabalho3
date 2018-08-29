#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Rotulacao import Rotulacao

if __name__ == '__main__':
	print("Processamento de Imagens.")

	rotulacao = Rotulacao("img/black_white.png")
	rotulacao.carregarImagem()
	op = -1

	menuStr = "\n\nDigite 0 para sair.\nMenu:\n"
	menuStr += "Rotulação\n1 - Rotular\n"

	while op != 0:
		op = input(menuStr)
		op = int(op)
		if op == 1:
			rotulacao.executar()
			
	print("Fim execução!!")
