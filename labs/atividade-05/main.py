def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    tf = 0
    #checa quem possui a maior/menor quantidade de figurinhas
    qmenor = figurinhas_da_maria if len(figurinhas_da_maria) <= len(figurinhas_do_joao) else figurinhas_do_joao
    qmaior  = figurinhas_da_maria if len(figurinhas_da_maria) >= len(figurinhas_do_joao) else figurinhas_do_joao

    for i, n_figurinha in enumerate(qmenor):
        if not n_figurinha in qmaior:
            for n in range(i, len(qmaior)):
                if n_figurinha != qmaior[n]:
                    tff = qmaior[n]
                    qmaior[n] = n_figurinha
                    qmenor[i] = tff
                    tf = tf + 1
                    break
    return tf

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    print(maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao))
