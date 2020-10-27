#LIST COMPREHENSION

def ehPrimo(num):
    for i in range(2,num-1):
        if num%i==0:
            return False
    return True

nums = list(range(0,10))
quadrados = []
for num in nums:
    quadrados.append(num**2)

quadrados2 = [num**2 for num in range(0,10)]

impares = [num%2 for num in range(0,10)]


primos = [ehPrimo(x) for x in range(1,100)]
#SINTAXE: FUNÇÃO(VAR) for VAR in ITERAVEL

#LAMBDA FUNCTIONS (FUNÇÃO ANÔNIMA)

inputs_usuarios = ['    Josicleia', 'Rosângela  ', 'MATILDE', 'jose', 'chicO\n', 'a_tal_da_sandrinha']

#SEM LIST COPREHENSION, COM FOR E LISTA NOVA
nomes_limpos = []
for nome in inputs_usuarios:
    nomes_limpos.append(nome.upper().strip())
print(nomes_limpos)

#COM LIST COMPREHENSION
nomes_limpos = [nome.upper().strip() for nome in inputs_usuarios]
print(nomes_limpos)

#MAP COM FUNÇÃO
def limpa_nome(nome):
    return nome.upper().strip()
nomes_limpos = list(map(limpa_nome,nomes_limpos))
print(nomes_limpos)

#MAP COM LAMBDA
nomes_limpos = list(map(lambda nome: nome.upper().strip(),nomes_limpos))
print(nomes_limpos)

#(LAMBDA === ARROW FUNCTION NO JAVASCRIPT)