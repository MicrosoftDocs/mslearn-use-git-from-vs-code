lt = []
declaracao = True
while declaracao:
    msg = str(input('Insira sua mensagem:'))
    if msg != '':
        print(msg)
        print("test")        
        print(0, 1, 1, 0, 0)
        dsc = {
            'mensagem': msg
        }
        lt.append(dsc)
    else:
        print('finish process.')
        declaracao = False
for dsc in lt:
    print('Mensagem:', dsc['mensagem'])   