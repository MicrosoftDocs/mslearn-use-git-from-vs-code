declaracao = True
while declaracao:
    msg = str(input('Insira sua mensagem:'))
    if msg != '':
        print(msg)
        declaracao = False
    else:
        print('finish process.')
    