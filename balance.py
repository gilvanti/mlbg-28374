
def remove_task(work,linha):
    """Remover conexões com processos finalizados"""

    while (linha > 0):
        if  len(work) == 1:
            if work[0] > 1:
                work[0] = work[0]-1
                linha = linha - 1
            elif work[0] == 1:
                work[0] = work[0]-1
                linha = linha - 1
        elif len(work) > 1:
            if work[0] > 1:
                work[0] = work[0]-1
                linha = linha - 1
            elif work[0] == 1:
                work.pop(0)
                linha = linha - 1
        else:
            return work

    return work


def balace_work(line,umax,ttask,linhas,custo,contador,work):
    """balanceamento de conexão de usuários"""

    #verificação se existe processos que concluiu seu tempo de execução
    linha = int(linhas[(contador-ttask)])
    if (contador-ttask) >= 2 and linha > 0:
        work = remove_task(work,linha)

    #Conexão de novos usuários
    cont = 0
    while (cont < len(work)):
        if line > 0 :
            if work[cont] < umax:
                work[cont] = work[cont]+1
                line = line - 1
            else:
                work.append(1)
                line = line - 1
                cont = cont + 1
        else:
            break

    print(work)
    custo = custo + len(work)
    return work, custo


def open_arquivo():
    """Abrir arquivos com input"""

    with open('input.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    return linhas


def main():

    linhas = open_arquivo()
    ttask = int(linhas[0])
    umax = int(linhas[1])
    contador = 0
    work = []
    custo = 0

    for line in linhas:
        if contador >= 2:
            if not work:
                if int(line) > 0:
                    work.insert(0,0)
                    work, custo = balace_work(int(line),umax,ttask,linhas,custo,
                                                contador,work)
                    contador += 1
                else:
                    pass
            else:
                work, custo = balace_work(int(line),umax,ttask,linhas,custo,
                                            contador,work)
                contador += 1
        else:
            contador += 1

    while (work[0] > 0):
        linha = int(linhas[(contador-ttask)])
        work = remove_task(work,linha)
        contador += 1
        print(work)
        if work[0] == 0 :
            print(custo)
        else:
            custo = custo + len(work)


if __name__== "__main__":
  main()
